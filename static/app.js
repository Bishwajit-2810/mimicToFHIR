"use strict";

// ── State ─────────────────────────────────────────────────────────────────────
let currentData = null;

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
function showEmpty() {
  emptyState.classList.remove("hidden");
  loadingState.classList.add("hidden");
  dashboard.classList.add("hidden");
  tabNav.classList.add("hidden");
  patientInfoBar.classList.add("hidden");
  $("patientBadge").classList.add("hidden");
}
function showLoading() {
  loadingState.classList.remove("hidden");
  emptyState.classList.add("hidden");
  dashboard.classList.add("hidden");
  tabNav.classList.add("hidden");
}
function showDashboard() {
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
    : d.conditions.slice(0, 5);

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
  const total = encounters.reduce((n, e) => n + 1 + e.children.length, 0);
  $("encTotal").textContent = `${total} encounter${total !== 1 ? "s" : ""}`;

  const el = $("encountersContent");
  if (!encounters.length) {
    $("encountersEmpty").classList.remove("hidden");
    return;
  }

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

    return `
    <div class="enc-card">
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

  const dxLines = conditions.slice(0, 4).map((c, i) =>
    `<span class="enc-note-dx-item">${i + 1}. ${esc(c.name)}${c.code ? ` <span class="enc-note-code">(${esc(c.code)})</span>` : ""}</span>`
  ).join("");
  const moreDx = conditions.length > 4
    ? `<span class="enc-note-dx-item enc-note-more">+${conditions.length - 4} more diagnoses</span>`
    : "";

  const medLines = activeMeds.slice(0, 4).map(m =>
    `<span class="enc-note-med-item">
      <i class="fas fa-circle" style="color:#c084fc;font-size:0.45rem;margin-top:0.35rem;flex-shrink:0;"></i>
      ${esc(m.name)}${m.dose ? ` — <span style="color:#6e7681;">${esc(m.dose)}</span>` : ""}
     </span>`
  ).join("");
  const moreMeds = activeMeds.length > 4
    ? `<span class="enc-note-med-item" style="color:#484f58;">+${activeMeds.length - 4} more medications</span>`
    : "";

  let labSummary = `${labs.length} total`;
  if (abnormalLabs.length) labSummary += `, <span style="color:#f85149;font-weight:600;">${abnormalLabs.length} abnormal</span>`;
  if (criticalLabs.length) {
    const critNames = criticalLabs.slice(0, 2).map(l => esc(l.name)).join(", ");
    labSummary += ` — critical: <span style="color:#f85149;">${critNames}${criticalLabs.length > 2 ? ` +${criticalLabs.length - 2} more` : ""}</span>`;
  }

  const procLines = procedures.slice(0, 3).map(p =>
    `<span class="enc-note-proc-item">
      <i class="fas fa-circle" style="color:#4ade80;font-size:0.45rem;margin-top:0.35rem;flex-shrink:0;"></i>
      ${esc(p.name)}
     </span>`
  ).join("");

  const rptLines = reports.slice(0, 4).map(r =>
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
  const moreRpts = reports.length > 4
    ? `<span class="enc-note-rpt-item" style="color:#484f58;">+${reports.length - 4} more reports</span>`
    : "";

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
        <div class="enc-note-dx-list">${dxLines}${moreDx}</div>
      </div>` : ""}

      ${activeMeds.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-pills" style="color:#c084fc;"></i> Active Medications (${activeMeds.length})</div>
        <div class="enc-note-med-list">${medLines}${moreMeds}</div>
      </div>` : ""}

      ${labs.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-flask-vial" style="color:#818cf8;"></i> Lab Findings</div>
        <div class="enc-note-text">${labSummary}</div>
      </div>` : ""}

      ${reports.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-vial-circle-check" style="color:#38bdf8;"></i> Microbiology / Reports (${reports.length})</div>
        <div class="enc-note-rpt-list">${rptLines}${moreRpts}</div>
      </div>` : ""}

      ${procedures.length ? `
      <div class="enc-note-section">
        <div class="enc-note-label"><i class="fas fa-syringe" style="color:#4ade80;"></i> Procedures (${procedures.length})</div>
        <div class="enc-note-proc-list">${procLines}${procedures.length > 3 ? `<span class="enc-note-proc-item" style="color:#484f58;">+${procedures.length - 3} more</span>` : ""}</div>
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
  const body    = header.nextElementSibling;
  const chevron = header.querySelector(".enc-chevron");
  const open    = !body.classList.contains("hidden");
  body.classList.toggle("hidden", open);
  chevron.style.transform = open ? "" : "rotate(180deg)";
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
