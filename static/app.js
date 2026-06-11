"use strict";

// ── State ─────────────────────────────────────────────────────────────────────
let currentData = null;
const _charts     = {};
const _encDataMap = {};

// ── DOM refs ──────────────────────────────────────────────────────────────────
const $ = id => document.getElementById(id);
const patientSelect  = $("patientSelect");
const emptyState     = $("emptyState");
const loadingState   = $("loadingState");
const dashboard      = $("dashboard");
const tabNav         = $("tabNav");
const patientInfoBar = $("patientInfoBar");

// ── Bootstrap ─────────────────────────────────────────────────────────────────
(async () => {
  await Promise.all([loadPatients(), loadDatasetInfo()]);
  patientSelect.addEventListener("change", e => loadPatient(e.target.value));
  document.querySelectorAll(".tab-btn").forEach(btn =>
    btn.addEventListener("click", () => activateTab(btn.dataset.tab))
  );
  $("labSearch").addEventListener("input", e => filterLabs(e.target.value));
  $("noteSearch").addEventListener("input", e => filterNotes(e.target.value));
})();

// ── Dataset info banner ───────────────────────────────────────────────────────
async function loadDatasetInfo() {
  try {
    const res = await fetch("/api/info");
    if (!res.ok) return;
    const info = await res.json();
    renderDatasetBanner(info);
  } catch (_) { /* optional endpoint — ignore errors */ }
}

function renderDatasetBanner(info) {
  const banner = $("datasetBanner");
  if (!banner) return;

  const badge = $("dsBadge");
  badge.textContent = info.label || info.mode;
  badge.style.setProperty("--ds-color", info.color || "#3b82f6");

  $("dsDesc").textContent = info.description || "";

  const inc = info.includes || {};
  const chips = [
    ["conditions",  "fa-stethoscope",    "Diagnoses"],
    ["medications", "fa-pills",          "Medications"],
    ["notes",       "fa-file-medical",   "Notes"],
    ["vitals",      "fa-heart-pulse",    "Vitals"],
    ["labs",        "fa-flask-vial",     "Labs"],
    ["procedures",  "fa-syringe",        "Procedures"],
  ];
  const wrap = $("dsIncludes");
  wrap.innerHTML = "";
  chips.forEach(([key, icon, label]) => {
    const on = inc[key] !== false;
    const el = document.createElement("span");
    el.className = on ? "ds-chip ds-chip-on" : "ds-chip ds-chip-off";
    el.innerHTML = `<i class="fas ${icon}"></i> ${label}`;
    if (!on) el.title = `${label} excluded from this dataset`;
    wrap.appendChild(el);
  });

  if (info.bundleCount != null) {
    $("dsBundleCount").textContent = `${info.bundleCount.toLocaleString()} patients`;
  }

  banner.classList.remove("hidden");
}

// ── Patient list ──────────────────────────────────────────────────────────────
async function loadPatients() {
  const res  = await fetch("/api/patients");
  const data = await res.json();
  data.patients.forEach(id => {
    const opt = document.createElement("option");
    opt.value       = id;
    opt.textContent = `Patient ${id}`;
    opt.style.backgroundColor = "#21262d";
    opt.style.color = "#e6edf3";
    patientSelect.appendChild(opt);
  });
}

// ── Load patient ──────────────────────────────────────────────────────────────
async function loadPatient(id) {
  if (!id) { showEmpty(); return; }
  showLoading();
  try {
    const res = await fetch(`/api/patients/${id}`);
    if (!res.ok) throw new Error("Not found");
    currentData = await res.json();
    render(currentData);
    showDashboard();
    activateTab("overview");
  } catch (err) {
    alert("Error loading patient: " + err.message);
    showEmpty();
  }
}

// ── Visibility helpers ────────────────────────────────────────────────────────
function _hidePopPanel() {
  $("populationPanel").classList.add("hidden");
  $("popToggleBtn").classList.remove("active");
}
function showEmpty() {
  _hidePopPanel();
  emptyState.classList.remove("hidden");
  loadingState.classList.add("hidden");
  dashboard.classList.add("hidden");
  tabNav.classList.add("hidden");
  patientInfoBar.classList.add("hidden");
  $("patientBadge").classList.add("hidden");
}
function showLoading() {
  _hidePopPanel();
  loadingState.classList.remove("hidden");
  emptyState.classList.add("hidden");
  dashboard.classList.add("hidden");
  tabNav.classList.add("hidden");
}
function showDashboard() {
  _hidePopPanel();
  loadingState.classList.add("hidden");
  dashboard.classList.remove("hidden");
  tabNav.classList.remove("hidden");
  patientInfoBar.classList.remove("hidden");
  $("patientBadge").classList.remove("hidden");
}

// ── Tab switching ─────────────────────────────────────────────────────────────
function activateTab(name) {
  document.querySelectorAll(".tab-btn").forEach(b =>
    b.classList.toggle("active", b.dataset.tab === name)
  );
  document.querySelectorAll(".tab-pane").forEach(p =>
    p.classList.toggle("hidden", p.id !== `tab-${name}`)
  );
}

// ── Master render ─────────────────────────────────────────────────────────────
function render(d) {
  renderInfoBar(d.demographics);
  renderDemographics(d.demographics);
  renderVitals(d.vitals);
  renderMedications(d.medications);
  renderConditions(d.conditions);
  renderTests(d.diagnosticReports);
  renderLabs(d.labs);
  renderComplaint(d);
  renderValidation(d);
  renderEncounters(d.encounters);
  renderNotes(d.notes || []);
  renderAnalytics(d);
  renderICDReport(d);
}

// ── Info bar ──────────────────────────────────────────────────────────────────
function renderInfoBar(demo) {
  $("piName").textContent      = `Patient ${demo.subjectId}`;
  $("piGenderAge").textContent =
    `${demo.gender}${demo.age != null ? ", ~" + demo.age + " yrs" : ""}`;
  $("piRace").textContent      = demo.race;
  $("piMrn").textContent       = `MRN: ${demo.subjectId}`;
  $("piDeceased").classList.toggle("hidden", !demo.deceased);
}

// ── Demographics ──────────────────────────────────────────────────────────────
function renderDemographics(demo) {
  const fields = [
    ["Patient ID",      demo.subjectId],
    ["Gender",          demo.gender],
    ["Birth Date",      demo.birthDate || "—"],
    ["Age (approx.)",  demo.age != null ? demo.age + " yrs" : "—"],
    ["Race",            demo.race],
    ["Ethnicity",       demo.ethnicity],
    ["Birth Sex",       demo.birthSex],
    ["Marital Status", demo.maritalStatus || "—"],
    ["Language",        demo.language || "—"],
    ["Anchor Year",     demo.anchorYear || "—"],
    ["Deceased",        demo.deceased || "No"],
  ];
  $("demoContent").innerHTML = fields.map(([lbl, val]) => `
    <div class="demo-cell">
      <span class="demo-label">${lbl}</span>
      <span class="demo-value">${esc(val)}</span>
    </div>`).join("");
}

// ── Vitals ────────────────────────────────────────────────────────────────────
function renderVitals(vitals) {
  const el = $("vitalsContent");
  if (!vitals.length) {
    el.innerHTML = `<p class="col-span-full text-sm text-gray-500 p-5">No vital signs recorded.</p>`;
    return;
  }
  el.innerHTML = vitals.map(v => {
    const valStr   = typeof v.value === "number" ? v.value.toFixed(1) : v.value;
    const nr       = v.normalRange;
    const rangeStr = nr
      ? `<span class="text-xs" style="color:#484f58;">${nr[0]}–${nr[1]}</span>`
      : "";
    const valueColor = v.status === "abnormal" ? "#f85149" : "#79c0ff";
    const iconColor  = v.status === "abnormal" ? "#f85149" : "#79c0ff";
    return `
    <div class="vital-card ${v.status}">
      <i class="fas ${v.icon} text-lg" style="color:${iconColor};"></i>
      <span class="text-xs mt-1" style="color:#6e7681;">${esc(v.name)}</span>
      <span class="font-bold text-lg leading-tight" style="color:${valueColor};">
        ${esc(valStr)}
        <span class="text-xs font-normal" style="color:#484f58;">${esc(v.unit)}</span>
      </span>
      ${rangeStr}
      <span class="text-[10px] mt-1" style="color:#6e7681;">${v.time || ""}</span>
    </div>`;
  }).join("");
}

// ── Medications ───────────────────────────────────────────────────────────────
function renderMedications(meds) {
  $("medCount").textContent = meds.length;
  const el = $("medsContent");
  if (!meds.length) { $("medsEmpty").classList.remove("hidden"); return; }
  el.innerHTML = meds.map(m => `
    <div class="list-row">
      <i class="fas fa-capsules shrink-0 mt-0.5" style="color:#a78bfa;"></i>
      <div class="min-w-0">
        <p class="font-medium truncate" style="color:#cdd9e5;">${esc(m.name)}</p>
        <p class="text-xs" style="color:#6e7681;">
          ${m.dose ? esc(m.dose) : ""}${m.route ? " · " + esc(m.route) : ""}
          ${m.start ? " · " + m.start : ""}
        </p>
      </div>
      <span class="ml-auto shrink-0 ${m.status === "completed" ? "badge-completed" : "badge-inactive"}">
        ${esc(m.status)}
      </span>
    </div>`).join("");
}

// ── Conditions ────────────────────────────────────────────────────────────────
function renderConditions(conds) {
  $("condCount").textContent = conds.length;
  const el = $("condsContent");
  if (!conds.length) { $("condsEmpty").classList.remove("hidden"); return; }
  el.innerHTML = conds.map(c => `
    <div class="list-row">
      <i class="fas fa-circle-dot shrink-0 mt-0.5 text-xs" style="color:#2dd4bf;"></i>
      <div class="min-w-0">
        <p class="font-medium" style="color:#cdd9e5;">${esc(c.name)}</p>
        ${c.code
          ? `<p class="text-xs font-mono" style="color:#6e7681;">${esc(c.codeSystem)} ${esc(c.code)}</p>`
          : ""}
      </div>
      <span class="ml-auto shrink-0 ${c.status === "active" ? "badge-teal" : "badge-inactive"}">
        ${esc(c.status)}
      </span>
    </div>`).join("");
}

// ── Suggested Tests ───────────────────────────────────────────────────────────
function renderTests(reports) {
  $("testsCount").textContent = reports.length;
  const el = $("testsContent");
  if (!reports.length) { $("testsEmpty").classList.remove("hidden"); return; }
  el.innerHTML = reports.map(r => `
    <div class="list-row">
      <i class="fas fa-vial shrink-0 mt-0.5" style="color:#38bdf8;"></i>
      <div class="min-w-0">
        <p class="font-medium" style="color:#cdd9e5;">${esc(r.name)}</p>
        <p class="text-xs" style="color:#6e7681;">${r.category || ""} ${r.time ? "· " + r.time : ""}</p>
      </div>
      <span class="ml-auto shrink-0 badge-sky">${esc(r.status)}</span>
    </div>`).join("");
}

// ── Labs ──────────────────────────────────────────────────────────────────────
function renderLabs(labs) {
  $("labCount").textContent = labs.length;
  const tbody = $("labsBody");
  if (!labs.length) { $("labsEmpty").classList.remove("hidden"); return; }

  tbody.innerHTML = labs.map(l => {
    const flagClass = l.flag ? `flag-${l.flag}` : "";
    const flagIcon  = { H: "↑", L: "↓", HH: "↑↑", LL: "↓↓", A: "!" }[l.flag] || l.flag || "";
    const refStr    = (l.refLow != null && l.refHigh != null)
      ? `${l.refLow} – ${l.refHigh}` : "—";
    const valStr    = typeof l.value === "number" ? l.value.toFixed(2) : (l.value ?? "—");

    return `
    <tr class="lab-row" data-name="${esc(l.name.toLowerCase())}">
      <td class="px-4 py-2.5 font-medium" style="color:#cdd9e5;">${esc(l.name)}</td>
      <td class="px-4 py-2.5 text-right font-mono font-semibold ${flagClass}">
        ${esc(String(valStr))}
        <span class="text-xs ml-1" style="color:#484f58;">${esc(l.unit)}</span>
      </td>
      <td class="px-4 py-2.5 text-center ${flagClass}">${flagIcon}</td>
      <td class="px-4 py-2.5 text-center text-xs font-mono hidden sm:table-cell" style="color:#484f58;">${refStr}</td>
      <td class="px-4 py-2.5 text-xs hidden md:table-cell" style="color:#6e7681;">${l.time || "—"}</td>
    </tr>`;
  }).join("");
}

function filterLabs(query) {
  const q = query.toLowerCase().trim();
  document.querySelectorAll(".lab-row").forEach(row => {
    const name = row.dataset.name || "";
    row.style.display = !q || name.includes(q) ? "" : "none";
  });
}

// ── Chief Complaint ───────────────────────────────────────────────────────────
function renderComplaint(d) {
  $("chiefComplaintText").textContent = d.chiefComplaint || "Not recorded";

  const enc    = d.encounters[0];
  const admDet = $("admissionDetails");
  if (enc) {
    const rows = [
      ["Encounter Type",        enc.type || enc.cls],
      ["Admission",             enc.start],
      ["Discharge",             enc.end],
      ["Admit Source",          enc.admitSource],
      ["Discharge Disposition", enc.dischDisp],
      ["Insurance",             enc.insurance],
    ].filter(([, v]) => v);
    admDet.innerHTML = rows.map(([lbl, val]) => `
      <div class="flex justify-between gap-4">
        <span style="color:#6e7681;">${esc(lbl)}</span>
        <span class="font-medium text-right" style="color:#cdd9e5;">${esc(String(val))}</span>
      </div>`).join("");
  } else {
    admDet.innerHTML = `<p style="color:#6e7681;">No encounter data.</p>`;
  }

  const primaryDiag = $("primaryDiagnoses");
  const encId       = enc?.id;
  const encDiags    = encId
    ? d.conditions.filter(c => c.encounterRef === encId)
    : d.conditions;

  primaryDiag.innerHTML = encDiags.length
    ? encDiags.map(c => `
      <div class="flex items-start gap-2">
        <i class="fas fa-circle-dot text-xs mt-1 shrink-0" style="color:#fb923c;"></i>
        <div>
          <p style="color:#cdd9e5;">${esc(c.name)}</p>
          ${c.code
            ? `<p class="text-xs font-mono" style="color:#6e7681;">${esc(c.codeSystem)} ${esc(c.code)}</p>`
            : ""}
        </div>
      </div>`).join("")
    : `<p style="color:#6e7681;">No diagnoses linked to this encounter.</p>`;
}

// ── Validation tab ────────────────────────────────────────────────────────────
function renderValidation(d) {
  $("diagCount").textContent = d.conditions.length;
  const diagEl = $("diagContent");
  if (!d.conditions.length) { $("diagEmpty").classList.remove("hidden"); }
  else {
    diagEl.innerHTML = d.conditions.map((c, i) => `
      <div class="list-row">
        <span class="shrink-0 text-xs font-bold rounded-full w-6 h-6 flex items-center justify-center"
              style="background:rgba(244,63,94,0.12);color:#fb7185;">
          ${i + 1}
        </span>
        <div class="min-w-0">
          <p class="font-medium" style="color:#cdd9e5;">${esc(c.name)}</p>
          ${c.code
            ? `<p class="text-xs font-mono" style="color:#6e7681;">${esc(c.codeSystem)} · ${esc(c.code)}</p>`
            : ""}
        </div>
        <span class="ml-auto shrink-0 ${c.status === "active" ? "badge-rose" : "badge-inactive"}">
          ${esc(c.status)}
        </span>
      </div>`).join("");
  }

  const tmEl = $("treatMedsContent");
  if (!d.medications.length) { $("treatMedsEmpty").classList.remove("hidden"); }
  else {
    tmEl.innerHTML = d.medications.map(m => `
      <div class="list-row">
        <i class="fas fa-prescription-bottle-medical shrink-0 mt-0.5" style="color:#c084fc;"></i>
        <div class="min-w-0">
          <p class="font-medium truncate" style="color:#cdd9e5;">${esc(m.name)}</p>
          <p class="text-xs" style="color:#6e7681;">${m.dose || ""}${m.route ? " · " + m.route : ""}</p>
        </div>
      </div>`).join("");
  }

  $("procCount").textContent = d.procedures.length;
  const prEl = $("procsContent");
  if (!d.procedures.length) { $("procsEmpty").classList.remove("hidden"); }
  else {
    prEl.innerHTML = d.procedures.map(p => `
      <div class="list-row">
        <i class="fas fa-syringe shrink-0 mt-0.5" style="color:#4ade80;"></i>
        <div class="min-w-0">
          <p class="font-medium" style="color:#cdd9e5;">${esc(p.name)}</p>
          <p class="text-xs" style="color:#6e7681;">${p.time || ""}</p>
        </div>
      </div>`).join("");
  }
}

// ── Encounters ────────────────────────────────────────────────────────────────
function renderEncounters(encounters) {
  // Destroy old per-encounter charts and clear data map
  Object.keys(_charts).filter(k => k.startsWith("encChart_")).forEach(k => _destroyChart(k));
  Object.keys(_encDataMap).forEach(k => delete _encDataMap[k]);

  const total = encounters.reduce((n, e) => n + 1 + e.children.length, 0);
  $("encTotal").textContent = `${total} encounter${total !== 1 ? "s" : ""}`;

  const el = $("encountersContent");
  if (!encounters.length) {
    $("encountersEmpty").classList.remove("hidden");
    return;
  }

  // Store encounter data for lazy chart rendering
  encounters.forEach((enc, idx) => { _encDataMap[idx] = enc; });

  el.innerHTML = encounters.map((enc, idx) => {
    const cls         = enc.cls === "IMP" ? "Inpatient" : (enc.cls === "ACUTE" ? "ICU" : enc.cls);
    const isInpatient = enc.cls === "IMP";
    const numBadge    = isInpatient ? "badge-num-blue" : "badge-num-indigo";
    const typeBadge   = isInpatient ? "badge-type-blue" : "badge-type-indigo";
    const statusBadge = enc.status === "finished" ? "badge-finished" : "badge-ongoing";
    const hasChildren = enc.children.length > 0;
    const ed          = enc.encounterData || {};

    const nConds   = ed.conditions?.length        || 0;
    const nMeds    = ed.medications?.length       || 0;
    const nProcs   = ed.procedures?.length        || 0;
    const nLabs    = ed.labs?.length              || 0;
    const nVitals  = ed.vitals?.length            || 0;
    const nReports = ed.diagnosticReports?.length || 0;
    const nNotes   = ed.notes?.length             || 0;
    const totalItems = nConds + nMeds + nProcs + nLabs + nVitals + nReports + nNotes;

    // Abnormal lab count for quick alert
    const nAbnormal = (ed.labs || []).filter(l => l.flag && l.flag !== "N").length;

    // ── ICU stays ──────────────────────────────────────────────────────────
    const icuHtml = hasChildren ? `
      <div class="enc-icu-section">
        <div class="enc-icu-title">
          <i class="fas fa-bed-pulse"></i> ICU Stay${enc.children.length > 1 ? "s" : ""}
        </div>
        <div class="enc-icu-grid">
          ${enc.children.map(icu => `
          <div class="icu-card">
            <div class="flex items-center gap-2 font-semibold mb-2" style="color:#79c0ff;font-size:0.85rem;">
              <i class="fas fa-location-dot" style="color:#388bfd;"></i>
              ${esc(icu.location || "Unknown Unit")}
            </div>
            <div class="enc-icu-kv-grid">
              ${kv("Admitted",   icu.start)}
              ${kv("Discharged", icu.end)}
              ${icu.los != null ? kv("LOS (days)", icu.los) : ""}
              ${kv("Status",     icu.status)}
            </div>
          </div>`).join("")}
        </div>
      </div>` : "";

    // ── Stats bar ──────────────────────────────────────────────────────────
    const statsBar = `
      <div class="enc-stats-bar">
        ${statChip("fa-stethoscope",          "#fb7185", nConds,   "Diagnos.")}
        ${statChip("fa-pills",                "#c084fc", nMeds,    "Meds")}
        ${statChip("fa-syringe",              "#4ade80", nProcs,   "Procs")}
        ${statChip("fa-heart-pulse",          "#f87171", nVitals,  "Vitals")}
        ${statChip("fa-flask-vial",           "#818cf8", nLabs,    "Labs")}
        ${statChip("fa-vial-circle-check",    "#38bdf8", nReports, "Reports")}
        ${nNotes > 0 ? statChip("fa-file-medical", "#34d399", nNotes, "Notes") : ""}
        ${nAbnormal > 0
          ? `<span class="enc-stat-chip enc-stat-abnormal">
               <i class="fas fa-triangle-exclamation"></i> ${nAbnormal} abnormal lab${nAbnormal !== 1 ? "s" : ""}
             </span>`
          : ""}
      </div>`;

    // ── Per-encounter chart canvas section ──────────────────────────────────
    const _dedupVitals = (() => {
      const m = {};
      (ed.vitals || []).forEach(v => {
        if (!m[v.name] || v.raw > m[v.name].raw) m[v.name] = v;
      });
      return Object.values(m).sort((a, b) => a.name.localeCompare(b.name));
    })();
    const _dedupLabs = (() => {
      const m = {};
      (ed.labs || []).forEach(l => {
        if (!m[l.name] || l.rawDt > m[l.name].rawDt) m[l.name] = l;
      });
      return Object.values(m).filter(l => typeof l.value === "number");
    })();
    const _hasDxChart   = (ed.conditions || []).length > 1;
    const _labsH        = Math.max(180, Math.min(_dedupLabs.length, 40) * 22 + 40);
    const _dxH          = Math.max(100, (ed.conditions || []).length * 30);
    // Vitals trend — needs ≥2 readings of same vital with a known normal range
    const _hasVtrend = (() => {
      const m = {};
      (ed.vitals || []).forEach(v => { if (v.normalRange) m[v.name] = (m[v.name] || 0) + 1; });
      return Object.values(m).some(n => n >= 2);
    })();
    // Lab vs reference range — deduplicated labs that have refLow/refHigh
    const _refLabs = (() => {
      const m = {};
      (ed.labs || []).forEach(l => { if (!m[l.name] || l.rawDt > m[l.name].rawDt) m[l.name] = l; });
      return Object.values(m)
        .filter(l => l.refLow != null && l.refHigh != null && typeof l.value === "number")
        .slice(0, 30);
    })();
    const _hasRefNorm = _refLabs.length > 0;
    const _refNormH   = Math.max(180, _refLabs.length * 22 + 40);

    const encChartSection = `
    <div class="enc-charts-block">
      <div class="enc-charts-block-header">
        <i class="fas fa-chart-column"></i> Charts &amp; Plots
      </div>
      <div class="enc-charts-grid-top">
        ${_dedupVitals.length ? `
        <div class="enc-chart-card">
          <div class="enc-chart-label"><i class="fas fa-heart-pulse" style="color:#f87171;"></i> Vital Signs <span class="enc-chart-hint">latest per type · red = abnormal</span></div>
          <div style="height:${Math.max(140, _dedupVitals.length * 32)}px;position:relative;">
            <canvas id="encChart_vitals_${idx}"></canvas>
          </div>
        </div>` : ""}
        ${nLabs > 0 ? `
        <div class="enc-chart-card">
          <div class="enc-chart-label"><i class="fas fa-flag" style="color:#818cf8;"></i> Lab Flag Distribution</div>
          <div style="height:200px;position:relative;">
            <canvas id="encChart_flags_${idx}"></canvas>
          </div>
        </div>` : ""}
      </div>
      ${_dedupLabs.length ? `
      <div class="enc-chart-card">
        <div class="enc-chart-label"><i class="fas fa-flask-vial" style="color:#818cf8;"></i> Lab Values <span class="enc-chart-hint">latest per test · sorted by severity · top 40</span></div>
        <div style="height:${_labsH}px;position:relative;">
          <canvas id="encChart_labs_${idx}"></canvas>
        </div>
      </div>` : ""}
      ${_hasDxChart ? `
      <div class="enc-chart-card" style="margin-top:0.75rem;">
        <div class="enc-chart-label"><i class="fas fa-stethoscope" style="color:#fb7185;"></i> Diagnoses</div>
        <div style="height:${_dxH}px;position:relative;">
          <canvas id="encChart_dx_${idx}"></canvas>
        </div>
      </div>` : ""}
      ${_hasVtrend ? `
      <div class="enc-chart-card" style="margin-top:0.75rem;">
        <div class="enc-chart-label"><i class="fas fa-chart-line" style="color:#58a6ff;"></i> Vitals Trend <span class="enc-chart-hint">normalised % of normal range · all readings over time</span></div>
        <div style="height:280px;position:relative;">
          <canvas id="encChart_vtrend_${idx}"></canvas>
        </div>
      </div>` : ""}
      ${_hasRefNorm ? `
      <div class="enc-chart-card" style="margin-top:0.75rem;">
        <div class="enc-chart-label"><i class="fas fa-ruler" style="color:#3fb950;"></i> Lab vs Reference Range <span class="enc-chart-hint">0–100 % = within range · red = outside · sorted by severity</span></div>
        <div style="height:${_refNormH}px;position:relative;">
          <canvas id="encChart_refnorm_${idx}"></canvas>
        </div>
      </div>` : ""}
    </div>`;

    return `
    <div class="enc-card" data-enc-idx="${idx}">
      <!-- ── Header ── -->
      <div class="enc-header" onclick="toggleEnc(this)">
        <div class="${numBadge}">${idx + 1}</div>
        <div class="min-w-0 flex-1">
          <p class="font-semibold" style="color:#cdd9e5;line-height:1.4;">
            ${esc(enc.type || cls)} Encounter
            ${hasChildren
              ? `<span class="badge-icu">${enc.children.length} ICU stay${enc.children.length > 1 ? "s" : ""}</span>`
              : ""}
            ${totalItems > 0
              ? `<span class="enc-items-chip">${totalItems} records</span>`
              : ""}
          </p>
          <p style="font-size:0.8125rem;color:#6e7681;margin-top:0.15rem;">
            <i class="fas fa-calendar-range" style="font-size:0.7rem;margin-right:0.3rem;"></i>
            ${enc.start || "?"} &nbsp;→&nbsp; ${enc.end || "ongoing"}
            ${enc.los != null ? `<span style="margin-left:0.75rem;color:#484f58;">LOS: ${enc.los}d</span>` : ""}
          </p>
        </div>
        <div class="shrink-0 flex flex-col items-end gap-1.5">
          <span class="${statusBadge}">${esc(enc.status)}</span>
          <span class="${typeBadge}">${cls}</span>
        </div>
        <i class="fas fa-chevron-down enc-chevron text-sm ml-3 shrink-0"></i>
      </div>

      <!-- ── Expandable body ── -->
      <div class="enc-body hidden">

        <!-- Chief Complaint -->
        ${encChiefComplaintBox(ed.chiefComplaint, ed.providers)}

        <!-- Admission details -->
        <div class="enc-admit-row">
          ${encDetail("fa-door-open",    "#6e7681", "Admit Source",    enc.admitSource)}
          ${encDetail("fa-door-closed",  "#6e7681", "Discharge Dispo", enc.dischDisp)}
          ${encDetail("fa-shield-halved","#6e7681", "Insurance",       enc.insurance)}
          ${encDetail("fa-clock",        "#6e7681", "Location",        enc.location)}
          ${enc.serviceType ? encDetail("fa-stethoscope", "#6e7681", "Service", enc.serviceType) : ""}
        </div>

        <!-- ICU stays -->
        ${icuHtml}

        <!-- Stats bar -->
        ${statsBar}

        <!-- Clinical Note (synthesized) or real note preview -->
        ${encClinicalNote(enc, ed)}

        <!-- ── Clinical data grid ── -->
        <div class="enc-clinical-grid">

          <!-- Row 1: Diagnoses + Medications -->
          <div class="enc-section-pair">
            ${encSectionDiagnoses(ed.conditions)}
            ${encSectionMedications(ed.medications)}
          </div>

          <!-- Row 2: Vitals (full width) -->
          ${encSectionVitals(ed.vitals)}

          <!-- Row 3: Labs (full width) -->
          ${encSectionLabs(ed.labs)}

          <!-- Row 4: Procedures + Reports -->
          <div class="enc-section-pair">
            ${encSectionProcedures(ed.procedures)}
            ${encSectionReports(ed.diagnosticReports)}
          </div>

          <!-- Row 5: Clinical Notes (full width, only when present) -->
          ${(ed.notes?.length) ? encSectionNotes(ed.notes) : ""}

        </div>

        <!-- ── Per-encounter charts (lazy) ── -->
        ${encChartSection}

      </div>
    </div>`;
  }).join("");
}

// ── Helpers used inside encounter cards ───────────────────────────────────────

function statChip(icon, color, count, label) {
  return `
  <span class="enc-stat-chip">
    <i class="fas ${icon}" style="color:${color};"></i>
    <strong>${count}</strong> ${label}
  </span>`;
}

function encDetail(icon, color, label, val) {
  if (!val) return "";
  return `
  <div class="enc-detail-item">
    <i class="fas ${icon}" style="color:${color};font-size:0.7rem;margin-top:0.1rem;flex-shrink:0;"></i>
    <div>
      <div class="enc-detail-label">${label}</div>
      <div class="enc-detail-val">${esc(val)}</div>
    </div>
  </div>`;
}

// ── Encounter section renderers ───────────────────────────────────────────────

function encSectionDiagnoses(items) {
  const header = encSecHeader("fa-stethoscope", "#fb7185", "Diagnoses", items?.length || 0);
  const body   = items?.length
    ? items.map((c, i) => `
      <div class="enc-data-row">
        <span class="enc-row-num">${i + 1}</span>
        <div class="min-w-0 flex-1">
          <span class="enc-row-name">${esc(c.name)}</span>
          ${c.code ? `<span class="enc-row-meta">${esc(c.codeSystem)} · ${esc(c.code)}</span>` : ""}
        </div>
        <span class="shrink-0 ${c.status === "active" ? "badge-rose" : "badge-inactive"}">${esc(c.status)}</span>
      </div>`).join("")
    : encEmpty("No diagnoses recorded for this encounter");
  return `<div class="enc-section">${header}<div class="enc-section-body">${body}</div></div>`;
}

function encSectionMedications(items) {
  const header = encSecHeader("fa-pills", "#c084fc", "Medications", items?.length || 0);
  const body   = items?.length
    ? items.map(m => `
      <div class="enc-data-row">
        <i class="fas fa-capsules enc-row-icon" style="color:#c084fc;"></i>
        <div class="min-w-0 flex-1">
          <span class="enc-row-name">${esc(m.name)}</span>
          ${(m.dose || m.route)
            ? `<span class="enc-row-meta">${[m.dose, m.route].filter(Boolean).join(" · ")}</span>`
            : ""}
          ${m.start ? `<span class="enc-row-meta">${m.start}${m.end ? " → " + m.end : ""}</span>` : ""}
        </div>
        <span class="shrink-0 ${m.status === "completed" ? "badge-completed" : "badge-inactive"}">${esc(m.status)}</span>
      </div>`).join("")
    : encEmpty("No medications recorded for this encounter");
  return `<div class="enc-section">${header}<div class="enc-section-body">${body}</div></div>`;
}

function encSectionProcedures(items) {
  const header = encSecHeader("fa-syringe", "#4ade80", "Procedures", items?.length || 0);
  const body   = items?.length
    ? items.map(p => `
      <div class="enc-data-row">
        <i class="fas fa-syringe enc-row-icon" style="color:#4ade80;"></i>
        <div class="min-w-0 flex-1">
          <span class="enc-row-name">${esc(p.name)}</span>
          ${p.time ? `<span class="enc-row-meta">${esc(p.time)}</span>` : ""}
        </div>
        <span class="shrink-0 badge-inactive">${esc(p.status)}</span>
      </div>`).join("")
    : encEmpty("No procedures recorded for this encounter");
  return `<div class="enc-section">${header}<div class="enc-section-body">${body}</div></div>`;
}

function encSectionReports(items) {
  const header = encSecHeader("fa-vial-circle-check", "#38bdf8", "Diagnostic Reports", items?.length || 0);
  const body   = items?.length
    ? items.map(r => `
      <div class="enc-data-row">
        <i class="fas fa-vial enc-row-icon" style="color:#38bdf8;"></i>
        <div class="min-w-0 flex-1">
          <span class="enc-row-name">${esc(r.name)}</span>
          ${(r.category || r.time)
            ? `<span class="enc-row-meta">${[r.category, r.time].filter(Boolean).join(" · ")}</span>`
            : ""}
        </div>
        <span class="shrink-0 badge-sky">${esc(r.status)}</span>
      </div>`).join("")
    : encEmpty("No diagnostic reports for this encounter");
  return `<div class="enc-section">${header}<div class="enc-section-body">${body}</div></div>`;
}

function encSectionVitals(items) {
  const header = encSecHeader("fa-heart-pulse", "#f87171", "Vital Signs", items?.length || 0);
  const body   = items?.length
    ? `<div class="enc-vitals-grid">
        ${items.map(v => {
          const val   = typeof v.value === "number" ? v.value.toFixed(1) : v.value;
          const color = v.status === "abnormal" ? "#f85149" : "#79c0ff";
          const nr    = v.normalRange;
          return `
          <div class="enc-vital-chip ${v.status === "abnormal" ? "enc-vital-abnormal" : ""}">
            <i class="fas ${v.icon}" style="color:${color};font-size:0.875rem;flex-shrink:0;"></i>
            <div class="min-w-0">
              <div class="enc-vital-name">${esc(v.name)}</div>
              <div class="enc-vital-val" style="color:${color};">
                ${esc(String(val))} <span class="enc-vital-unit">${esc(v.unit)}</span>
              </div>
              ${nr ? `<div class="enc-vital-range">Normal: ${nr[0]}–${nr[1]}</div>` : ""}
              ${v.time ? `<div class="enc-vital-time">${v.time}</div>` : ""}
            </div>
          </div>`;
        }).join("")}
      </div>`
    : encEmpty("No vital signs recorded for this encounter");
  return `<div class="enc-section enc-section-full">${header}${body}</div>`;
}

function encSectionLabs(items) {
  const flagIcon = { H: "↑", L: "↓", HH: "↑↑", LL: "↓↓", A: "!" };
  const nAbn     = (items || []).filter(l => l.flag && l.flag !== "N").length;
  const header   = encSecHeader("fa-flask-vial", "#818cf8", "Lab Results", items?.length || 0,
    nAbn > 0 ? `<span class="enc-lab-abn-chip">${nAbn} abnormal</span>` : "");
  const body     = items?.length
    ? `<div class="enc-labs-table-wrap">
        <table class="enc-labs-table">
          <thead>
            <tr>
              <th style="text-align:left;">Test</th>
              <th style="text-align:right;">Result</th>
              <th style="text-align:center;">Flag</th>
              <th style="text-align:center;">Ref Range</th>
              <th style="text-align:left;">Date</th>
            </tr>
          </thead>
          <tbody>
            ${items.map(l => {
              const fc  = l.flag ? `flag-${l.flag}` : "";
              const ico = flagIcon[l.flag] || l.flag || "—";
              const val = typeof l.value === "number" ? l.value.toFixed(2) : (l.value ?? "—");
              const ref = (l.refLow != null && l.refHigh != null) ? `${l.refLow}–${l.refHigh}` : "—";
              const rowCls = (l.flag && l.flag !== "N") ? "enc-lab-row enc-lab-row-flagged" : "enc-lab-row";
              return `
              <tr class="${rowCls}">
                <td style="color:#cdd9e5;font-weight:500;">${esc(l.name)}</td>
                <td style="text-align:right;" class="font-mono ${fc}">
                  ${esc(String(val))}
                  <span style="color:#484f58;font-size:0.68rem;margin-left:0.2rem;">${esc(l.unit)}</span>
                </td>
                <td style="text-align:center;" class="${fc}">${ico}</td>
                <td style="text-align:center;color:#484f58;font-size:0.7rem;font-family:monospace;">${ref}</td>
                <td style="color:#6e7681;font-size:0.72rem;">${l.time || "—"}</td>
              </tr>`;
            }).join("")}
          </tbody>
        </table>
      </div>`
    : encEmpty("No lab results recorded for this encounter");
  return `<div class="enc-section enc-section-full">${header}${body}</div>`;
}

// ── Chief complaint banner ────────────────────────────────────────────────────

function encChiefComplaintBox(chiefComplaint, providers) {
  if (!chiefComplaint && (!providers || !providers.length)) return "";
  const providerHtml = (providers || []).map(p => `
    <span class="enc-provider-chip">
      <i class="fas fa-user-doctor" style="color:#d29922;"></i>
      ${esc(p.name || p.providerId || "Unknown Provider")}
    </span>`).join("");
  return `
  <div class="enc-chief-box">
    <div class="enc-chief-top">
      <i class="fas fa-circle-exclamation enc-chief-icon"></i>
      <div class="enc-chief-label">Chief Complaint &amp; Reason for Visit</div>
    </div>
    <div class="enc-chief-text">${esc(chiefComplaint || "Not documented")}</div>
    ${providerHtml ? `<div class="enc-chief-providers">${providerHtml}</div>` : ""}
  </div>`;
}

// ── Synthesized clinical note ─────────────────────────────────────────────────

function encClinicalNote(enc, ed) {
  const conditions  = ed.conditions        || [];
  const medications = ed.medications       || [];
  const labs        = ed.labs              || [];
  const procedures  = ed.procedures        || [];
  const vitals      = ed.vitals            || [];
  const reports     = ed.diagnosticReports || [];
  const hasRealNotes = (ed.notes?.length || 0) > 0;

  const abnormalLabs = labs.filter(l => l.flag && l.flag !== "N");
  const criticalLabs = labs.filter(l => l.flag === "HH" || l.flag === "LL");
  const activeMeds   = medications.filter(m => m.status !== "stopped");
  const abnVitals    = vitals.filter(v => v.status === "abnormal");

  const dxLines = conditions.map((c, i) =>
    `<span class="enc-note-dx-item">${i + 1}. ${esc(c.name)}${c.code ? ` <span class="enc-note-code">(${esc(c.code)})</span>` : ""}</span>`
  ).join("");

  const medLines = activeMeds.map(m =>
    `<span class="enc-note-med-item">
      <i class="fas fa-circle" style="color:#c084fc;font-size:0.45rem;margin-top:0.35rem;flex-shrink:0;"></i>
      ${esc(m.name)}${m.dose ? ` — <span style="color:#6e7681;">${esc(m.dose)}</span>` : ""}
     </span>`
  ).join("");

  let labSummary = `${labs.length} total`;
  if (abnormalLabs.length) labSummary += `, <span style="color:#f85149;font-weight:600;">${abnormalLabs.length} abnormal</span>`;
  if (criticalLabs.length) {
    const critNames = criticalLabs.map(l => esc(l.name)).join(", ");
    labSummary += ` — critical: <span style="color:#f85149;">${critNames}</span>`;
  }

  const procLines = procedures.map(p =>
    `<span class="enc-note-proc-item">
      <i class="fas fa-circle" style="color:#4ade80;font-size:0.45rem;margin-top:0.35rem;flex-shrink:0;"></i>
      ${esc(p.name)}
     </span>`
  ).join("");

  const rptLines = reports.map(r =>
    `<span class="enc-note-rpt-item">
      <i class="fas fa-circle" style="color:#38bdf8;font-size:0.45rem;margin-top:0.35rem;flex-shrink:0;"></i>
      <span>
        <span style="color:#cdd9e5;">${esc(r.name)}</span>
        ${r.category ? `<span style="color:#484f58;font-size:0.7rem;margin-left:0.3rem;">(${esc(r.category)})</span>` : ""}
        ${r.time     ? `<span style="color:#484f58;font-size:0.7rem;margin-left:0.3rem;">· ${esc(r.time)}</span>` : ""}
        <span class="enc-note-rpt-status">${esc(r.status)}</span>
      </span>
     </span>`
  ).join("");

  return `
  <div class="enc-note-card">
    <div class="enc-note-header">
      <i class="fas fa-file-medical" style="color:#58a6ff;"></i>
      <span>Clinical Summary</span>
      ${hasRealNotes
        ? `<span class="enc-note-generated-tag" style="background:rgba(52,211,153,0.12);color:#34d399;border-color:#34d39933;">
             <i class="fas fa-circle-check" style="font-size:0.6rem;"></i> Real notes attached — see below
           </span>`
        : `<span class="enc-note-generated-tag">Synthesized from FHIR · No free-text notes in bundle</span>`
      }
    </div>
    <div class="enc-note-body">

      ${conditions.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-stethoscope" style="color:#fb7185;"></i> Diagnoses (${conditions.length})</div>
        <div class="enc-note-dx-list">${dxLines}</div>
      </div>` : ""}

      ${activeMeds.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-pills" style="color:#c084fc;"></i> Active Medications (${activeMeds.length})</div>
        <div class="enc-note-med-list">${medLines}</div>
      </div>` : ""}

      ${labs.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-flask-vial" style="color:#818cf8;"></i> Lab Findings</div>
        <div class="enc-note-text">${labSummary}</div>
      </div>` : ""}

      ${reports.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-vial-circle-check" style="color:#38bdf8;"></i> Microbiology / Reports (${reports.length})</div>
        <div class="enc-note-rpt-list">${rptLines}</div>
      </div>` : ""}

      ${procedures.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-syringe" style="color:#4ade80;"></i> Procedures (${procedures.length})</div>
        <div class="enc-note-proc-list">${procLines}</div>
      </div>` : ""}

      ${vitals.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-heart-pulse" style="color:#f87171;"></i> Vitals</div>
        <div class="enc-note-text">${vitals.length} recorded${abnVitals.length ? `, <span style="color:#f85149;">${abnVitals.length} abnormal</span>` : ", all within normal range"}</div>
      </div>` : ""}

      ${enc.dischDisp ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-door-open" style="color:#6e7681;"></i> Disposition</div>
        <div class="enc-note-text">${esc(enc.dischDisp)}${enc.los != null ? ` after ${enc.los} day${enc.los !== 1 ? "s" : ""} (${esc(enc.start)} – ${esc(enc.end)})` : ""}</div>
      </div>` : ""}

    </div>
  </div>`;
}

// ── Shared enc section helpers ────────────────────────────────────────────────

function encSecHeader(icon, color, title, count, extra = "") {
  return `
  <div class="enc-section-header">
    <i class="fas ${icon}" style="color:${color};"></i>
    <span style="color:#cdd9e5;">${title}</span>
    <span class="enc-section-badge" style="color:${color};background:${color}1a;border-color:${color}33;">${count}</span>
    ${extra}
  </div>`;
}

function encEmpty(msg) {
  return `
  <div class="enc-empty-state">
    <i class="fas fa-circle-xmark" style="color:#30363d;font-size:1.1rem;"></i>
    <span>${msg}</span>
  </div>`;
}

function toggleEnc(header) {
  const card    = header.parentElement;
  const body    = header.nextElementSibling;
  const chevron = header.querySelector(".enc-chevron");
  const open    = !body.classList.contains("hidden");
  body.classList.toggle("hidden", open);
  chevron.style.transform = open ? "" : "rotate(180deg)";
  // Lazy-render per-encounter charts on first open
  if (!open && body.dataset.chartsInit !== "1") {
    body.dataset.chartsInit = "1";
    const idx = parseInt(card.dataset.encIdx, 10);
    if (!isNaN(idx)) _renderEncCharts(idx);
  }
}

// ── Clinical Notes tab ────────────────────────────────────────────────────────

function renderNotes(notes) {
  const discharge = notes.filter(n => n.category === "discharge");
  const radiology = notes.filter(n => n.category === "radiology");
  const other     = notes.filter(n => n.category !== "discharge" && n.category !== "radiology");

  $("notesTotalBadge").textContent = `${notes.length} note${notes.length !== 1 ? "s" : ""}`;
  $("dischargeCount").textContent  = discharge.length;
  $("radiologyCount").textContent  = radiology.length;
  $("otherNotesCount").textContent = other.length;

  renderNoteGroup("dischargeContent",  "dischargeEmpty",  discharge);
  renderNoteGroup("radiologyContent",  "radiologyEmpty",  radiology);
  renderNoteGroup("otherNotesContent", "otherNotesEmpty", other);
}

function renderNoteGroup(contentId, emptyId, notes) {
  const el = $(contentId);
  if (!notes.length) {
    $(emptyId).classList.remove("hidden");
    return;
  }
  el.innerHTML = notes.map((n, idx) => noteCard(n, `${contentId}-${idx}`)).join("");
}

function noteCard(n, uid) {
  const preview  = n.preview ? esc(n.preview) + (n.text.length > 300 ? "…" : "") : "<em style='color:#484f58;'>No content</em>";
  const hasMore  = n.text.length > 300;
  const fullText = hasMore ? esc(n.text) : "";
  return `
  <div class="note-card" data-note-text="${esc((n.typeDisplay + " " + n.text).toLowerCase())}">
    <div class="note-card-header" onclick="toggleNote(this)">
      <div class="flex items-center gap-2 min-w-0 flex-1">
        <i class="fas fa-file-lines shrink-0" style="color:#34d399;font-size:0.85rem;"></i>
        <span class="font-medium truncate" style="color:#cdd9e5;">${esc(n.typeDisplay)}</span>
        ${n.date ? `<span class="note-date-chip">${esc(n.date)}</span>` : ""}
      </div>
      <i class="fas fa-chevron-down note-chevron shrink-0 text-xs" style="color:#484f58;"></i>
    </div>
    <div class="note-body hidden">
      <p class="note-preview-text">${preview}</p>
      ${hasMore ? `
      <div class="note-full hidden" id="noteFull-${uid}">
        <pre class="note-full-text">${fullText}</pre>
      </div>
      <button class="note-expand-btn" onclick="toggleFullNote(this, 'noteFull-${uid}')">
        <i class="fas fa-expand-alt" style="font-size:0.7rem;"></i> Show full text
      </button>` : ""}
    </div>
  </div>`;
}

function toggleNote(header) {
  const body    = header.nextElementSibling;
  const chevron = header.querySelector(".note-chevron");
  const open    = !body.classList.contains("hidden");
  body.classList.toggle("hidden", open);
  chevron.style.transform = open ? "" : "rotate(180deg)";
}

function toggleFullNote(btn, id) {
  const el   = $(id);
  const open = !el.classList.contains("hidden");
  el.classList.toggle("hidden", open);
  btn.innerHTML = open
    ? `<i class="fas fa-expand-alt" style="font-size:0.7rem;"></i> Show full text`
    : `<i class="fas fa-compress-alt" style="font-size:0.7rem;"></i> Collapse`;
}

function filterNotes(query) {
  const q = query.toLowerCase().trim();
  document.querySelectorAll(".note-card").forEach(card => {
    const text = card.dataset.noteText || "";
    card.style.display = !q || text.includes(q) ? "" : "none";
  });
}

// ── Notes section inside encounter card ───────────────────────────────────────

function encSectionNotes(notes) {
  const header = encSecHeader("fa-file-medical", "#34d399", "Clinical Notes", notes.length);
  const body   = `
    <div class="divide-y divide-gray-800/60">
      ${notes.map((n, i) => {
        const preview = n.preview
          ? esc(n.preview) + (n.text.length > 300 ? "…" : "")
          : "<em style='color:#484f58;'>No content</em>";
        const uid     = `encNote-${i}-${n.id || i}`;
        const hasMore = n.text.length > 300;
        return `
        <div class="enc-note-item">
          <div class="enc-note-item-header" onclick="toggleNote(this)">
            <i class="fas fa-file-lines shrink-0" style="color:#34d399;font-size:0.8rem;"></i>
            <span class="font-medium" style="color:#cdd9e5;font-size:0.85rem;">${esc(n.typeDisplay)}</span>
            ${n.date ? `<span class="note-date-chip">${esc(n.date)}</span>` : ""}
            <i class="fas fa-chevron-down note-chevron ml-auto shrink-0 text-xs" style="color:#484f58;"></i>
          </div>
          <div class="enc-note-item-body hidden">
            <p class="note-preview-text">${preview}</p>
            ${hasMore ? `
            <div class="note-full hidden" id="${uid}">
              <pre class="note-full-text">${esc(n.text)}</pre>
            </div>
            <button class="note-expand-btn" onclick="toggleFullNote(this,'${uid}')">
              <i class="fas fa-expand-alt" style="font-size:0.7rem;"></i> Show full text
            </button>` : ""}
          </div>
        </div>`;
      }).join("")}
    </div>`;
  return `<div class="enc-section enc-section-full">${header}${body}</div>`;
}

// ── Per-encounter chart renderer (lazy — called on first card expand) ─────────
function _renderEncCharts(idx) {
  const enc = _encDataMap[idx];
  if (!enc) return;
  const ed     = enc.encounterData || {};
  const labs   = ed.labs        || [];
  const vitals = ed.vitals      || [];
  const conds  = ed.conditions  || [];

  const _FC = { Normal: "#3fb950", H: "#ffa657", HH: "#f85149", L: "#79c0ff", LL: "#58a6ff", A: "#ff7b72" };
  const _flagKey = f => (!f || f === "N") ? "Normal" : f;

  // Deduplicate vitals — latest observation per vital name
  const vitalMap = {};
  vitals.forEach(v => { if (!vitalMap[v.name] || v.raw > vitalMap[v.name].raw) vitalMap[v.name] = v; });
  const dVitals = Object.values(vitalMap).sort((a, b) => a.name.localeCompare(b.name));

  // Deduplicate labs — latest per test name, numeric only
  const labMap = {};
  labs.forEach(l => { if (!labMap[l.name] || l.rawDt > labMap[l.name].rawDt) labMap[l.name] = l; });
  const allDedupLabs = Object.values(labMap);

  // Sort labs: HH/LL → H/L → A → others, then alpha; cap at 40
  const _sev = f => ({ HH: 0, LL: 0, H: 1, L: 1, A: 2 }[f] ?? ((!f || f === "N") ? 4 : 3));
  const dLabs = allDedupLabs
    .filter(l => typeof l.value === "number")
    .sort((a, b) => _sev(a.flag) - _sev(b.flag) || a.name.localeCompare(b.name))
    .slice(0, 40);

  // ── Vitals horizontal bar ──────────────────────────────────────────────────
  if (dVitals.length) {
    _mkBar(`encChart_vitals_${idx}`, dVitals.map(v => v.name), [{
      data: dVitals.map(v => typeof v.value === "number" ? +v.value.toFixed(1) : parseFloat(v.value) || 0),
      backgroundColor: dVitals.map(v => (v.status === "abnormal" ? "#f85149" : "#58a6ff") + "44"),
      borderColor:     dVitals.map(v => v.status === "abnormal" ? "#f85149" : "#58a6ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      horizontal: true,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => {
          const v = dVitals[ctx.dataIndex];
          const nr = v.normalRange ? `  normal: ${v.normalRange[0]}–${v.normalRange[1]}` : "";
          return ` ${ctx.raw} ${v.unit}${nr}  (${v.status})`;
        }}},
      },
    });
  }

  // ── Lab flag distribution bar ──────────────────────────────────────────────
  if (allDedupLabs.length) {
    const flagTally = {};
    allDedupLabs.forEach(l => { const k = _flagKey(l.flag); flagTally[k] = (flagTally[k] || 0) + 1; });
    const order = ["Normal","H","HH","L","LL","A"];
    const present = order.filter(f => flagTally[f]);
    _mkBar(`encChart_flags_${idx}`, present, [{
      data: present.map(f => flagTally[f]),
      backgroundColor: present.map(f => (_FC[f] || "#58a6ff") + "44"),
      borderColor:     present.map(f => _FC[f] || "#58a6ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], { plugins: { legend: { display: false } } });
  }

  // ── Lab values horizontal bar (colour = flag severity) ────────────────────
  if (dLabs.length) {
    _mkBar(`encChart_labs_${idx}`, dLabs.map(l => l.name.slice(0, 28)), [{
      data: dLabs.map(l => +l.value.toFixed(2)),
      backgroundColor: dLabs.map(l => (_FC[_flagKey(l.flag)] || "#3fb950") + "44"),
      borderColor:     dLabs.map(l => _FC[_flagKey(l.flag)] || "#3fb950"),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      horizontal: true,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => {
          const l = dLabs[ctx.dataIndex];
          const ref = (l.refLow != null && l.refHigh != null) ? `  ref: ${l.refLow}–${l.refHigh}` : "";
          return ` ${ctx.raw} ${l.unit}  [${l.flag || "normal"}]${ref}`;
        }}},
      },
    });
  }

  // ── Diagnoses horizontal bar ───────────────────────────────────────────────
  if (conds.length > 1) {
    const dxColors = { active: "#f85149", resolved: "#3fb950", inactive: "#6e7681" };
    _mkBar(`encChart_dx_${idx}`, conds.map(c => c.name.slice(0, 32)), [{
      data: conds.map(() => 1),
      backgroundColor: conds.map(c => (dxColors[c.status] || "#fb7185") + "44"),
      borderColor:     conds.map(c => dxColors[c.status] || "#fb7185"),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      horizontal: true,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => {
          const c = conds[ctx.dataIndex];
          return ` ${c.codeSystem || ""} ${c.code || ""}  status: ${c.status}`;
        }}},
      },
    });
  }

  // ── Vitals trend — normalised line chart (all readings over time) ──────────
  {
    const vByName = {};
    vitals.forEach(v => {
      if (v.normalRange) (vByName[v.name] = vByName[v.name] || []).push(v);
    });
    const trendEntries = Object.entries(vByName).filter(([, rs]) => rs.length >= 2);
    if (trendEntries.length) {
      const encStartMs = Date.parse((enc.start || "").replace(" ", "T"));
      const palette = ["#58a6ff","#f87171","#3fb950","#ffa657","#c084fc","#79c0ff","#f85149","#4ade80","#d2a8ff"];
      const datasets = trendEntries.map(([name, readings], i) => {
        const [lo, hi] = readings[0].normalRange;
        const range = hi - lo || 1;
        const sorted = readings.slice().sort((a, b) => a.raw < b.raw ? -1 : 1);
        return {
          label: name,
          data: sorted.map(v => ({
            x: +((Date.parse(v.raw) - encStartMs) / 60000).toFixed(0),
            y: +((v.value - lo) / range * 100).toFixed(1),
          })),
          borderColor: palette[i % palette.length],
          backgroundColor: "transparent",
          borderWidth: 2, pointRadius: 3, tension: 0.35, fill: false,
        };
      });
      _destroyChart(`encChart_vtrend_${idx}`);
      const cv = document.getElementById(`encChart_vtrend_${idx}`);
      if (cv) {
        _charts[`encChart_vtrend_${idx}`] = new Chart(cv, {
          type: "line",
          data: { datasets },
          options: {
            responsive: true, maintainAspectRatio: false,
            plugins: {
              legend: { position: "bottom", labels: { color: "#8b949e", font: { size: 9 }, padding: 6, boxWidth: 10 } },
              tooltip: { callbacks: { label: ctx =>
                ` ${ctx.dataset.label}: ${ctx.parsed.y}% of range  at +${ctx.parsed.x} min` } },
            },
            scales: {
              x: { type: "linear", ticks: { color: _TC, font: { size: 9 }, callback: v => v + "m" }, grid: { color: _GC },
                   title: { display: true, text: "minutes from admission", color: _TC, font: { size: 9 } } },
              y: { ticks: { color: _TC, font: { size: 9 }, callback: v => v + "%" }, grid: { color: _GC },
                   title: { display: true, text: "% of normal range (0–100 = in range)", color: _TC, font: { size: 9 } } },
            },
          },
        });
      }
    }
  }

  // ── Lab vs reference range — normalised horizontal bar ────────────────────
  {
    const labMap2 = {};
    labs.forEach(l => { if (!labMap2[l.name] || l.rawDt > labMap2[l.name].rawDt) labMap2[l.name] = l; });
    const refLabs = Object.values(labMap2)
      .filter(l => l.refLow != null && l.refHigh != null && typeof l.value === "number")
      .sort((a, b) => _sev(a.flag) - _sev(b.flag) || a.name.localeCompare(b.name))
      .slice(0, 30);
    if (refLabs.length) {
      const pcts = refLabs.map(l => {
        const range = l.refHigh - l.refLow || 1;
        return +((l.value - l.refLow) / range * 100).toFixed(1);
      });
      _mkBar(`encChart_refnorm_${idx}`, refLabs.map(l => l.name.slice(0, 28)), [{
        data: pcts,
        backgroundColor: pcts.map(p => (p < 0 || p > 100) ? "#f8514944" : "#3fb95044"),
        borderColor:     pcts.map(p => (p < 0 || p > 100) ? "#f85149"   : "#3fb950"),
        borderWidth: 1.5, borderRadius: 3,
      }], {
        horizontal: true,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: ctx => {
            const l = refLabs[ctx.dataIndex];
            const s = ctx.raw < 0 ? "BELOW" : ctx.raw > 100 ? "ABOVE" : "in";
            return ` ${ctx.raw}% (${s} range)  ${l.value} ${l.unit}  ref: ${l.refLow}–${l.refHigh}`;
          }}},
        },
      });
    }
  }

  // Inject download buttons into this encounter's chart cards
  setTimeout(_injectDownloadBtns, 0);
}

// ── Chart download helpers ────────────────────────────────────────────────────
// Render a chart canvas onto a dark background with an optional title bar, so
// the exported PNG isn't transparent and carries its human-readable label.
function _renderLabeledCanvas(canvas, label) {
  const dpr     = window.devicePixelRatio || 1;
  const pad     = Math.round(20 * dpr);
  const headerH = label ? Math.round(52 * dpr) : 0;
  const off = document.createElement('canvas');
  off.width  = canvas.width  + pad * 2;
  off.height = canvas.height + headerH + pad;
  const ctx  = off.getContext('2d');
  ctx.fillStyle = '#161b22';
  ctx.fillRect(0, 0, off.width, off.height);
  if (label) {
    ctx.fillStyle = '#1e4976';
    ctx.fillRect(0, 0, off.width, headerH);
    ctx.fillStyle = '#ffffff';
    ctx.font = `600 ${Math.round(22 * dpr)}px -apple-system, "Segoe UI", Roboto, sans-serif`;
    ctx.textBaseline = 'middle';
    ctx.fillText(label, pad, headerH / 2);
  }
  ctx.drawImage(canvas, pad, headerH);
  return off;
}

function _downloadCanvas(canvas, filename, label) {
  const off = _renderLabeledCanvas(canvas, label);
  const a = document.createElement('a');
  a.href     = off.toDataURL('image/png');
  a.download = (filename || 'chart').replace(/\W+/g, '_') + '.png';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}

// Read the human-readable label from a chart card's header.
function _cardLabel(card) {
  const span = card.querySelector('.card-header span');
  return span ? span.textContent.trim() : '';
}

// Bundle every population chart into a single ZIP of labelled PNGs.
async function downloadAllPopCharts() {
  const btn   = $("popDownloadAllBtn");
  const lbl   = $("popDownloadAllLabel");
  if (typeof JSZip === 'undefined') {
    alert('Could not load the ZIP library. Please check your connection and retry.');
    return;
  }
  const cards = Array.from(document.querySelectorAll('#populationPanel section.card'))
    .map(card => ({ canvas: card.querySelector('canvas'), label: _cardLabel(card) }))
    .filter(c => c.canvas && c.label);
  if (!cards.length) return;

  if (btn) btn.disabled = true;
  const origText = lbl ? lbl.textContent : '';

  try {
    const zip  = new JSZip();
    const seen = {};
    for (let i = 0; i < cards.length; i++) {
      const { canvas, label } = cards[i];
      if (lbl) lbl.textContent = `Preparing ${i + 1}/${cards.length}…`;
      let name = label.replace(/[^\w \-]+/g, '').trim().replace(/\s+/g, '_') || `chart_${i + 1}`;
      if (seen[name]) name += `_${seen[name]++}`; else seen[name] = 1;
      const off  = _renderLabeledCanvas(canvas, label);
      const blob = await new Promise(res => off.toBlob(res, 'image/png'));
      zip.file(`${String(i + 1).padStart(2, '0')}_${name}.png`, blob);
    }
    if (lbl) lbl.textContent = 'Zipping…';
    const content = await zip.generateAsync({ type: 'blob' });
    const a = document.createElement('a');
    a.href     = URL.createObjectURL(content);
    a.download = 'population_charts.zip';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(a.href);
  } catch (e) {
    console.error('Chart export failed', e);
    alert('Failed to export charts. See console for details.');
  } finally {
    if (lbl) lbl.textContent = origText;
    if (btn) btn.disabled = false;
  }
}

function _injectDownloadBtns() {
  // Analytics tab + Population panel: button goes into .card-header
  document.querySelectorAll('#tab-analytics section.card, #populationPanel section.card').forEach(card => {
    if (card.querySelector('.chart-dl-btn')) return;
    const canvas = card.querySelector('canvas');
    const header = card.querySelector('.card-header');
    if (!canvas || !header) return;
    const btn = document.createElement('button');
    btn.className = 'chart-dl-btn';
    btn.title     = 'Download chart as PNG';
    btn.innerHTML = '<i class="fas fa-download"></i>';
    const label = _cardLabel(card);
    btn.onclick   = e => { e.stopPropagation(); _downloadCanvas(canvas, label || canvas.id, label); };
    header.appendChild(btn);
  });

  // Per-encounter charts: button goes into .enc-chart-label
  document.querySelectorAll('.enc-chart-card').forEach(card => {
    if (card.querySelector('.chart-dl-btn')) return;
    const canvas = card.querySelector('canvas');
    const label  = card.querySelector('.enc-chart-label');
    if (!canvas || !label) return;
    const btn = document.createElement('button');
    btn.className      = 'chart-dl-btn enc-dl-btn';
    btn.title          = 'Download chart as PNG';
    btn.innerHTML      = '<i class="fas fa-download"></i>';
    btn.onclick        = e => { e.stopPropagation(); _downloadCanvas(canvas, canvas.id); };
    label.appendChild(btn);
  });
}

// ── Charts — helpers ─────────────────────────────────────────────────────────
const _GC = '#21262d';
const _TC = '#6e7681';

// ── Axis label registry ────────────────────────────────────────────────────────
// [xAxisLabel, yAxisLabel]
// For HORIZONTAL bar charts Chart.js puts categories on the y-axis (left) and
// values on the x-axis (bottom).  Adding a rotated y-title to a horizontal chart
// shifts the plot area and clips category labels, so horizontal charts only
// receive an x-title (value axis).  Pass null for y to skip it explicitly.
const _CHART_LABELS = {
  // ── Per-patient Analytics ────────────────────────────────────────────────────
  chartA_los:         ['LOS (days)',               null],               // hbar
  chartA_types:       ['Encounter Type',           'Count'],
  chartA_records:     ['Encounter #',             'Records'],
  chartA_admit:       ['Count',                    null],               // hbar
  chartA_status:      ['Status',                  'Encounters'],
  chartA_serviceType: ['Count',                    null],               // hbar
  chartA_location:    ['Count',                    null],               // hbar
  chartP_serviceType: ['Count',                    null],               // hbar
  chartB_perEnc:      ['Encounter #',             'Diagnoses'],
  chartB_icd:         ['ICD Code System',          'Conditions'],
  chartB_status:      ['Diagnosis Status',         'Conditions'],
  chartB_top:         ['Occurrences',              null],               // hbar
  chartC_flags:       ['Flag Type',               'Lab Results'],
  chartC_perEnc:      ['Encounter #',             'Lab Results'],
  chartC_abnormal:    ['Count',                    null],               // hbar
  chartC_allLabs:     ['Measured Value',            null],              // hbar
  chartD_vitals:      ['Measured Value',            null],              // hbar
  chartD_vitalStatus: ['Status',                  'Vital Readings'],
  chartE_medStatus:   ['Medication Status',        'Medications'],
  chartE_procsPerEnc: ['Encounter #',             'Procedures'],
  chartE_medRoutes:   ['Count',                    null],               // hbar
  chartE_topMeds:     ['Occurrences',              null],               // hbar
  chartE_topProcs:    ['Occurrences',              null],               // hbar
  chartF_hour:        ['Hour of Day',              'Encounters'],
  chartF_dow:         ['Day of Week',             'Encounters'],
  chartG_crossEnc:    ['Vital Sign',              'Measured Value'],
  chartG_vitalStatus: ['Encounter',               'Vital Readings'],
  chartH_refRange:    ['Encounter',               'Lab Results'],
  chartH_abnRate:     ['Encounter',               'Abnormal Rate (%)'],
  chartI_dischDisp:   ['Count',                    null],               // hbar
  chartI_noteTypes:   ['Count',                    null],               // hbar
  chartI_notesPerEnc: ['Encounter',               'Count'],
  // ── Population Charts ────────────────────────────────────────────────────────
  chartP_ageHist:        ['Age Group (decade)',          'Patients'],
  chartP_race:           ['Patients',                     null],        // hbar
  chartP_anchorYear:     ['Anchor Year Group',            'Patients'],
  chartP_encType:        ['Encounter Type',               'Encounters'],
  chartP_losHist:        ['LOS (days)',                  'Encounters'],
  chartP_encPerPt:       ['Encounters per Patient',       'Patients'],
  chartP_admitSrc:       ['Encounters',                   null],        // hbar
  chartP_dischDisp:      ['Encounters',                   null],        // hbar
  chartP_avgLosByType:   ['Encounter Type',               'Avg LOS (days)'],
  chartP_icuPerPt:       ['ICU Stays per Patient',        'Patients'],
  chartP_topDx:          ['Occurrences',                  null],        // hbar
  chartP_condPerPt:      ['Conditions per Patient',       'Patients'],
  chartP_dxStatus:       ['Diagnosis Status',             'Conditions'],
  chartP_icdAlpha:       ['ICD Code Initial Letter (A–Z)', 'Occurrences'],
  chartP_labFlags:       ['Flag Type',                   'Lab Results'],
  chartP_labPerPt:       ['Labs per Patient',             'Patients'],
  chartP_abnLabRate:     ['Abnormal Rate Bucket',         'Patients'],
  chartP_topLabs:        ['Occurrences',                  null],        // hbar
  chartP_topAbnLabs:     ['Abnormal Occurrences',         null],        // hbar
  chartP_refCompliance:  ['Compliance Category',          'Lab Results'],
  chartP_critLabs:       ['Abnormal Rate (%)',             null],        // hbar — custom chart, label set inline
  chartP_topMeds:        ['Occurrences',                  null],        // hbar
  chartP_topProcs:       ['Occurrences',                  null],        // hbar
  chartP_medRoute:       ['Dispenses',                    null],        // hbar
  chartP_medStatus:      ['Medication Status',            'Medications'],
  chartP_medPerPt:       ['Medications per Patient',      'Patients'],
  chartP_procsPerPt:     ['Procedures per Patient',       'Patients'],
  chartP_medDispStatus:  ['Medications per Encounter',     'Encounters'],
  chartP_topVitals:      ['Occurrences',                  null],        // hbar
  chartP_vitalStatus:    ['Status',                      'Vital Readings'],
  chartP_noteTypes:      ['Notes',                        null],        // hbar
  chartP_rptPerPt:       ['Reports per Patient',          'Patients'],
  chartP_vitPerPt:       ['Vitals per Patient',           'Patients'],
  chartP_notePerPt:      ['Notes per Patient',            'Patients'],
  chartP_genderVsEnc:    ['Gender',                      'Avg Encounters / Patient'],
  chartP_ageVsCond:      ['Age Group',                   'Avg Conditions / Patient'],
  chartP_ageVsLos:       ['Age Group',                   'Avg LOS (days)'],
  chartP_genderVsAbnLab: ['Gender',                      'Avg Abnormal Lab %'],
  chartP_raceVsAbnLab:   ['Avg Abnormal %',               null],        // hbar
  chartP_encTypeVsProcs: ['Encounter Type',               'Avg Procedures / Enc'],
  chartP_encTypeVsMeds:  ['Encounter Type',               'Avg Medications / Enc'],
  chartP_encTypeVsLabs:  ['Encounter Type',               'Avg Lab Tests / Enc'],
};

function _encLOS(enc) {
  if (enc.los != null) return enc.los;
  if (!enc.start || !enc.end) return null;
  const ms = Date.parse(enc.end.replace(' ', 'T')) - Date.parse(enc.start.replace(' ', 'T'));
  if (isNaN(ms) || ms < 0) return null;
  return Math.round(ms / 864e5 * 10) / 10;
}

function _encTypeLabel(enc) {
  if (enc.type) return enc.type;
  if (enc.cls === 'IMP')  return 'Inpatient';
  if (enc.cls === 'EMER') return 'Emergency';
  if (enc.cls === 'AMB')  return 'Ambulatory';
  return enc.cls || 'Other';
}

function _destroyChart(id) {
  if (_charts[id]) { try { _charts[id].destroy(); } catch (_) {} delete _charts[id]; }
}

function _mkBar(id, labels, datasets, opts = {}) {
  _destroyChart(id);
  const cv = document.getElementById(id);
  if (!cv) return;

  // Look up axis labels from registry; opts can override.
  // For horizontal charts the rotated y-axis title clashes with category
  // labels — so we never apply a y-axis title to horizontal charts.
  const [regX, regY] = _CHART_LABELS[id] || [];
  const isHBar   = !!opts.horizontal;
  const xLabel   = opts.xLabel ?? regX ?? null;
  const yLabel   = (!isHBar) ? (opts.yLabel ?? regY ?? null) : null;
  const _at      = text => text
    ? { display: true, text, color: '#6e7681', font: { size: 9 }, padding: { top: 3, bottom: 3 } }
    : { display: false };

  _charts[id] = new Chart(cv, {
    type: 'bar',
    data: { labels, datasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      // Extra padding so axis titles / tick labels never clip at canvas edge
      layout: { padding: { left: isHBar ? 2 : 4, right: 8, top: 4, bottom: 2 } },
      plugins: { legend: { display: false }, ...opts.plugins },
      scales: {
        x: {
          stacked: !!opts.stacked,
          ticks: {
            color: _TC, font: { size: 10 },
            // Vertical bars put categories on the x-axis — show every label (rotate
            // as needed). Horizontal bars put values here, so thinning is fine.
            maxRotation: isHBar ? (opts.rotateX || 0) : (opts.rotateX ?? 45),
            autoSkip: isHBar,
            ...(isHBar ? { maxTicksLimit: 20 } : {}),
          },
          grid:  { color: _GC },
          title: _at(xLabel),
        },
        y: {
          stacked:     !!opts.stacked,
          beginAtZero: true,
          // Horizontal bars put categories on the y-axis — never drop a category
          // label. Vertical bars put values here, so thinning is fine.
          ticks: {
            color: _TC, font: { size: 10 },
            autoSkip: !isHBar,
            ...(isHBar ? {} : { maxTicksLimit: 15 }),
          },
          grid:  { color: _GC },
          title: _at(yLabel),
          ...opts.yAxis,
        },
      },
      indexAxis: isHBar ? 'y' : 'x',
      ...opts.extra,
    },
  });
}

function _mkHBar(id, labels, values, color, opts = {}) {
  _mkBar(id, labels, [{
    data: values,
    backgroundColor: color + '44',
    borderColor: color,
    borderWidth: 1.5,
    borderRadius: 3,
  }], { horizontal: true, ...opts });
}

function _mkVBar(id, labels, values, color, opts = {}) {
  _mkBar(id, labels, [{
    data: values,
    backgroundColor: color + '44',
    borderColor: color,
    borderWidth: 1.5,
    borderRadius: 3,
    label: opts.label || '',
  }], opts);
}

function _mkDonut(id, labels, values, colors) {
  _destroyChart(id);
  const cv = document.getElementById(id);
  if (!cv || !labels.length) return;
  _charts[id] = new Chart(cv, {
    type: 'doughnut',
    data: {
      labels,
      datasets: [{ data: values, backgroundColor: colors.map(c => c + '55'), borderColor: colors, borderWidth: 1.5, hoverOffset: 4 }],
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 10 }, padding: 8, boxWidth: 12 } } },
    },
  });
}

function _tally(arr, key) {
  const m = {};
  arr.forEach(x => { const v = (key ? x[key] : x) || 'Unknown'; m[v] = (m[v] || 0) + 1; });
  return m;
}

function _top(map, n = 20) {
  return Object.entries(map).sort((a, b) => b[1] - a[1]).slice(0, n);
}

// ── Master Analytics renderer ─────────────────────────────────────────────────
function renderAnalytics(d) {
  const encs  = d.encounters  || [];
  const conds = d.conditions  || [];
  const labs  = d.labs        || [];
  const meds  = d.medications || [];
  const procs = d.procedures  || [];
  const vits  = d.vitals      || [];

  // ── Section A: Encounter Analytics ──────────────────────────────────────────

  // A1 — LOS horizontal bar (compute from start/end if no los field)
  {
    const rows = encs
      .map((e, i) => ({ label: `#${i + 1}  ${(e.start || '').slice(0, 10)}`, los: _encLOS(e) }))
      .filter(r => r.los != null);
    if (rows.length) {
      _mkHBar('chartA_los', rows.map(r => r.label), rows.map(r => r.los), '#58a6ff', {
        plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.raw} days` } } },
      });
    }
  }

  // A2 — Encounter class breakdown (bar)
  {
    const m = _tally(encs, null);
    const labels = encs.reduce((acc, e) => {
      const k = _encTypeLabel(e); acc[k] = (acc[k] || 0) + 1; return acc;
    }, {});
    const keys = Object.keys(labels);
    const pal  = ['#58a6ff','#3fb950','#ffa657','#f85149','#d2a8ff','#79c0ff'];
    _mkBar('chartA_types', keys, keys.map((k, i) => ({
      label: k, data: [labels[k]], backgroundColor: pal[i % pal.length] + '44',
      borderColor: pal[i % pal.length], borderWidth: 1.5, borderRadius: 3,
    })), { plugins: { legend: { display: false } } });
  }

  // A3 — Records per encounter (stacked bar)
  {
    const labels = encs.map((_, i) => `#${i + 1}`);
    const mk = (key, color) => ({
      label: key.charAt(0).toUpperCase() + key.slice(1),
      data: encs.map(e => (e.encounterData?.[key] || []).length),
      backgroundColor: color + '55', borderColor: color, borderWidth: 1, stack: 'a', borderRadius: 2,
    });
    _mkBar('chartA_records', labels, [
      mk('conditions',  '#fb7185'), mk('medications', '#c084fc'),
      mk('labs',        '#818cf8'), mk('vitals',      '#f87171'),
      mk('procedures',  '#4ade80'),
    ], {
      stacked: true,
      plugins: { legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 9 }, padding: 6, boxWidth: 10 } }, tooltip: { mode: 'index', intersect: false } },
    });
  }

  // A4 — Admit source distribution
  {
    const m = encs.reduce((acc, e) => { const s = e.admitSource || 'Unknown'; acc[s] = (acc[s] || 0) + 1; return acc; }, {});
    const entries = _top(m, 10);
    _mkHBar('chartA_admit', entries.map(e => e[0]), entries.map(e => e[1]), '#22d3ee');
  }

  // A5 — Encounter status bar
  {
    const m = _tally(encs.map(e => e.status));
    const keys = Object.keys(m);
    const sc = { finished: '#3fb950', 'in-progress': '#ffa657', unknown: '#484f58' };
    _mkBar('chartA_status', keys, [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (sc[k] || '#58a6ff') + '44'),
      borderColor: keys.map(k => sc[k] || '#58a6ff'),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // A6 — Service type (category) distribution
  {
    const m = encs.reduce((acc, e) => {
      const svc = e.serviceType || 'Unknown';
      acc[svc] = (acc[svc] || 0) + 1;
      return acc;
    }, {});
    const entries = _top(m, 15);
    if (entries.length) {
      _mkHBar('chartA_serviceType', entries.map(e => e[0]), entries.map(e => e[1]), '#a78bfa', {
        plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.raw} encounter${c.raw !== 1 ? 's' : ''}` } } },
      });
    }
  }

  // A7 — Care location distribution
  {
    const m = encs.reduce((acc, e) => {
      const loc = e.location || 'Unknown';
      acc[loc] = (acc[loc] || 0) + 1;
      return acc;
    }, {});
    const entries = _top(m, 15);
    if (entries.length) {
      _mkHBar('chartA_location', entries.map(e => e[0]), entries.map(e => e[1]), '#34d399', {
        plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.raw} encounter${c.raw !== 1 ? 's' : ''}` } } },
      });
    }
  }

  // ── Section B: Diagnosis Analysis ───────────────────────────────────────────

  // B1 — Diagnoses per encounter
  {
    const rows = encs
      .map((e, i) => ({ label: `#${i + 1}`, n: conds.filter(c => c.encounterRef === e.id).length }))
      .filter(r => r.n > 0);
    _mkVBar('chartB_perEnc', rows.map(r => r.label), rows.map(r => r.n), '#fb7185');
  }

  // B2 — ICD system bar
  {
    const m = _tally(conds, 'codeSystem');
    const pal = { 'ICD-10': '#58a6ff', 'ICD-9': '#ffa657', 'Unknown': '#484f58' };
    const keys = Object.keys(m);
    _mkBar('chartB_icd', keys, [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (pal[k] || '#79c0ff') + '44'),
      borderColor: keys.map(k => pal[k] || '#79c0ff'),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // B3 — Diagnosis status bar
  {
    const m = _tally(conds, 'status');
    const pal = { active: '#f85149', resolved: '#3fb950', inactive: '#6e7681', remission: '#ffa657', unknown: '#484f58' };
    const keys = Object.keys(m);
    _mkBar('chartB_status', keys.map(k => k.charAt(0).toUpperCase() + k.slice(1)), [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (pal[k] || '#58a6ff') + '44'),
      borderColor: keys.map(k => pal[k] || '#58a6ff'),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // B4 — All diagnoses frequency (horizontal bar, sorted)
  {
    const m = _tally(conds, 'name');
    const entries = _top(m, 25);
    _mkHBar('chartB_top', entries.map(e => e[0]), entries.map(e => e[1]), '#d2a8ff', {
      plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? 's' : ''}` } } },
    });
  }

  // ── Section C: Lab Results ───────────────────────────────────────────────────

  // C1 — Lab flag distribution
  {
    const flags = ['Normal', 'H', 'HH', 'L', 'LL', 'A'];
    const flagColors = { Normal: '#3fb950', H: '#ffa657', HH: '#f85149', L: '#79c0ff', LL: '#58a6ff', A: '#ff7b72' };
    const m = {};
    labs.forEach(l => {
      const f = !l.flag || l.flag === 'N' ? 'Normal' : l.flag;
      m[f] = (m[f] || 0) + 1;
    });
    const present = flags.filter(f => m[f]);
    _mkBar('chartC_flags', present, [{
      data: present.map(f => m[f] || 0),
      backgroundColor: present.map(f => (flagColors[f] || '#58a6ff') + '44'),
      borderColor: present.map(f => flagColors[f] || '#58a6ff'),
      borderWidth: 1.5, borderRadius: 3,
    }], { plugins: { legend: { display: false } } });
  }

  // C2 — Labs per encounter
  {
    const rows = encs
      .map((e, i) => ({ label: `#${i + 1}`, n: (e.encounterData?.labs || []).length }))
      .filter(r => r.n > 0);
    _mkVBar('chartC_perEnc', rows.map(r => r.label), rows.map(r => r.n), '#818cf8');
  }

  // C3 — Abnormal lab count grouped by lab name (top 15 most-flagged tests)
  {
    const abnormal = labs.filter(l => l.flag && l.flag !== 'N');
    const flagColors = { H: '#ffa657', HH: '#f85149', L: '#79c0ff', LL: '#58a6ff', A: '#ff7b72' };
    if (abnormal.length) {
      const byName = {};
      abnormal.forEach(l => { byName[l.name] = (byName[l.name] || 0) + 1; });
      const entries = _top(byName, 15);
      // pick the most common flag for each lab to use as colour
      const labFlag = {};
      abnormal.forEach(l => {
        if (!labFlag[l.name]) labFlag[l.name] = {};
        labFlag[l.name][l.flag] = (labFlag[l.name][l.flag] || 0) + 1;
      });
      const dominantFlag = name => Object.entries(labFlag[name] || {}).sort((a,b)=>b[1]-a[1])[0]?.[0] || 'A';
      _mkHBar('chartC_abnormal',
        entries.map(e => e[0].slice(0, 30)),
        entries.map(e => e[1]),
        '#ff7b72', {
          plugins: {
            legend: { display: false },
            tooltip: { callbacks: { label: c => {
              const f = dominantFlag(entries[c.dataIndex][0]);
              return ` ${c.raw} abnormal result${c.raw !== 1 ? 's' : ''} [${f}]`;
            }}},
          },
        });
    }
  }

  // C4 — All labs bar (latest values, coloured by flag)
  {
    const flagColors = { H: '#ffa657', HH: '#f85149', L: '#79c0ff', LL: '#58a6ff', A: '#ff7b72', N: '#3fb950' };
    const numeric = labs.filter(l => typeof l.value === 'number');
    if (numeric.length) {
      _mkBar('chartC_allLabs', numeric.map(l => l.name.slice(0, 22)), [{
        label: 'Value',
        data: numeric.map(l => typeof l.value === 'number' ? +l.value.toFixed(2) : l.value),
        backgroundColor: numeric.map(l => (flagColors[l.flag] || '#3fb950') + '44'),
        borderColor: numeric.map(l => flagColors[l.flag] || '#3fb950'),
        borderWidth: 1.5, borderRadius: 3,
      }], {
        horizontal: true,
        plugins: { legend: { display: false }, tooltip: {
          callbacks: { label: (ctx) => {
            const l = numeric[ctx.dataIndex];
            return ` ${ctx.raw} ${l.unit}  [flag: ${l.flag || '—'}]`;
          }},
        }},
      });
    }
  }

  // ── Section D: Vitals ────────────────────────────────────────────────────────

  // D1 — Vital values horizontal bar, colour-coded by status
  {
    if (vits.length) {
      _mkBar('chartD_vitals', vits.map(v => v.name), [{
        data: vits.map(v => typeof v.value === 'number' ? +v.value.toFixed(1) : parseFloat(v.value) || 0),
        backgroundColor: vits.map(v => (v.status === 'abnormal' ? '#f85149' : '#58a6ff') + '44'),
        borderColor: vits.map(v => v.status === 'abnormal' ? '#f85149' : '#58a6ff'),
        borderWidth: 1.5, borderRadius: 3,
      }], {
        horizontal: true,
        plugins: { legend: { display: false }, tooltip: {
          callbacks: { label: (ctx) => {
            const v = vits[ctx.dataIndex];
            const nr = v.normalRange ? `  range: ${v.normalRange[0]}–${v.normalRange[1]}` : '';
            return ` ${ctx.raw} ${v.unit}${nr}  (${v.status})`;
          }},
        }},
      });
    }
  }

  // D2 — Normal vs abnormal vitals bar
  {
    const norm = vits.filter(v => v.status !== 'abnormal').length;
    const abn  = vits.filter(v => v.status === 'abnormal').length;
    _mkBar('chartD_vitalStatus', ['Normal', 'Abnormal'], [{
      data: [norm, abn],
      backgroundColor: ['#3fb95044', '#f8514944'],
      borderColor: ['#3fb950', '#f85149'],
      borderWidth: 1.5, borderRadius: 4,
    }], {});
  }

  // ── Section E: Medications & Procedures ─────────────────────────────────────

  // E1 — Medication status
  {
    const m = _tally(meds, 'status');
    const pal = { active: '#3fb950', completed: '#58a6ff', stopped: '#f85149', 'on-hold': '#ffa657', unknown: '#484f58' };
    const keys = Object.keys(m);
    _mkBar('chartE_medStatus', keys, [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (pal[k] || '#79c0ff') + '44'),
      borderColor: keys.map(k => pal[k] || '#79c0ff'),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // E2 — Procedures per encounter
  {
    const rows = encs
      .map((e, i) => ({ label: `#${i + 1}`, n: (e.encounterData?.procedures || []).length }))
      .filter(r => r.n > 0);
    _mkVBar('chartE_procsPerEnc', rows.map(r => r.label), rows.map(r => r.n), '#4ade80');
  }

  // E3 — Medication routes
  {
    const m = _tally(meds.map(m => m.route || 'Unknown'));
    const entries = _top(m, 10);
    _mkHBar('chartE_medRoutes', entries.map(e => e[0]), entries.map(e => e[1]), '#c084fc');
  }

  // E4 — Top medications horizontal bar
  {
    const m = _tally(meds, 'name');
    const entries = _top(m, 20);
    _mkHBar('chartE_topMeds', entries.map(e => e[0].slice(0, 35)), entries.map(e => e[1]), '#a78bfa', {
      plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? 's' : ''}` } } },
    });
  }

  // E5 — Top procedures horizontal bar
  {
    const m = _tally(procs, 'name');
    const entries = _top(m, 20);
    _mkHBar('chartE_topProcs', entries.map(e => e[0].slice(0, 35)), entries.map(e => e[1]), '#4ade80', {
      plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? 's' : ''}` } } },
    });
  }

  // ── Section F: Temporal Analysis ────────────────────────────────────────────

  const _toMs = s => s ? Date.parse(s.replace(' ', 'T')) : NaN;

  // F1 — Encounter timeline (floating bar — Gantt style)
  {
    const epoch = Math.min(...encs.map(e => _toMs(e.start)).filter(n => !isNaN(n)));
    const toDays = ms => isNaN(ms) ? null : +((ms - epoch) / 864e5).toFixed(2);
    const clsPal = e =>
      e.cls === 'IMP'  ? '#58a6ff' :
      e.cls === 'EMER' ? '#f85149' :
      e.cls === 'AMB'  ? '#3fb950' : '#ffa657';
    const rows = encs.map(e => {
      const s = toDays(_toMs(e.start)), en = toDays(_toMs(e.end));
      return (s != null && en != null) ? [s, en <= s ? s + 0.05 : en] : null;
    });
    if (rows.some(Boolean)) {
      _destroyChart('chartF_timeline');
      const cv = document.getElementById('chartF_timeline');
      if (cv) {
        _charts['chartF_timeline'] = new Chart(cv, {
          type: 'bar',
          data: {
            labels: encs.map((e, i) => `#${i+1}  ${(e.start||'').slice(0,10)}`),
            datasets: [{
              data: rows,
              backgroundColor: encs.map(e => clsPal(e) + '55'),
              borderColor:     encs.map(e => clsPal(e)),
              borderWidth: 1.5, borderRadius: 3,
            }],
          },
          options: {
            indexAxis: 'y', responsive: true, maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: { callbacks: { label: ctx => {
                const e = encs[ctx.dataIndex];
                const los = _encLOS(e);
                return ` ${e.start || '?'} → ${e.end || 'ongoing'}${los != null ? `  (${los} days)` : ''}`;
              }}},
            },
            scales: {
              x: { ticks: { color: _TC, font: { size: 10 } }, grid: { color: _GC },
                   title: { display: true, text: 'Days since first encounter', color: _TC, font: { size: 10 } } },
              y: { ticks: { color: _TC, font: { size: 9 } }, grid: { color: _GC } },
            },
          },
        });
      }
    }
  }

  // F2 — Encounters by hour of day
  {
    const hours = new Array(24).fill(0);
    encs.forEach(e => {
      const ms = _toMs(e.start);
      if (!isNaN(ms)) hours[new Date(ms).getHours()]++;
    });
    const hLabels = Array.from({length: 24}, (_, i) => `${String(i).padStart(2,'0')}h`);
    _mkVBar('chartF_hour', hLabels, hours, '#38bdf8', { rotateX: 45 });
  }

  // F3 — Encounters by day of week
  {
    const days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
    const dow = new Array(7).fill(0);
    encs.forEach(e => {
      const ms = _toMs(e.start);
      if (!isNaN(ms)) dow[(new Date(ms).getDay() + 6) % 7]++;
    });
    _mkVBar('chartF_dow', days, dow, '#818cf8');
  }

  // ── Section G: Vitals Deep Dive ──────────────────────────────────────────────

  // G1 — Cross-encounter vitals (grouped bar)
  {
    const vNames = [...new Set(encs.flatMap(e =>
      (e.encounterData?.vitals || []).map(v => v.name)
    ))].sort();
    if (vNames.length) {
      const palette = ['#58a6ff','#f87171','#3fb950','#ffa657','#c084fc','#79c0ff','#f85149','#4ade80'];
      const datasets = encs.map((e, i) => {
        const vMap = {};
        (e.encounterData?.vitals || []).forEach(v => {
          if (!vMap[v.name] || v.raw > vMap[v.name].raw) vMap[v.name] = v;
        });
        return {
          label: `Enc #${i+1}`,
          data: vNames.map(n => vMap[n] && typeof vMap[n].value === 'number' ? +vMap[n].value.toFixed(1) : null),
          backgroundColor: palette[i % palette.length] + '44',
          borderColor:     palette[i % palette.length],
          borderWidth: 1.5, borderRadius: 2,
        };
      });
      _mkBar('chartG_crossEnc', vNames, datasets, {
        plugins: {
          legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 9 }, padding: 6, boxWidth: 10 } },
          tooltip: { mode: 'index', intersect: false },
        },
      });
    }
  }

  // G2 — Normal vs abnormal vitals per encounter (stacked bar)
  {
    const gLabels = encs.map((_, i) => `Enc #${i+1}`);
    _mkBar('chartG_vitalStatus', gLabels, [
      { label: 'Normal',   data: encs.map(e => (e.encounterData?.vitals||[]).filter(v => v.status !== 'abnormal').length), backgroundColor: '#3fb95044', borderColor: '#3fb950', borderWidth: 1.5, borderRadius: 2, stack: 'a' },
      { label: 'Abnormal', data: encs.map(e => (e.encounterData?.vitals||[]).filter(v => v.status === 'abnormal').length), backgroundColor: '#f8514944', borderColor: '#f85149', borderWidth: 1.5, borderRadius: 2, stack: 'a' },
    ], {
      stacked: true,
      plugins: {
        legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 10 }, padding: 8, boxWidth: 12 } },
        tooltip: { mode: 'index', intersect: false },
      },
    });
  }

  // ── Section H: Lab Reference Analysis ───────────────────────────────────────

  // H1 — Reference range compliance per encounter (stacked: below / in / above)
  {
    const hLabels = encs.map((_, i) => `Enc #${i+1}`);
    const below   = encs.map(e => (e.encounterData?.labs||[]).filter(l => l.refLow  != null && typeof l.value === 'number' && l.value < l.refLow).length);
    const inRange = encs.map(e => (e.encounterData?.labs||[]).filter(l => l.refLow  != null && l.refHigh != null && typeof l.value === 'number' && l.value >= l.refLow && l.value <= l.refHigh).length);
    const above   = encs.map(e => (e.encounterData?.labs||[]).filter(l => l.refHigh != null && typeof l.value === 'number' && l.value > l.refHigh).length);
    _mkBar('chartH_refRange', hLabels, [
      { label: 'Below',   data: below,   backgroundColor: '#79c0ff44', borderColor: '#79c0ff', borderWidth: 1.5, borderRadius: 2, stack: 'a' },
      { label: 'In range',data: inRange, backgroundColor: '#3fb95044', borderColor: '#3fb950', borderWidth: 1.5, borderRadius: 2, stack: 'a' },
      { label: 'Above',   data: above,   backgroundColor: '#f8514944', borderColor: '#f85149', borderWidth: 1.5, borderRadius: 2, stack: 'a' },
    ], {
      stacked: true,
      plugins: {
        legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 10 }, padding: 8, boxWidth: 12 } },
        tooltip: { mode: 'index', intersect: false },
      },
    });
  }

  // H2 — Abnormal lab rate % per encounter
  {
    const hLabels = encs.map((_, i) => `Enc #${i+1}`);
    const rates = encs.map(e => {
      const el = e.encounterData?.labs || [];
      if (!el.length) return 0;
      return +(el.filter(l => l.flag && l.flag !== 'N' && l.flag !== '').length / el.length * 100).toFixed(1);
    });
    _destroyChart('chartH_abnRate');
    const cv = document.getElementById('chartH_abnRate');
    if (cv) {
      _charts['chartH_abnRate'] = new Chart(cv, {
        type: 'bar',
        data: {
          labels: hLabels,
          datasets: [{
            label: '% abnormal',
            data: rates,
            backgroundColor: rates.map(r => (r > 50 ? '#f85149' : r > 20 ? '#ffa657' : '#3fb950') + '44'),
            borderColor:     rates.map(r =>  r > 50 ? '#f85149' : r > 20 ? '#ffa657' : '#3fb950'),
            borderWidth: 1.5, borderRadius: 3,
          }],
        },
        options: {
          responsive: true, maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: { callbacks: { label: ctx => ` ${ctx.raw}% of labs flagged abnormal` } },
          },
          scales: {
            x: { ticks: { color: _TC, font: { size: 10 } }, grid: { color: _GC } },
            y: { beginAtZero: true, max: 100, ticks: { color: _TC, font: { size: 10 }, callback: v => v + '%' }, grid: { color: _GC } },
          },
        },
      });
    }
  }

  // ── Section I: Admission, Discharge & Notes ──────────────────────────────────

  // I1 — Discharge disposition horizontal bar
  {
    const m = encs.reduce((acc, e) => { if (e.dischDisp) acc[e.dischDisp] = (acc[e.dischDisp]||0)+1; return acc; }, {});
    const entries = _top(m, 10);
    _mkHBar('chartI_dischDisp', entries.map(e => e[0].slice(0,30)), entries.map(e => e[1]), '#34d399');
  }

  // I2 — Clinical note types
  {
    const m = _tally(d.notes || [], 'typeDisplay');
    const entries = _top(m, 10);
    _mkHBar('chartI_noteTypes', entries.map(e => e[0]), entries.map(e => e[1]), '#22d3ee');
  }

  // I3 — Notes + Reports per encounter (grouped bar)
  {
    const iLabels = encs.map((_, i) => `Enc #${i+1}`);
    _mkBar('chartI_notesPerEnc', iLabels, [
      { label: 'Notes',   data: encs.map(e => (e.encounterData?.notes||[]).length),            backgroundColor: '#34d39944', borderColor: '#34d399', borderWidth: 1.5, borderRadius: 2 },
      { label: 'Reports', data: encs.map(e => (e.encounterData?.diagnosticReports||[]).length), backgroundColor: '#38bdf844', borderColor: '#38bdf8', borderWidth: 1.5, borderRadius: 2 },
    ], {
      plugins: {
        legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 10 }, padding: 8, boxWidth: 12 } },
        tooltip: { mode: 'index', intersect: false },
      },
    });
  }

  // Inject download buttons into all analytics chart cards
  setTimeout(_injectDownloadBtns, 0);
}
// ── Utility ───────────────────────────────────────────────────────────────────
function esc(str) {
  if (str == null) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function kv(label, val) {
  if (!val && val !== 0) return "";
  return `
    <div style="display:flex;gap:0.5rem;">
      <span style="color:#6e7681;white-space:nowrap;">${esc(label)}:</span>
      <span style="color:#cdd9e5;font-weight:600;">${esc(String(val))}</span>
    </div>`;
}

// ── Population Analytics ──────────────────────────────────────────────────────
let _popData    = null;
let _popLoading = false;

function togglePopulation() {
  const panel  = $("populationPanel");
  const btn    = $("popToggleBtn");
  const isOpen = !panel.classList.contains("hidden");
  if (isOpen) {
    panel.classList.add("hidden");
    btn.classList.remove("active");
    // restore visible state depending on whether a patient is loaded
    if (currentData) showDashboard();
    else showEmpty();
    return;
  }
  // hide all patient UI, show population panel
  emptyState.classList.add("hidden");
  loadingState.classList.add("hidden");
  dashboard.classList.add("hidden");
  tabNav.classList.add("hidden");
  patientInfoBar.classList.add("hidden");
  $("patientBadge").classList.add("hidden");
  panel.classList.remove("hidden");
  btn.classList.add("active");
  if (!_popData && !_popLoading) _loadPopulationAnalytics();
}

async function _loadPopulationAnalytics() {
  _popLoading = true;
  $("popProgress").classList.remove("hidden");
  $("popStats").classList.add("hidden");
  $("popCharts").classList.add("hidden");
  $("popProgressBar").style.width = "0%";
  $("popProgressText").textContent = "Fetching patient list…";
  $("popProgressSub").textContent  = "";

  let patients = [];
  try {
    const r = await fetch("/api/patients");
    patients = (await r.json()).patients || [];
  } catch (e) {
    $("popProgressText").textContent = "Failed to load patient list.";
    _popLoading = false;
    return;
  }

  const total   = patients.length;
  const allData = [];
  const BATCH   = 10;

  for (let i = 0; i < total; i += BATCH) {
    const batch = patients.slice(i, i + BATCH);
    const results = await Promise.all(
      batch.map(id => fetch(`/api/patients/${id}`).then(r => r.ok ? r.json() : null).catch(() => null))
    );
    allData.push(...results.filter(Boolean));
    const pct = Math.round(allData.length / total * 100);
    $("popProgressBar").style.width  = pct + "%";
    $("popProgressText").textContent = `Loading… ${pct}%`;
    $("popProgressSub").textContent  = `${allData.length} / ${total} patients`;
  }

  _popData = allData;
  _popLoading = false;
  $("popProgress").classList.add("hidden");
  $("popStats").classList.remove("hidden");
  $("popCharts").classList.remove("hidden");
  _renderPopulationCharts(allData);
}

function _renderPopulationCharts(all) {
  const allConds = all.flatMap(d => d.conditions  || []);
  const allMeds  = all.flatMap(d => d.medications || []);
  const allLabs  = all.flatMap(d => d.labs        || []);
  const allVits  = all.flatMap(d => d.vitals      || []);
  const allEncs  = all.flatMap(d => d.encounters  || []);
  const allProcs = all.flatMap(d => d.procedures  || []);
  const allNotes = all.flatMap(d => d.notes       || []);
  const allRpts  = all.flatMap(d =>
    (d.encounters || []).flatMap(e => e.encounterData?.diagnosticReports || [])
  );

  // Stats bar
  $("pStatPts").textContent   = all.length.toLocaleString();
  $("pStatEncs").textContent  = allEncs.length.toLocaleString();
  $("pStatDx").textContent    = allConds.length.toLocaleString();
  $("pStatMeds").textContent  = allMeds.length.toLocaleString();
  $("pStatLabs").textContent  = allLabs.length.toLocaleString();
  $("pStatProcs").textContent = allProcs.length.toLocaleString();
  $("pStatNotes").textContent = allNotes.length.toLocaleString();
  $("pStatVits").textContent  = allVits.length.toLocaleString();

  // ── B: Demographics ──────────────────────────────────────────────────────────

  // Gender donut
  {
    const m = _tally(all.map(d => d.demographics?.gender || "Unknown"));
    const keys  = Object.keys(m);
    const gPal  = { male: "#58a6ff", female: "#f472b6", other: "#ffa657", unknown: "#484f58" };
    _mkDonut("chartP_gender", keys, keys.map(k => m[k]),
      keys.map(k => gPal[k.toLowerCase()] || "#79c0ff"));
  }

  // Age histogram by decade
  {
    const buckets = {};
    all.forEach(d => {
      const a = d.demographics?.age;
      if (a == null) return;
      const k = Math.floor(a / 10) * 10 + "s";
      buckets[k] = (buckets[k] || 0) + 1;
    });
    const keys = Object.keys(buckets).sort((a, b) => parseInt(a) - parseInt(b));
    _mkVBar("chartP_ageHist", keys, keys.map(k => buckets[k]), "#79c0ff");
  }

  // Race horizontal bar
  {
    const entries = _top(_tally(all.map(d => d.demographics?.race || "Unknown")), 10);
    _mkHBar("chartP_race", entries.map(e => e[0]), entries.map(e => e[1]), "#22d3ee");
  }

  // Ethnicity donut (better than a bar when one category dominates)
  {
    const m    = _tally(all.map(d => d.demographics?.ethnicity || "Unknown"));
    const keys = Object.keys(m);
    const pal  = ["#38bdf8", "#f472b6", "#34d399", "#fbbf24", "#a78bfa", "#818cf8"];
    _mkDonut("chartP_ethnicity", keys, keys.map(k => m[k]),
      keys.map((_, i) => pal[i % pal.length]));
  }

  // ── C: Encounter Analytics ───────────────────────────────────────────────────

  // Encounter type breakdown
  {
    const m   = {};
    allEncs.forEach(e => { const k = _encTypeLabel(e); m[k] = (m[k] || 0) + 1; });
    const keys = Object.keys(m);
    const pal  = ["#58a6ff", "#3fb950", "#ffa657", "#f85149", "#d2a8ff", "#79c0ff"];
    _mkBar("chartP_encType", keys, keys.map((k, i) => ({
      label: k, data: [m[k]],
      backgroundColor: pal[i % pal.length] + "44",
      borderColor:     pal[i % pal.length],
      borderWidth: 1.5, borderRadius: 3,
    })), { plugins: { legend: { display: false } } });
  }

  // LOS histogram (binned)
  {
    const bins = { "0–1d": 0, "1–3d": 0, "3–7d": 0, "7–14d": 0, "14–30d": 0, ">30d": 0 };
    allEncs.forEach(e => {
      const los = _encLOS(e);
      if (los == null) return;
      if      (los <= 1)  bins["0–1d"]++;
      else if (los <= 3)  bins["1–3d"]++;
      else if (los <= 7)  bins["3–7d"]++;
      else if (los <= 14) bins["7–14d"]++;
      else if (los <= 30) bins["14–30d"]++;
      else                bins[">30d"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_losHist", keys, keys.map(k => bins[k]), "#38bdf8");
  }

  // Encounters per patient histogram
  {
    const bins = {};
    all.forEach(d => {
      const n = (d.encounters || []).length;
      const k = `${n}`;
      bins[k] = (bins[k] || 0) + 1;
    });
    const keys = Object.keys(bins).sort((a, b) => +a - +b);
    _mkVBar("chartP_encPerPt", keys, keys.map(k => bins[k]), "#3fb950", {
      plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} patient${c.raw !== 1 ? "s" : ""}` } } },
    });
  }

  // Admit source
  {
    const m = {};
    allEncs.forEach(e => { if (e.admitSource) m[e.admitSource] = (m[e.admitSource] || 0) + 1; });
    const entries = _top(m, 10);
    _mkHBar("chartP_admitSrc", entries.map(e => e[0]), entries.map(e => e[1]), "#22d3ee");
  }

  // Discharge disposition
  {
    const m = {};
    allEncs.forEach(e => { if (e.dischDisp) m[e.dischDisp] = (m[e.dischDisp] || 0) + 1; });
    const entries = _top(m, 10);
    _mkHBar("chartP_dischDisp", entries.map(e => e[0].slice(0, 35)), entries.map(e => e[1]), "#34d399");
  }

  // Service type (category) distribution across all encounters
  {
    const m = {};
    allEncs.forEach(e => {
      const svc = e.serviceType || 'Unknown';
      if (svc) m[svc] = (m[svc] || 0) + 1;
    });
    const entries = _top(m, 20);
    if (entries.length) {
      _mkHBar("chartP_serviceType",
        entries.map(e => e[0]),
        entries.map(e => e[1]),
        "#a78bfa", {
          plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.raw} encounter${c.raw !== 1 ? "s" : ""}` } } },
        });
    }
  }

  // ── D: Diagnosis Landscape ───────────────────────────────────────────────────

  // Top 30 diagnoses
  {
    const entries = _top(_tally(allConds, "name"), 30);
    _mkHBar("chartP_topDx",
      entries.map(e => e[0].slice(0, 50)),
      entries.map(e => e[1]),
      "#d2a8ff", {
        plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? "s" : ""}` } } },
      });
  }

  // Conditions per patient histogram
  {
    const bins = { "0": 0, "1–2": 0, "3–5": 0, "6–10": 0, "11–20": 0, ">20": 0 };
    all.forEach(d => {
      const n = (d.conditions || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 2)  bins["1–2"]++;
      else if (n <= 5)  bins["3–5"]++;
      else if (n <= 10) bins["6–10"]++;
      else if (n <= 20) bins["11–20"]++;
      else              bins[">20"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_condPerPt", keys, keys.map(k => bins[k]), "#fb7185");
  }

  // ICD system donut
  {
    const m    = _tally(allConds, "codeSystem");
    const keys = Object.keys(m);
    const pal  = { "ICD-10": "#58a6ff", "ICD-9": "#ffa657", "Unknown": "#484f58" };
    _mkDonut("chartP_icdSys", keys, keys.map(k => m[k]),
      keys.map(k => pal[k] || "#79c0ff"));
  }

  // Diagnosis status bar
  {
    const m    = _tally(allConds, "status");
    const keys = Object.keys(m);
    const pal  = { active: "#f85149", resolved: "#3fb950", inactive: "#6e7681", remission: "#ffa657", unknown: "#484f58" };
    _mkBar("chartP_dxStatus", keys.map(k => k.charAt(0).toUpperCase() + k.slice(1)), [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (pal[k] || "#58a6ff") + "44"),
      borderColor:     keys.map(k =>  pal[k] || "#58a6ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // ICD codes by initial letter (A–Z), split by ICD-9 / ICD-10
  {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
    const icd9  = Object.fromEntries(letters.map(l => [l, 0]));
    const icd10 = Object.fromEntries(letters.map(l => [l, 0]));
    allConds.forEach(c => {
      const ch = (c.code || "").trim().charAt(0).toUpperCase();
      if (!icd9.hasOwnProperty(ch)) return;
      if      (c.codeSystem === "ICD-9")  icd9[ch]++;
      else if (c.codeSystem === "ICD-10") icd10[ch]++;
    });
    _mkBar("chartP_icdAlpha", letters, [
      { label: "ICD-9",  data: letters.map(l => icd9[l]),
        backgroundColor: "#ffa657" + "44", borderColor: "#ffa657", borderWidth: 1.5, borderRadius: 3 },
      { label: "ICD-10", data: letters.map(l => icd10[l]),
        backgroundColor: "#58a6ff" + "44", borderColor: "#58a6ff", borderWidth: 1.5, borderRadius: 3 },
    ], {
      rotateX: 0,
      plugins: { legend: { display: true, position: "bottom", labels: { color: "#8b949e", font: { size: 10 }, padding: 8, boxWidth: 12 } } },
    });
  }

  // ── E: Lab Results ───────────────────────────────────────────────────────────

  // Lab flag distribution bar
  {
    const m = {};
    allLabs.forEach(l => { const f = (!l.flag || l.flag === "N") ? "Normal" : l.flag; m[f] = (m[f] || 0) + 1; });
    const order   = ["Normal", "H", "HH", "L", "LL", "A"];
    const present = order.filter(f => m[f]);
    const fc      = { Normal: "#3fb950", H: "#ffa657", HH: "#f85149", L: "#79c0ff", LL: "#58a6ff", A: "#ff7b72" };
    _mkBar("chartP_labFlags", present, [{
      data: present.map(f => m[f]),
      backgroundColor: present.map(f => (fc[f] || "#58a6ff") + "44"),
      borderColor:     present.map(f =>  fc[f] || "#58a6ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], { plugins: { legend: { display: false } } });
  }

  // Labs per patient histogram
  {
    const bins = { "0": 0, "1–10": 0, "11–30": 0, "31–60": 0, "61–120": 0, ">120": 0 };
    all.forEach(d => {
      const n = (d.labs || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 10) bins["1–10"]++;
      else if (n <= 30) bins["11–30"]++;
      else if (n <= 60) bins["31–60"]++;
      else if (n <= 120) bins["61–120"]++;
      else               bins[">120"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_labPerPt", keys, keys.map(k => bins[k]), "#818cf8");
  }

  // Abnormal lab rate per patient histogram
  {
    const bins = { "0%": 0, "1–10%": 0, "11–25%": 0, "26–50%": 0, "51–75%": 0, ">75%": 0 };
    all.forEach(d => {
      const labs = d.labs || [];
      if (!labs.length) { bins["0%"]++; return; }
      const r = labs.filter(l => l.flag && l.flag !== "N" && l.flag !== "").length / labs.length * 100;
      if      (r === 0) bins["0%"]++;
      else if (r <= 10) bins["1–10%"]++;
      else if (r <= 25) bins["11–25%"]++;
      else if (r <= 50) bins["26–50%"]++;
      else if (r <= 75) bins["51–75%"]++;
      else              bins[">75%"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_abnLabRate", keys, keys.map(k => bins[k]), "#f85149");
  }

  // Top 25 most common lab tests
  {
    const entries = _top(_tally(allLabs, "name"), 25);
    _mkHBar("chartP_topLabs",
      entries.map(e => e[0].slice(0, 38)),
      entries.map(e => e[1]),
      "#818cf8");
  }

  // ── F: Medications & Procedures ──────────────────────────────────────────────

  // Top 25 medications
  {
    const entries = _top(_tally(allMeds, "name"), 25);
    _mkHBar("chartP_topMeds",
      entries.map(e => e[0].slice(0, 40)),
      entries.map(e => e[1]),
      "#a78bfa", {
        plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? "s" : ""}` } } },
      });
  }

  // Top procedures
  {
    const entries = _top(_tally(allProcs, "name"), 20);
    if (entries.length) {
      _mkHBar("chartP_topProcs",
        entries.map(e => e[0].slice(0, 40)),
        entries.map(e => e[1]),
        "#4ade80", {
          plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} occurrence${c.raw !== 1 ? "s" : ""}` } } },
        });
    }
  }

  // Medication routes
  {
    const entries = _top(_tally(allMeds.map(m => m.route || "Unknown")), 10);
    _mkHBar("chartP_medRoute", entries.map(e => e[0]), entries.map(e => e[1]), "#c084fc");
  }

  // Medication status
  {
    const m    = _tally(allMeds, "status");
    const keys = Object.keys(m);
    const pal  = { active: "#3fb950", completed: "#58a6ff", stopped: "#f85149", "on-hold": "#ffa657", unknown: "#484f58" };
    _mkBar("chartP_medStatus", keys, [{
      data: keys.map(k => m[k]),
      backgroundColor: keys.map(k => (pal[k] || "#79c0ff") + "44"),
      borderColor:     keys.map(k =>  pal[k] || "#79c0ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], {});
  }

  // Medications per patient histogram
  {
    const bins = { "0": 0, "1–3": 0, "4–7": 0, "8–15": 0, "16–30": 0, ">30": 0 };
    all.forEach(d => {
      const n = (d.medications || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 3)  bins["1–3"]++;
      else if (n <= 7)  bins["4–7"]++;
      else if (n <= 15) bins["8–15"]++;
      else if (n <= 30) bins["16–30"]++;
      else              bins[">30"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_medPerPt", keys, keys.map(k => bins[k]), "#c084fc");
  }

  // ── G: Vitals & Notes ────────────────────────────────────────────────────────

  // Most common vitals across all patients
  {
    const entries = _top(_tally(allVits, "name"), 12);
    if (entries.length) {
      _mkHBar("chartP_topVitals",
        entries.map(e => e[0]),
        entries.map(e => e[1]),
        "#f87171");
    }
  }

  // Vital normal vs abnormal
  {
    const norm = allVits.filter(v => v.status !== "abnormal").length;
    const abn  = allVits.filter(v => v.status === "abnormal").length;
    _mkBar("chartP_vitalStatus", ["Normal", "Abnormal"], [{
      data: [norm, abn],
      backgroundColor: ["#3fb95044", "#f8514944"],
      borderColor:     ["#3fb950",   "#f85149"],
      borderWidth: 1.5, borderRadius: 4,
    }], {});
  }

  // Note type distribution
  {
    const entries = _top(_tally(allNotes, "typeDisplay"), 12);
    if (entries.length) {
      _mkHBar("chartP_noteTypes",
        entries.map(e => e[0]),
        entries.map(e => e[1]),
        "#34d399");
    }
  }

  // Diagnostic reports per patient histogram
  {
    const bins = { "0": 0, "1": 0, "2–3": 0, "4–6": 0, ">6": 0 };
    all.forEach(d => {
      const n = (d.encounters || []).reduce(
        (s, e) => s + (e.encounterData?.diagnosticReports || []).length, 0
      );
      if      (n === 0) bins["0"]++;
      else if (n === 1) bins["1"]++;
      else if (n <= 3)  bins["2–3"]++;
      else if (n <= 6)  bins["4–6"]++;
      else              bins[">6"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_rptPerPt", keys, keys.map(k => bins[k]), "#38bdf8");
  }

  // ── B extra: Birth Sex, Deceased, Anchor Year ──────────────────────────────

  // Birth sex donut
  {
    const m    = _tally(all.map(d => d.demographics?.birthSex || "Unknown"));
    const keys = Object.keys(m);
    const pal  = { M: "#58a6ff", F: "#f472b6", male: "#58a6ff", female: "#f472b6", Unknown: "#484f58" };
    _mkDonut("chartP_birthSex", keys, keys.map(k => m[k]),
      keys.map(k => pal[k] || pal[k.toLowerCase()] || "#79c0ff"));
  }

  // Deceased vs alive donut
  {
    const deceased = all.filter(d => {
      const v = d.demographics?.deceased;
      return v && v !== false && v !== "No" && v !== "no";
    }).length;
    _mkDonut("chartP_deceased", ["Alive", "Deceased"], [all.length - deceased, deceased],
      ["#3fb950", "#f85149"]);
  }

  // Anchor year group bar
  {
    const m    = _tally(all.map(d => d.demographics?.anchorYear || "Unknown"));
    const keys = Object.keys(m).sort();
    _mkVBar("chartP_anchorYear", keys, keys.map(k => m[k]), "#fbbf24");
  }

  // ── C extra: Avg LOS by Type, Encounter Status, ICU per Patient ────────────

  // Avg LOS by encounter type
  {
    const byType = {};
    allEncs.forEach(e => {
      const t   = _encTypeLabel(e);
      const los = _encLOS(e);
      if (los == null) return;
      if (!byType[t]) byType[t] = { total: 0, count: 0 };
      byType[t].total += los; byType[t].count++;
    });
    const keys = Object.keys(byType);
    const pal  = ["#58a6ff", "#3fb950", "#ffa657", "#f85149", "#d2a8ff"];
    _mkBar("chartP_avgLosByType", keys, [{
      data: keys.map(k => +(byType[k].total / byType[k].count).toFixed(1)),
      backgroundColor: keys.map((_, i) => pal[i % pal.length] + "44"),
      borderColor:     keys.map((_, i) => pal[i % pal.length]),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw} days` } } },
    });
  }

  // Encounter status donut
  {
    const m    = _tally(allEncs, "status");
    const keys = Object.keys(m);
    const pal  = { finished: "#3fb950", "in-progress": "#ffa657", unknown: "#484f58" };
    _mkDonut("chartP_encStatus", keys, keys.map(k => m[k]),
      keys.map(k => pal[k] || "#58a6ff"));
  }

  // ICU stays per patient histogram
  {
    const bins = { "0": 0, "1": 0, "2": 0, "3+": 0 };
    all.forEach(d => {
      const n = (d.encounters || []).reduce((s, e) => s + (e.children?.length || 0), 0);
      if      (n === 0) bins["0"]++;
      else if (n === 1) bins["1"]++;
      else if (n === 2) bins["2"]++;
      else              bins["3+"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_icuPerPt", keys, keys.map(k => bins[k]), "#22d3ee");
  }

  // ── E extra: Top Abnormal Labs, Ref Compliance, Critical Labs ──────────────

  // Top labs most-often flagged abnormal
  {
    const abnM = {};
    allLabs.filter(l => l.flag && l.flag !== "N" && l.flag !== "").forEach(l => {
      abnM[l.name] = (abnM[l.name] || 0) + 1;
    });
    const entries = _top(abnM, 20);
    if (entries.length)
      _mkHBar("chartP_topAbnLabs", entries.map(e => e[0].slice(0, 35)), entries.map(e => e[1]), "#f85149");
  }

  // Reference range compliance — all labs combined
  {
    const below   = allLabs.filter(l => l.refLow  != null && typeof l.value === "number" && l.value < l.refLow).length;
    const inRange = allLabs.filter(l => l.refLow  != null && l.refHigh != null && typeof l.value === "number" && l.value >= l.refLow && l.value <= l.refHigh).length;
    const above   = allLabs.filter(l => l.refHigh != null && typeof l.value === "number" && l.value > l.refHigh).length;
    const noRef   = allLabs.filter(l => l.refLow == null  && l.refHigh == null).length;
    _mkBar("chartP_refCompliance",
      ["Below Range", "In Range", "Above Range", "No Ref Data"],
      [{ data: [below, inRange, above, noRef],
         backgroundColor: ["#79c0ff44", "#3fb95044", "#f8514944", "#48495844"],
         borderColor:     ["#79c0ff",   "#3fb950",   "#f85149",   "#484958"],
         borderWidth: 1.5, borderRadius: 3 }],
      { plugins: { legend: { display: false },
          tooltip: { callbacks: { label: c => ` ${c.raw.toLocaleString()} labs` } } } });
  }

  // Highest abnormal rate per lab test (% of results flagged, min 5 results)
  {
    const byLab = {};
    allLabs.forEach(l => {
      if (!byLab[l.name]) byLab[l.name] = { total: 0, abn: 0 };
      byLab[l.name].total++;
      if (l.flag && l.flag !== "N" && l.flag !== "") byLab[l.name].abn++;
    });
    const entries = Object.entries(byLab)
      .filter(([, v]) => v.total >= 5 && v.abn > 0)
      .map(([k, v]) => [k, +(v.abn / v.total * 100).toFixed(1)])
      .sort((a, b) => b[1] - a[1])
      .slice(0, 15);
    if (entries.length) {
      _destroyChart("chartP_critLabs");
      const cv = document.getElementById("chartP_critLabs");
      if (cv) {
        _charts["chartP_critLabs"] = new Chart(cv, {
          type: "bar",
          data: {
            labels: entries.map(e => e[0].slice(0, 35)),
            datasets: [{
              data: entries.map(e => e[1]),
              backgroundColor: entries.map(e => (e[1] >= 75 ? "#f85149" : e[1] >= 40 ? "#ffa657" : "#fbbf24") + "44"),
              borderColor:     entries.map(e =>  e[1] >= 75 ? "#f85149" : e[1] >= 40 ? "#ffa657" : "#fbbf24"),
              borderWidth: 1.5, borderRadius: 3,
            }],
          },
          options: {
            responsive: true, maintainAspectRatio: false,
            indexAxis: "y",
            layout: { padding: { left: 2, right: 8, top: 4, bottom: 2 } },
            plugins: {
              legend: { display: false },
              tooltip: { callbacks: { label: c => ` ${c.raw}% of results flagged abnormal` } },
            },
            scales: {
              x: {
                beginAtZero: true, max: 100,
                ticks: { color: _TC, font: { size: 10 }, callback: v => v + "%" },
                grid:  { color: _GC },
                title: { display: true, text: "Abnormal Rate (%)", color: "#6e7681", font: { size: 9 }, padding: { top: 3, bottom: 3 } },
              },
              y: { ticks: { color: _TC, font: { size: 10 } }, grid: { color: _GC } },
            },
          },
        });
      }
    }
  }

  // ── F extra: Procedures per patient, Med dispense status ───────────────────

  // Procedures per patient histogram
  {
    const bins = { "0": 0, "1–5": 0, "6–15": 0, "16–30": 0, ">30": 0 };
    all.forEach(d => {
      const n = (d.procedures || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 5)  bins["1–5"]++;
      else if (n <= 15) bins["6–15"]++;
      else if (n <= 30) bins["16–30"]++;
      else              bins[">30"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_procsPerPt", keys, keys.map(k => bins[k]), "#4ade80");
  }

  // Medications per encounter — how many meds were dispensed per hospital encounter
  {
    const counts = allEncs
      .map(e => (e.encounterData?.medications || []).length)
      .filter(n => n > 0);
    const bins = { "1–3": 0, "4–7": 0, "8–15": 0, "16–30": 0, ">30": 0 };
    counts.forEach(n => {
      if      (n <= 3)  bins["1–3"]++;
      else if (n <= 7)  bins["4–7"]++;
      else if (n <= 15) bins["8–15"]++;
      else if (n <= 30) bins["16–30"]++;
      else              bins[">30"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_medDispStatus", keys, keys.map(k => bins[k]), "#818cf8", {
      plugins: { tooltip: { callbacks: { label: c => ` ${c.raw} encounter${c.raw !== 1 ? "s" : ""}` } } },
    });
  }

  // ── G extra: Vitals per patient, Notes per patient ──────────────────────────

  // Vitals per patient histogram
  {
    const bins = { "0": 0, "1–5": 0, "6–15": 0, "16–30": 0, ">30": 0 };
    all.forEach(d => {
      const n = (d.vitals || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 5)  bins["1–5"]++;
      else if (n <= 15) bins["6–15"]++;
      else if (n <= 30) bins["16–30"]++;
      else              bins[">30"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_vitPerPt", keys, keys.map(k => bins[k]), "#f87171");
  }

  // Notes per patient histogram
  {
    const bins = { "0": 0, "1–2": 0, "3–5": 0, "6–10": 0, ">10": 0 };
    all.forEach(d => {
      const n = (d.notes || []).length;
      if      (n === 0) bins["0"]++;
      else if (n <= 2)  bins["1–2"]++;
      else if (n <= 5)  bins["3–5"]++;
      else if (n <= 10) bins["6–10"]++;
      else              bins[">10"]++;
    });
    const keys = Object.keys(bins);
    _mkVBar("chartP_notePerPt", keys, keys.map(k => bins[k]), "#34d399");
  }

  // ── H: Cross-Dimensional Analysis ──────────────────────────────────────────

  // Avg encounters by gender
  {
    const byG = {};
    all.forEach(d => {
      const g = d.demographics?.gender || "Unknown";
      if (!byG[g]) byG[g] = { total: 0, count: 0 };
      byG[g].total += (d.encounters || []).length; byG[g].count++;
    });
    const keys = Object.keys(byG);
    const pal  = { Male: "#58a6ff", Female: "#f472b6", male: "#58a6ff", female: "#f472b6" };
    _mkBar("chartP_genderVsEnc", keys, [{
      data: keys.map(k => +(byG[k].total / byG[k].count).toFixed(2)),
      backgroundColor: keys.map(k => (pal[k] || "#79c0ff") + "44"),
      borderColor:     keys.map(k =>  pal[k] || "#79c0ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw} encounters per patient` } } },
    });
  }

  // Avg conditions by age group
  {
    const byAge = {};
    all.forEach(d => {
      const a = d.demographics?.age; if (a == null) return;
      const k = Math.floor(a / 10) * 10 + "s";
      if (!byAge[k]) byAge[k] = { total: 0, count: 0 };
      byAge[k].total += (d.conditions || []).length; byAge[k].count++;
    });
    const keys = Object.keys(byAge).sort((a, b) => parseInt(a) - parseInt(b));
    _mkVBar("chartP_ageVsCond", keys,
      keys.map(k => +(byAge[k].total / byAge[k].count).toFixed(1)),
      "#fb7185", {
        plugins: { tooltip: { callbacks: { label: c => ` avg ${c.raw} conditions` } } },
      });
  }

  // Avg LOS by age group
  {
    const byAge = {};
    all.forEach(d => {
      const a = d.demographics?.age; if (a == null) return;
      const k = Math.floor(a / 10) * 10 + "s";
      (d.encounters || []).forEach(e => {
        const los = _encLOS(e); if (los == null) return;
        if (!byAge[k]) byAge[k] = { total: 0, count: 0 };
        byAge[k].total += los; byAge[k].count++;
      });
    });
    const keys = Object.keys(byAge).sort((a, b) => parseInt(a) - parseInt(b));
    _mkVBar("chartP_ageVsLos", keys,
      keys.map(k => +(byAge[k].total / byAge[k].count).toFixed(1)),
      "#38bdf8", {
        plugins: { tooltip: { callbacks: { label: c => ` avg ${c.raw} days LOS` } } },
      });
  }

  // Avg abnormal lab % by gender
  {
    const byG = {};
    all.forEach(d => {
      const g    = d.demographics?.gender || "Unknown";
      const labs = d.labs || [];
      if (!labs.length) return;
      const rate = labs.filter(l => l.flag && l.flag !== "N" && l.flag !== "").length / labs.length * 100;
      if (!byG[g]) byG[g] = { total: 0, count: 0 };
      byG[g].total += rate; byG[g].count++;
    });
    const keys = Object.keys(byG);
    const pal  = { Male: "#58a6ff", Female: "#f472b6", male: "#58a6ff", female: "#f472b6" };
    _mkBar("chartP_genderVsAbnLab", keys, [{
      data: keys.map(k => +(byG[k].total / byG[k].count).toFixed(1)),
      backgroundColor: keys.map(k => (pal[k] || "#79c0ff") + "44"),
      borderColor:     keys.map(k =>  pal[k] || "#79c0ff"),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw}% abnormal labs` } } },
    });
  }

  // Avg abnormal lab % by race
  {
    const byR = {};
    all.forEach(d => {
      const race = d.demographics?.race || "Unknown";
      const labs = d.labs || [];
      if (!labs.length) return;
      const rate = labs.filter(l => l.flag && l.flag !== "N" && l.flag !== "").length / labs.length * 100;
      if (!byR[race]) byR[race] = { total: 0, count: 0 };
      byR[race].total += rate; byR[race].count++;
    });
    const entries = Object.entries(byR)
      .map(([k, v]) => [k, +(v.total / v.count).toFixed(1)])
      .sort((a, b) => b[1] - a[1]).slice(0, 10);
    _mkHBar("chartP_raceVsAbnLab",
      entries.map(e => e[0]), entries.map(e => e[1]), "#ffa657", {
        plugins: { tooltip: { callbacks: { label: c => ` avg ${c.raw}% labs flagged` } } },
      });
  }

  // Avg procedures per encounter type
  {
    const byType = {};
    all.forEach(d => {
      (d.encounters || []).forEach(e => {
        const t   = _encTypeLabel(e);
        const n   = (e.encounterData?.procedures || []).length;
        if (!byType[t]) byType[t] = { total: 0, count: 0 };
        byType[t].total += n; byType[t].count++;
      });
    });
    const keys = Object.keys(byType);
    const pal  = ["#4ade80", "#3fb950", "#22c55e", "#16a34a", "#15803d"];
    _mkBar("chartP_encTypeVsProcs", keys, [{
      data: keys.map(k => +(byType[k].total / byType[k].count).toFixed(1)),
      backgroundColor: keys.map((_, i) => pal[i % pal.length] + "44"),
      borderColor:     keys.map((_, i) => pal[i % pal.length]),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw} procedures` } } },
    });
  }

  // Avg medications per encounter type
  {
    const byType = {};
    all.forEach(d => {
      (d.encounters || []).forEach(e => {
        const t = _encTypeLabel(e);
        const n = (e.encounterData?.medications || []).length;
        if (!byType[t]) byType[t] = { total: 0, count: 0 };
        byType[t].total += n; byType[t].count++;
      });
    });
    const keys = Object.keys(byType);
    const pal  = ["#c084fc", "#a78bfa", "#8b5cf6", "#7c3aed", "#6d28d9"];
    _mkBar("chartP_encTypeVsMeds", keys, [{
      data: keys.map(k => +(byType[k].total / byType[k].count).toFixed(1)),
      backgroundColor: keys.map((_, i) => pal[i % pal.length] + "44"),
      borderColor:     keys.map((_, i) => pal[i % pal.length]),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw} medications` } } },
    });
  }

  // Avg labs per encounter type
  {
    const byType = {};
    all.forEach(d => {
      (d.encounters || []).forEach(e => {
        const t = _encTypeLabel(e);
        const n = (e.encounterData?.labs || []).length;
        if (!byType[t]) byType[t] = { total: 0, count: 0 };
        byType[t].total += n; byType[t].count++;
      });
    });
    const keys = Object.keys(byType);
    const pal  = ["#818cf8", "#6366f1", "#4f46e5", "#4338ca", "#3730a3"];
    _mkBar("chartP_encTypeVsLabs", keys, [{
      data: keys.map(k => +(byType[k].total / byType[k].count).toFixed(1)),
      backgroundColor: keys.map((_, i) => pal[i % pal.length] + "44"),
      borderColor:     keys.map((_, i) => pal[i % pal.length]),
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false },
        tooltip: { callbacks: { label: c => ` avg ${c.raw} labs` } } },
    });
  }

  // Inject download buttons into population chart cards
  setTimeout(_injectDownloadBtns, 0);
}

// ── ICD & Diagnosis Analysis Report ──────────────────────────────────────────

function renderICDReport(d) {
  const encounters = d.encounters || [];
  const allConds   = d.conditions || [];

  // Clear old ICD charts
  ["chartJ_icdSys", "chartJ_dxPerEnc", "chartJ_coverage", "chartJ_topDx"].forEach(id => _destroyChart(id));

  const container  = $("icdEncounterCards");
  const emptyEl    = $("icdEmpty");
  const badgeEl    = $("icdTotalBadge");
  const chipsEl    = $("icdSummaryChips");

  if (!encounters.length) {
    container.innerHTML = "";
    emptyEl.classList.remove("hidden");
    return;
  }
  emptyEl.classList.add("hidden");

  // ── Compute note coverage globally ──────────────────────────────────────────
  function _noteExcerpt(text, keyword, radius) {
    if (!text || !keyword) return "";
    const hay = text.toLowerCase();
    const idx = hay.indexOf(keyword.toLowerCase());
    if (idx < 0) return "";
    const s = Math.max(0, idx - radius);
    const e = Math.min(text.length, idx + keyword.length + radius);
    return (s > 0 ? "…" : "") + text.slice(s, e).trim() + (e < text.length ? "…" : "");
  }

  // Generic clinical stopwords to skip when matching diagnosis names to note text
  const _DX_STOPWORDS = new Set([
    "other","unspecified","specified","without","mention","personal","history",
    "disorder","condition","disease","syndrome","chronic","acute","primary",
    "secondary","multiple","single","bilateral","unilateral","benign","malignant",
    "encounter","hazards","presenting","elsewhere","classified","initial","subsequent",
    "sequela","adverse","effect","poisoning","assault","undetermined","intentional",
    "postoperative","operation","surgical","external","internal","complication",
    "following","procedure","status","presenting","visit","evaluation","management",
  ]);

  function _diagInNote(diag, noteText) {
    if (!noteText) return { found: false, keyword: null };
    const hay = noteText.toLowerCase();
    // 1. Try exact ICD code match
    if (diag.code && hay.includes(diag.code.toLowerCase())) {
      return { found: true, keyword: diag.code };
    }
    // 2. Try significant words from diagnosis name — sorted longest-first, skip stopwords
    const words = diag.name
      .replace(/[(),\/]/g, " ")
      .split(/\s+/)
      .map(w => w.toLowerCase().replace(/[^a-z]/g, ""))
      .filter(w => w.length >= 4 && !_DX_STOPWORDS.has(w));
    words.sort((a, b) => b.length - a.length);  // try longest (most specific) first
    for (const w of words) {
      if (hay.includes(w)) return { found: true, keyword: w };
    }
    // 3. Try word stem (first 5 chars) for clinical terms ≥8 chars
    for (const w of words.filter(w => w.length >= 8)) {
      const stem = w.slice(0, 6);
      if (hay.includes(stem)) return { found: true, keyword: stem };
    }
    return { found: false, keyword: null };
  }

  // Build per-encounter coverage stats
  const encStats = [];
  let totalDx = 0, totalCovered = 0;

  encounters.forEach((enc, idx) => {
    const ed    = enc.encounterData || {};
    const conds = ed.conditions || [];
    const notes = ed.notes || [];
    const allNoteText = notes.map(n => n.text || "").join("\n");

    const diagRows = conds.map(c => {
      let found = false, keyword = null, noteSnippet = "", noteRef = "";
      for (const note of notes) {
        const r = _diagInNote(c, note.text || "");
        if (r.found) {
          found       = true;
          keyword     = r.keyword;
          noteSnippet = _noteExcerpt(note.text, keyword, 80);
          noteRef     = note.typeDisplay || "Note";
          break;
        }
      }
      // Fallback: search all notes combined
      if (!found) {
        const r = _diagInNote(c, allNoteText);
        if (r.found) {
          found   = true;
          keyword = r.keyword;
          noteRef = "Combined notes";
          noteSnippet = _noteExcerpt(allNoteText, keyword, 80);
        }
      }
      return { ...c, found, keyword, noteSnippet, noteRef };
    });

    const covered = diagRows.filter(r => r.found).length;
    totalDx      += conds.length;
    totalCovered += covered;

    encStats.push({
      enc,
      idx,
      diagRows,
      covered,
      total: conds.length,
      notes,
    });
  });

  const coveragePct = totalDx > 0 ? Math.round((totalCovered / totalDx) * 100) : 0;
  const totalICD10  = allConds.filter(c => c.codeSystem === "ICD-10").length;
  const totalICD9   = allConds.filter(c => c.codeSystem === "ICD-9").length;

  // ── Summary badge + chips ───────────────────────────────────────────────────
  badgeEl.textContent = `${encounters.length} encounter${encounters.length !== 1 ? "s" : ""} · ${totalDx} diagnoses`;

  chipsEl.innerHTML = [
    ["fa-stethoscope",   "#fb7185", totalDx,         "Total Diagnoses"],
    ["fa-code-branch",   "#818cf8", totalICD10,       "ICD-10 Codes"],
    ["fa-code",          "#fbbf24", totalICD9,        "ICD-9 Codes"],
    ["fa-file-medical",  "#34d399", totalCovered,     "Found in Notes"],
    ["fa-percent",       "#38bdf8", coveragePct + "%","Note Coverage"],
  ].map(([icon, color, val, label]) => `
    <span class="enc-stat-chip">
      <i class="fas ${icon}" style="color:${color};"></i>
      <strong>${esc(String(val))}</strong> <span style="color:#8b949e;">${label}</span>
    </span>`).join("");

  // ── Overview charts ─────────────────────────────────────────────────────────

  // ICD system donut
  {
    const sys10 = allConds.filter(c => c.codeSystem === "ICD-10").length;
    const sys9  = allConds.filter(c => c.codeSystem === "ICD-9").length;
    const other = allConds.length - sys10 - sys9;
    const labels = [], data = [], colors = [];
    if (sys10) { labels.push("ICD-10"); data.push(sys10); colors.push("#818cf8"); }
    if (sys9)  { labels.push("ICD-9");  data.push(sys9);  colors.push("#fbbf24"); }
    if (other) { labels.push("Other");  data.push(other); colors.push("#484f58"); }
    if (data.length) {
      _mkDonut("chartJ_icdSys", labels, data, colors);
    }
  }

  // Diagnoses per encounter bar
  {
    const labels = encStats.map((s, i) => `#${i + 1}  ${(s.enc.start || "").slice(0, 10)}`);
    const data   = encStats.map(s => s.total);
    _mkBar("chartJ_dxPerEnc", labels, [{
      data,
      backgroundColor: "#fb718544",
      borderColor:     "#fb7185",
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: { legend: { display: false }, tooltip: { callbacks: { label: c => ` ${c.raw} diagnos${c.raw !== 1 ? "es" : "is"}` } } },
    });
  }

  // Note coverage rate per encounter
  {
    const labels = encStats.map((s, i) => `#${i + 1}`);
    const data   = encStats.map(s => s.total > 0 ? Math.round((s.covered / s.total) * 100) : 0);
    const colors = data.map(v => v >= 70 ? "#34d399" : v >= 40 ? "#fbbf24" : "#f85149");
    _mkBar("chartJ_coverage", labels, [{
      data,
      backgroundColor: colors.map(c => c + "44"),
      borderColor:     colors,
      borderWidth: 1.5, borderRadius: 3,
    }], {
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: c => ` ${c.raw}% covered` } },
      },
      scales: { y: { max: 100, ticks: { callback: v => v + "%" } } },
    });
  }

  // Top diagnoses frequency
  {
    const freq = {};
    allConds.forEach(c => { freq[c.name] = (freq[c.name] || 0) + 1; });
    const entries = _top(freq, 20);
    if (entries.length) {
      const H = Math.max(240, entries.length * 22 + 40);
      // Resize canvas container dynamically
      const canvasParent = $("chartJ_topDx")?.parentElement;
      if (canvasParent) canvasParent.style.height = H + "px";
      _mkHBar("chartJ_topDx", entries.map(e => e[0]), entries.map(e => e[1]), "#d2a8ff");
    }
  }

  // ── Per-encounter cards ─────────────────────────────────────────────────────
  container.innerHTML = encStats.map(({ enc, idx, diagRows, covered, total, notes }) => {
    const cls      = enc.cls === "IMP" ? "Inpatient" : (enc.cls === "ACUTE" ? "ICU" : enc.cls || enc.type || "Encounter");
    const covPct   = total > 0 ? Math.round((covered / total) * 100) : 0;
    const covColor = covPct >= 70 ? "#34d399" : covPct >= 40 ? "#fbbf24" : "#f85149";
    const covLabel = covPct >= 70 ? "Good" : covPct >= 40 ? "Partial" : (total > 0 ? "Low" : "—");

    // ICD table rows
    const tableRows = diagRows.length ? diagRows.map((c, ri) => {
      const sysColor  = c.codeSystem === "ICD-10" ? "#818cf8" : c.codeSystem === "ICD-9" ? "#fbbf24" : "#484f58";
      const statusCls = c.status === "active" ? "badge-rose" : "badge-inactive";
      const noteId    = `icdNote_${idx}_${ri}`;
      return `
        <tr class="icd-dx-row">
          <td class="icd-td-num">${ri + 1}</td>
          <td class="icd-td-sys">
            ${c.codeSystem
              ? `<span class="icd-sys-badge" style="color:${sysColor};border-color:${sysColor}33;">${esc(c.codeSystem)}</span>`
              : `<span class="icd-sys-badge" style="color:#484f58;">—</span>`}
          </td>
          <td class="icd-td-code">
            ${c.code ? `<code class="icd-code-chip">${esc(c.code)}</code>` : `<span style="color:#484f58;">—</span>`}
          </td>
          <td class="icd-td-name">${esc(c.name)}</td>
          <td class="icd-td-status"><span class="${statusCls}">${esc(c.status || "—")}</span></td>
          <td class="icd-td-note">
            ${c.found
              ? `<span class="icd-note-found" onclick="_toggleIcdNote('${noteId}')">
                   <i class="fas fa-check-circle" style="color:#34d399;"></i> Found
                   <i class="fas fa-chevron-down" style="font-size:0.6rem;margin-left:0.2rem;"></i>
                 </span>
                 <div id="${noteId}" class="icd-note-snippet hidden">
                   <span class="icd-note-src"><i class="fas fa-file-medical" style="color:#58a6ff;font-size:0.65rem;"></i> ${esc(c.noteRef)}</span>
                   <p class="icd-note-text">${esc(c.noteSnippet)}</p>
                 </div>`
              : `<span class="icd-note-absent"><i class="fas fa-minus-circle" style="color:#484f58;"></i> Not found</span>`}
          </td>
        </tr>`;
    }).join("") : `
        <tr>
          <td colspan="6" class="icd-td-empty">No diagnoses recorded for this encounter</td>
        </tr>`;

    // Notes summary for this encounter
    const notesSummary = notes.length
      ? notes.map(n => `
          <span class="icd-note-chip">
            <i class="fas fa-file-medical" style="color:#58a6ff;font-size:0.65rem;"></i>
            ${esc(n.typeDisplay || "Note")}
            ${n.date ? `<span style="color:#484f58;">· ${n.date}</span>` : ""}
          </span>`).join("")
      : `<span style="color:#484f58;font-size:0.8rem;">No clinical notes attached</span>`;

    return `
    <div class="icd-enc-card">
      <!-- Card header -->
      <div class="icd-enc-header" onclick="this.parentElement.querySelector('.icd-enc-body').classList.toggle('hidden'); this.querySelector('.icd-enc-chevron').classList.toggle('rotate-180')">
        <div class="badge-num-blue">${idx + 1}</div>
        <div class="min-w-0 flex-1">
          <p class="font-semibold" style="color:#cdd9e5;line-height:1.4;">
            ${esc(enc.type || cls)} Encounter
            ${total > 0 ? `<span class="enc-items-chip">${total} diagnosis${total !== 1 ? "es" : ""}</span>` : ""}
          </p>
          <p style="font-size:0.8125rem;color:#6e7681;margin-top:0.15rem;">
            <i class="fas fa-calendar-range" style="font-size:0.7rem;margin-right:0.3rem;"></i>
            ${enc.start || "?"} &nbsp;→&nbsp; ${enc.end || "ongoing"}
            ${enc.los != null ? `<span style="margin-left:0.75rem;color:#484f58;">LOS: ${enc.los}d</span>` : ""}
          </p>
        </div>
        <div class="shrink-0 flex flex-col items-end gap-1.5">
          <span class="icd-coverage-badge" style="color:${covColor};border-color:${covColor}33;background:${covColor}12;">
            <i class="fas fa-file-medical" style="font-size:0.65rem;"></i>
            ${covPct}% note coverage &nbsp;<span style="color:#484f58;">(${covLabel})</span>
          </span>
          <span class="badge-type-indigo">${esc(cls)}</span>
        </div>
        <i class="fas fa-chevron-down icd-enc-chevron text-sm ml-3 shrink-0 transition-transform duration-200"></i>
      </div>

      <!-- Card body (collapsed by default) -->
      <div class="icd-enc-body hidden">

        <!-- Clinical notes attached -->
        <div class="icd-notes-bar">
          <span style="color:#6e7681;font-size:0.8rem;font-weight:600;"><i class="fas fa-file-medical" style="color:#58a6ff;margin-right:0.3rem;"></i>Notes attached:</span>
          ${notesSummary}
        </div>

        <!-- ICD / Diagnosis table -->
        <div class="icd-table-wrap">
          <table class="icd-table">
            <thead>
              <tr>
                <th class="icd-th">#</th>
                <th class="icd-th">System</th>
                <th class="icd-th">Code</th>
                <th class="icd-th" style="min-width:200px;">Diagnosis</th>
                <th class="icd-th">Status</th>
                <th class="icd-th">In Notes?</th>
              </tr>
            </thead>
            <tbody>${tableRows}</tbody>
          </table>
        </div>

        <!-- Coverage summary row -->
        ${total > 0 ? `
        <div class="icd-coverage-row">
          <div class="icd-coverage-bar-wrap">
            <div class="icd-coverage-bar-fill" style="width:${covPct}%;background:${covColor};"></div>
          </div>
          <span style="font-size:0.8rem;color:${covColor};font-weight:600;min-width:2.5rem;">${covPct}%</span>
          <span style="font-size:0.8rem;color:#6e7681;">${covered} of ${total} diagnoses found in clinical notes</span>
        </div>` : ""}

      </div>
    </div>`;
  }).join("");
}

function _toggleIcdNote(id) {
  const el = $(id);
  if (el) el.classList.toggle("hidden");
}
