"use strict";

// ── State ─────────────────────────────────────────────────────────────────────
let currentMode = "golddata";
let gdData = null;
let stdData = null;
let cmpData = null;

// ── DOM helpers ───────────────────────────────────────────────────────────────
const $ = id => document.getElementById(id);
const esc = s => {
  if (s == null) return "";
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
};

// ── Bootstrap ─────────────────────────────────────────────────────────────────
(async () => {
  await Promise.all([
    loadPatientList("golddata", $("gdPatientSelect")),
    loadPatientList("standard", $("stdPatientSelect")),
    loadPatientList("compare", $("cmpPatientSelect")),
    refreshStatus(),
  ]);

  $("gdPatientSelect").addEventListener("change", e => loadGdPatient(e.target.value));
  $("stdPatientSelect").addEventListener("change", e => loadStdPatient(e.target.value));
  $("cmpPatientSelect").addEventListener("change", e => loadCompare(e.target.value));
  $("gdLabSearch").addEventListener("input", e => filterTable("gdLabsBody", e.target.value));

  // Mode buttons
  document.querySelectorAll(".mode-btn").forEach(btn =>
    btn.addEventListener("click", () => setMode(btn.dataset.mode))
  );

  // GoldData tabs
  document.querySelectorAll("[data-gdtab]").forEach(btn =>
    btn.addEventListener("click", () => activateGdTab(btn.dataset.gdtab))
  );

  // Standard tabs
  document.querySelectorAll("[data-stdtab]").forEach(btn =>
    btn.addEventListener("click", () => activateStdTab(btn.dataset.stdtab))
  );

  // Auto-refresh pipeline status every 5s
  setInterval(refreshStatus, 5000);
})();

// ── Mode switching ────────────────────────────────────────────────────────────
function setMode(mode) {
  currentMode = mode;
  document.querySelectorAll(".mode-btn").forEach(b =>
    b.classList.toggle("active", b.dataset.mode === mode)
  );
  document.querySelectorAll(".mode-panel").forEach(p =>
    p.classList.toggle("hidden", p.id !== `panel-${mode}`)
  );
  $("blindedNotice").classList.toggle("hidden", mode !== "golddata");
}

// ── Tab switching ─────────────────────────────────────────────────────────────
function activateGdTab(name) {
  document.querySelectorAll("[data-gdtab]").forEach(b =>
    b.classList.toggle("active", b.dataset.gdtab === name)
  );
  document.querySelectorAll(".gd-tab-pane").forEach(p =>
    p.classList.toggle("hidden", p.id !== name)
  );
}

function activateStdTab(name) {
  document.querySelectorAll("[data-stdtab]").forEach(b =>
    b.classList.toggle("active", b.dataset.stdtab === name)
  );
  document.querySelectorAll(".std-tab-pane").forEach(p =>
    p.classList.toggle("hidden", p.id !== name)
  );
}

// ── Patient list loading ───────────────────────────────────────────────────────
async function loadPatientList(source, selectEl) {
  try {
    const endpoint = source === "compare"
      ? "/api/golddata/patients"  // compare uses golddata list as canonical
      : `/api/${source}/patients`;
    const res = await fetch(endpoint);
    const data = await res.json();
    data.patients.forEach(id => {
      const opt = document.createElement("option");
      opt.value = id;
      opt.textContent = `Patient ${id}`;
      opt.style.backgroundColor = "#1a1f27";
      opt.style.color = "#e6edf3";
      selectEl.appendChild(opt);
    });
  } catch (err) {
    console.warn(`Failed to load ${source} patient list:`, err);
  }
}

// ── GoldData patient loading ──────────────────────────────────────────────────
async function loadGdPatient(id) {
  if (!id) { showGdEmpty(); return; }
  showGdLoading();
  try {
    const res = await fetch(`/api/golddata/patients/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    gdData = await res.json();
    renderGolddata(gdData);
    showGdDashboard();
    activateGdTab("gd-overview");
    updateBlindedNotice(gdData);
  } catch (err) {
    alert("Error loading GoldData patient: " + err.message);
    showGdEmpty();
  }
}

function showGdEmpty()     { $("gdEmpty").classList.remove("hidden"); $("gdLoading").classList.add("hidden"); $("gdDashboard").classList.add("hidden"); $("gdPatientInfoBar").classList.add("hidden"); }
function showGdLoading()   { $("gdLoading").classList.remove("hidden"); $("gdEmpty").classList.add("hidden"); $("gdDashboard").classList.add("hidden"); }
function showGdDashboard() { $("gdLoading").classList.add("hidden"); $("gdEmpty").classList.add("hidden"); $("gdDashboard").classList.remove("hidden"); $("gdPatientInfoBar").classList.remove("hidden"); }

// ── Standard patient loading ──────────────────────────────────────────────────
async function loadStdPatient(id) {
  if (!id) { showStdEmpty(); return; }
  showStdLoading();
  try {
    const res = await fetch(`/api/standard/patients/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    stdData = await res.json();
    renderStandard(stdData);
    showStdDashboard();
    activateStdTab("std-overview");
  } catch (err) {
    alert("Error loading Standard patient: " + err.message);
    showStdEmpty();
  }
}

function showStdEmpty()     { $("stdEmpty").classList.remove("hidden"); $("stdLoading").classList.add("hidden"); $("stdDashboard").classList.add("hidden"); $("stdPatientInfoBar").classList.add("hidden"); }
function showStdLoading()   { $("stdLoading").classList.remove("hidden"); $("stdEmpty").classList.add("hidden"); $("stdDashboard").classList.add("hidden"); }
function showStdDashboard() { $("stdLoading").classList.add("hidden"); $("stdEmpty").classList.add("hidden"); $("stdDashboard").classList.remove("hidden"); $("stdPatientInfoBar").classList.remove("hidden"); }

// ── Compare loading ───────────────────────────────────────────────────────────
async function loadCompare(id) {
  if (!id) { showCmpEmpty(); return; }
  showCmpLoading();
  try {
    const res = await fetch(`/api/compare/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    cmpData = await res.json();
    renderCompare(cmpData);
    showCmpDashboard();
  } catch (err) {
    alert("Error loading comparison: " + err.message);
    showCmpEmpty();
  }
}

function showCmpEmpty()     { $("cmpEmpty").classList.remove("hidden"); $("cmpLoading").classList.add("hidden"); $("cmpDashboard").classList.add("hidden"); }
function showCmpLoading()   { $("cmpLoading").classList.remove("hidden"); $("cmpEmpty").classList.add("hidden"); $("cmpDashboard").classList.add("hidden"); }
function showCmpDashboard() { $("cmpLoading").classList.add("hidden"); $("cmpEmpty").classList.add("hidden"); $("cmpDashboard").classList.remove("hidden"); }

// ── Status refresh ────────────────────────────────────────────────────────────
async function refreshStatus() {
  try {
    const res = await fetch("/api/status");
    const data = await res.json();
    const std = data.standard_fhir;
    const gd  = data.golddata_fhir;
    const pp  = data.pipelines;

    $("stdCount").textContent = std.bundleCount;
    $("gdCount").textContent  = gd.bundleCount;

    updatePipelineDot($("stdDot"), pp.standard?.state);
    updatePipelineDot($("gdDot"),  pp.golddata?.state);

    const stdBtn = $("btnRunStandard");
    const gdBtn  = $("btnRunGolddata");
    if (pp.standard?.state === "running") {
      stdBtn.disabled = true;
      stdBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-1"></i>Running…';
    } else {
      stdBtn.disabled = false;
      stdBtn.innerHTML = '<i class="fas fa-play mr-1"></i>Run';
    }
    if (pp.golddata?.state === "running") {
      gdBtn.disabled = true;
      gdBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-1"></i>Running…';
    } else {
      gdBtn.disabled = false;
      gdBtn.innerHTML = '<i class="fas fa-play mr-1"></i>Run';
    }
  } catch (err) {
    // silent — status bar is best-effort
  }
}

function updatePipelineDot(el, state) {
  el.className = "pipeline-dot" + (el.classList.contains("gold") ? " gold" : "");
  if (state === "running") el.classList.add("running");
}

async function runPipeline(name) {
  try {
    const res = await fetch(`/api/run/${name}`, { method: "POST" });
    const data = await res.json();
    if (!res.ok) {
      alert(`Cannot start ${name} pipeline: ${data.detail || JSON.stringify(data)}`);
    } else {
      await refreshStatus();
    }
  } catch (err) {
    alert("Failed to start pipeline: " + err.message);
  }
}

// ── Pipeline log toggle ───────────────────────────────────────────────────────
let _logVisible = false;

function togglePipelineLog() {
  _logVisible = !_logVisible;
  $("pipelineLog").classList.toggle("hidden", !_logVisible);
  $("logToggleLabel").textContent = _logVisible ? "Hide Log" : "Show Log";
  if (_logVisible) refreshPipelineLog();
}

async function refreshPipelineLog() {
  try {
    const res = await fetch("/api/run/status");
    const data = await res.json();
    const allLog = [
      ...(data.standard?.log || []).map(l => `[standard] ${l}`),
      ...(data.golddata?.log || []).map(l => `[golddata] ${l}`),
    ];
    $("pipelineLogText").textContent = allLog.length
      ? allLog.join("\n")
      : "(no output yet)";
  } catch (err) {
    $("pipelineLogText").textContent = "Error fetching log: " + err.message;
  }
}

// ── Blinded notice ────────────────────────────────────────────────────────────
function updateBlindedNotice(d) {
  const hadm = d?.blindedHadm || d?.demographics?.goldataLatestHadm;
  if (hadm) {
    $("blindedNoticeText").textContent =
      `Diagnoses excluded for latest encounter (hadm_id: ${hadm}) — clinical outcome data withheld.`;
  }
}

// ── GoldData render ───────────────────────────────────────────────────────────
function renderGolddata(d) {
  const demo = d.demographics || {};
  $("gdPiName").textContent     = `Patient ${demo.subjectId}`;
  $("gdPiGenderAge").textContent = `${demo.gender || ""}${demo.age != null ? ", ~" + demo.age + " yrs" : ""}`;

  // Demographics grid
  renderDemoGrid("gdDemoContent", demo);

  // Exclusion card
  renderExclusionCard(d);

  // Vitals (overview)
  renderVitalsGrid("gdVitalsContent", d.vitals || []);
  renderVitalsGrid("gdAllVitals", d.vitals || []);
  $("gdVitalCount").textContent = (d.vitals || []).length;

  // Conditions (historical only)
  const conds = d.conditions || [];
  $("gdCondCount").textContent = conds.length;
  renderCondList("gdCondsContent", conds);
  $("gdCondsEmpty").classList.toggle("hidden", conds.length > 0);

  // Medications
  const meds = d.medications || [];
  $("gdMedCount").textContent  = meds.length;
  $("gdMedCount2").textContent = meds.length;
  renderMedList("gdMedsContent", meds);
  renderMedList("gdAllMeds", meds);

  // Labs
  const labs = d.labs || [];
  $("gdLabCount").textContent = labs.length;
  renderLabsTable("gdLabsBody", labs);
  $("gdLabsEmpty").classList.toggle("hidden", labs.length > 0);

  // Procedures
  const procs = d.procedures || [];
  $("gdProcCount").textContent = procs.length;
  renderProcList("gdProcsContent", procs);
  $("gdProcsEmpty").classList.toggle("hidden", procs.length > 0);

  // Encounters
  const encs = d.encounters || [];
  $("gdEncTotal").textContent = `${encs.length} encounter${encs.length !== 1 ? "s" : ""}`;
  renderEncounterList("gdEncountersContent", encs, "golddata");
  $("gdEncountersEmpty").classList.toggle("hidden", encs.length > 0);
}

function renderExclusionCard(d) {
  const el = $("gdExclusionContent");
  const hadm = d.blindedHadm || d.demographics?.goldataLatestHadm;
  const stdCounts = d.resourceCounts || {};
  const items = [
    { icon: "fa-eye-slash", color: "text-amber-400", label: "Diagnoses excluded", value: "(latest encounter)" },
    { icon: "fa-eye-slash", color: "text-amber-400", label: "Discharge disposition", value: "withheld (latest enc)" },
    { icon: "fa-check-circle", color: "text-green-400", label: "Vitals included", value: `${(d.vitals || []).length} items` },
    { icon: "fa-check-circle", color: "text-green-400", label: "Lab results included", value: `${(d.labs || []).length} items` },
    { icon: "fa-check-circle", color: "text-green-400", label: "Medications included", value: `${(d.medications || []).length} items` },
    { icon: "fa-check-circle", color: "text-green-400", label: "Procedures included", value: `${(d.procedures || []).length} items` },
  ];
  if (hadm) {
    el.innerHTML = `<p class="text-xs text-amber-300/80 mb-3 font-mono">Blinded encounter: hadm_id ${hadm}</p>` +
      items.map(it => `
        <div class="flex items-center justify-between">
          <span class="flex items-center gap-2 ${it.color}">
            <i class="fas ${it.icon} text-xs"></i>
            <span class="text-gray-300">${esc(it.label)}</span>
          </span>
          <span class="text-gray-500 text-xs">${esc(it.value)}</span>
        </div>`).join("");
  } else {
    el.innerHTML = `<p class="text-gray-500 text-xs">No blinded encounter metadata found.</p>`;
  }
}

// ── Standard render ───────────────────────────────────────────────────────────
function renderStandard(d) {
  const demo = d.demographics || {};
  $("stdPiName").textContent      = `Patient ${demo.subjectId}`;
  $("stdPiGenderAge").textContent = `${demo.gender || ""}${demo.age != null ? ", ~" + demo.age + " yrs" : ""}`;

  renderDemoGrid("stdDemoContent", demo);
  renderVitalsGrid("stdVitalsContent", d.vitals || []);

  const meds = d.medications || [];
  $("stdMedCount").textContent = meds.length;
  renderMedList("stdMedsContent", meds);

  const conds = d.conditions || [];
  $("stdCondCount").textContent    = conds.length;
  $("stdAllCondCount").textContent = conds.length;
  renderCondList("stdCondsContent", conds);
  renderCondList("stdAllCondsContent", conds);

  const labs = d.labs || [];
  $("stdLabCount").textContent = labs.length;
  renderLabsTable("stdLabsBody", labs);

  renderEncounterList("stdEncountersContent", d.encounters || [], "standard");
}

// ── Compare render ────────────────────────────────────────────────────────────
function renderCompare(d) {
  // Diff summary
  const diff = d.diff || {};
  const rc   = diff.resourceCountDiff || {};
  $("cmpDiffSummary").innerHTML = `
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-sm">
      ${Object.entries(rc).map(([k, v]) => `
        <div class="diff-count-card">
          <span class="text-gray-500 text-xs uppercase tracking-wide">${esc(k)}</span>
          <div class="flex gap-3 mt-1">
            <span class="text-blue-400 font-mono">${v.standard}</span>
            <span class="text-gray-600">vs</span>
            <span class="text-amber-400 font-mono">${v.golddata}</span>
          </div>
        </div>`).join("")}
    </div>
    <div class="mt-4 flex flex-wrap gap-3 text-xs">
      <span class="cmp-stat-badge blue">
        <i class="fas fa-circle-dot mr-1"></i>Standard conditions: ${d.standard?.conditions?.length ?? "—"}
      </span>
      <span class="cmp-stat-badge amber">
        <i class="fas fa-eye-slash mr-1"></i>GoldData conditions: ${d.golddata?.conditions?.length ?? "—"}
      </span>
      <span class="cmp-stat-badge rose">
        <i class="fas fa-minus-circle mr-1"></i>Excluded in GoldData: ${diff.conditionsOnlyInStandard ?? "—"}
      </span>
    </div>
  `;

  // Standard side
  renderSideSummary("cmpStdContent", d.standard, "standard");
  // GoldData side
  renderSideSummary("cmpGdContent", d.golddata, "golddata");

  // Condition diff
  renderConditionDiff("cmpCondDiff", d.standard, d.golddata);

  // Vitals side-by-side
  renderVitalsGrid("cmpStdVitals", d.standard?.vitals || []);
  renderVitalsGrid("cmpGdVitals", d.golddata?.vitals || []);
}

function renderSideSummary(elId, data, source) {
  if (!data) {
    $(elId).innerHTML = `<p class="text-gray-600 text-sm">No ${source} bundle available for this patient.</p>`;
    return;
  }
  const rc = data.resourceCounts || {};
  const demo = data.demographics || {};
  const color = source === "golddata" ? "text-amber-400" : "text-blue-400";
  $(elId).innerHTML = `
    <div class="grid grid-cols-2 gap-2 text-sm">
      ${[
        ["Patient",    `${demo.gender || "—"}, ${demo.age != null ? "~" + demo.age + " yrs" : "—"}`],
        ["Encounters", rc.encounters ?? 0],
        ["Conditions", rc.conditions ?? 0],
        ["Observations", rc.observations ?? 0],
        ["Medications",  rc.medications ?? 0],
        ["Procedures",   rc.procedures ?? 0],
        ["DiagReports",  rc.diagnosticReports ?? 0],
      ].map(([lbl, val]) => `
        <span class="text-gray-500">${esc(lbl)}</span>
        <span class="${color} font-mono">${esc(String(val))}</span>
      `).join("")}
    </div>
    ${source === "golddata" && data.blindedHadm ? `
      <div class="mt-3 pt-3 border-t border-gray-700/50 text-xs text-amber-300/70">
        <i class="fas fa-eye-slash mr-1"></i>Blinded hadm_id: ${data.blindedHadm}
      </div>` : ""}
  `;
}

function renderConditionDiff(elId, stdData, gdData) {
  if (!stdData && !gdData) {
    $(elId).innerHTML = `<p class="text-gray-600 text-sm">No data available for comparison.</p>`;
    return;
  }

  const stdConds = stdData?.conditions || [];
  const gdConds  = gdData?.conditions  || [];
  const gdCodes  = new Set(gdConds.map(c => c.code).filter(Boolean));

  const onlyInStd = stdConds.filter(c => c.code && !gdCodes.has(c.code));
  const inBoth    = stdConds.filter(c => c.code &&  gdCodes.has(c.code));

  $(elId).innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 text-sm">
      <div>
        <h4 class="text-rose-400 font-medium mb-2 flex items-center gap-2">
          <i class="fas fa-eye-slash text-xs"></i>
          Excluded from GoldData (${onlyInStd.length})
        </h4>
        ${onlyInStd.length ? `
          <div class="space-y-1 max-h-64 overflow-y-auto">
            ${onlyInStd.map(c => `
              <div class="diff-cond-row excluded">
                <span class="text-gray-300">${esc(c.name)}</span>
                ${c.code ? `<span class="text-xs font-mono text-gray-600">${esc(c.codeSystem)} ${esc(c.code)}</span>` : ""}
              </div>`).join("")}
          </div>` : `<p class="text-gray-600">None — golddata has all standard conditions.</p>`}
      </div>
      <div>
        <h4 class="text-green-400 font-medium mb-2 flex items-center gap-2">
          <i class="fas fa-check text-xs"></i>
          Present in Both (${inBoth.length})
        </h4>
        ${inBoth.length ? `
          <div class="space-y-1 max-h-64 overflow-y-auto">
            ${inBoth.map(c => `
              <div class="diff-cond-row shared">
                <span class="text-gray-300">${esc(c.name)}</span>
                ${c.code ? `<span class="text-xs font-mono text-gray-600">${esc(c.codeSystem)} ${esc(c.code)}</span>` : ""}
              </div>`).join("")}
          </div>` : `<p class="text-gray-600">No shared conditions.</p>`}
      </div>
    </div>
  `;
}

// ── Shared component renderers ────────────────────────────────────────────────

function renderDemoGrid(elId, demo) {
  const fields = [
    ["Patient ID",    demo.subjectId],
    ["Gender",        demo.gender],
    ["Birth Date",    demo.birthDate || "—"],
    ["Age (approx.)", demo.age != null ? demo.age + " yrs" : "—"],
    ["Race",          demo.race],
    ["Ethnicity",     demo.ethnicity],
    ["Marital",       demo.maritalStatus || "—"],
    ["Language",      demo.language || "—"],
    ["Deceased",      demo.deceased || "No"],
  ];
  $(elId).innerHTML = fields.map(([lbl, val]) => `
    <div>
      <div class="text-gray-500 text-xs mb-0.5">${esc(lbl)}</div>
      <div class="text-gray-200 font-medium text-sm truncate">${esc(val)}</div>
    </div>`).join("");
}

function renderVitalsGrid(elId, vitals) {
  const el = $(elId);
  if (!vitals.length) {
    el.innerHTML = `<p class="col-span-full text-sm text-gray-600 py-2">No vitals recorded.</p>`;
    return;
  }
  el.innerHTML = vitals.map(v => {
    const valStr = typeof v.value === "number" ? v.value.toFixed(1) : v.value;
    const nr     = v.normalRange;
    const vc     = v.status === "abnormal" ? "#f85149" : "#79c0ff";
    const rangeStr = nr ? `<span class="text-[10px]" style="color:#484f58;">${nr[0]}–${nr[1]}</span>` : "";
    return `
      <div class="gd-vital-card ${v.status}">
        <i class="fas ${v.icon} text-base" style="color:${vc};"></i>
        <span class="text-xs mt-1 text-gray-500">${esc(v.name)}</span>
        <span class="font-bold text-base leading-tight" style="color:${vc};">
          ${esc(String(valStr))}
          <span class="text-xs font-normal text-gray-600">${esc(v.unit)}</span>
        </span>
        ${rangeStr}
        <span class="text-[10px] text-gray-600">${v.time || ""}</span>
      </div>`;
  }).join("");
}

function renderCondList(elId, conds) {
  const el = $(elId);
  if (!conds.length) return;
  el.innerHTML = conds.map(c => `
    <div class="gd-list-row">
      <i class="fas fa-circle-dot text-xs shrink-0 mt-0.5 text-teal-500"></i>
      <div class="min-w-0">
        <p class="text-gray-200 font-medium truncate">${esc(c.name)}</p>
        ${c.code ? `<p class="text-xs font-mono text-gray-600">${esc(c.codeSystem)} ${esc(c.code)}</p>` : ""}
      </div>
      <span class="ml-auto shrink-0 ${c.status === "active" ? "badge-teal" : "badge-inactive"}">${esc(c.status)}</span>
    </div>`).join("");
}

function renderMedList(elId, meds) {
  const el = $(elId);
  if (!meds.length) {
    el.innerHTML = `<div class="gd-list-row text-gray-600">No medications recorded.</div>`;
    return;
  }
  el.innerHTML = meds.map(m => `
    <div class="gd-list-row">
      <i class="fas fa-capsules shrink-0 mt-0.5 text-violet-400"></i>
      <div class="min-w-0">
        <p class="text-gray-200 font-medium truncate">${esc(m.name)}</p>
        <p class="text-xs text-gray-600">
          ${m.dose ? esc(m.dose) : ""}${m.route ? " · " + esc(m.route) : ""}
          ${m.start ? " · " + m.start : ""}
        </p>
      </div>
      <span class="ml-auto shrink-0 ${m.status === "completed" ? "badge-completed" : "badge-inactive"}">${esc(m.status)}</span>
    </div>`).join("");
}

function renderProcList(elId, procs) {
  const el = $(elId);
  if (!procs.length) return;
  el.innerHTML = procs.map(p => `
    <div class="gd-list-row">
      <i class="fas fa-syringe shrink-0 mt-0.5 text-emerald-400"></i>
      <div class="min-w-0">
        <p class="text-gray-200 font-medium truncate">${esc(p.name)}</p>
        ${p.time ? `<p class="text-xs text-gray-600">${p.time}</p>` : ""}
      </div>
      <span class="ml-auto shrink-0 badge-completed">${esc(p.status)}</span>
    </div>`).join("");
}

function renderLabsTable(tbodyId, labs) {
  const tbody = $(tbodyId);
  if (!labs.length) return;
  tbody.innerHTML = labs.map(l => {
    const flagClass = l.flag ? `flag-${l.flag}` : "";
    const flagIcon  = { H: "↑", L: "↓", HH: "↑↑", LL: "↓↓", A: "!" }[l.flag] || l.flag || "";
    const refStr    = (l.refLow != null && l.refHigh != null)
      ? `${l.refLow} – ${l.refHigh}` : "—";
    const valStr    = typeof l.value === "number" ? l.value.toFixed(2) : (l.value ?? "—");
    return `
      <tr class="gd-lab-row" data-name="${esc((l.name || "").toLowerCase())}">
        <td class="px-4 py-2 font-medium text-gray-200">${esc(l.name)}</td>
        <td class="px-4 py-2 text-right font-mono font-semibold ${flagClass}">
          ${esc(String(valStr))}
          <span class="text-xs ml-1 text-gray-600">${esc(l.unit)}</span>
        </td>
        <td class="px-4 py-2 text-center ${flagClass}">${flagIcon}</td>
        <td class="px-4 py-2 text-center text-xs font-mono text-gray-600 hidden sm:table-cell">${refStr}</td>
        <td class="px-4 py-2 text-xs text-gray-600 hidden md:table-cell">${l.time || "—"}</td>
      </tr>`;
  }).join("");
}

function renderEncounterList(elId, encs, source) {
  const el = $(elId);
  if (!encs.length) return;
  const isGold = source === "golddata";
  el.innerHTML = encs.map((enc, i) => {
    const isBlinded = isGold && enc.blinded;
    const borderCls = isBlinded ? "border-amber-700/50" : "border-gray-700/50";
    const data = enc.encounterData || {};
    return `
      <div class="gd-enc-card ${borderCls}">
        <div class="gd-enc-header" onclick="toggleEncSection('enc-${source}-${i}')">
          <div class="flex items-center gap-3 min-w-0">
            <i class="fas fa-hospital text-xs ${isBlinded ? "text-amber-400" : "text-blue-400"}"></i>
            <div class="min-w-0">
              <p class="text-gray-200 font-medium text-sm">
                ${esc(enc.type || enc.cls || "Encounter")}
                ${isBlinded ? `<span class="ml-2 text-[10px] bg-amber-900/40 text-amber-400 border border-amber-700/50 px-1.5 py-0.5 rounded">dx-blind</span>` : ""}
              </p>
              <p class="text-gray-600 text-xs">${esc(enc.start || "—")} → ${esc(enc.end || "ongoing")}</p>
            </div>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            ${data.conditions?.length ? `<span class="text-xs text-teal-500">${data.conditions.length} dx</span>` : ""}
            ${data.vitals?.length ? `<span class="text-xs text-red-400">${data.vitals.length} vitals</span>` : ""}
            <i class="fas fa-chevron-down text-gray-600 text-xs enc-chevron" id="chevron-enc-${source}-${i}"></i>
          </div>
        </div>
        <div id="enc-${source}-${i}" class="hidden gd-enc-body">
          ${isBlinded ? `
            <div class="mb-3 p-2.5 bg-amber-900/20 border border-amber-700/30 rounded text-xs text-amber-300 flex items-center gap-2">
              <i class="fas fa-eye-slash"></i>
              Diagnoses withheld for this encounter (golddata_fhir evaluation mode)
            </div>` : ""}
          ${data.conditions?.length ? `
            <div class="mb-3">
              <h5 class="text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide">Diagnoses</h5>
              ${data.conditions.map(c => `
                <div class="flex gap-2 text-sm py-0.5">
                  <i class="fas fa-circle-dot text-xs text-teal-600 mt-0.5 shrink-0"></i>
                  <span class="text-gray-300">${esc(c.name)}</span>
                </div>`).join("")}
            </div>` : ""}
          ${data.vitals?.length ? `
            <div class="mb-3">
              <h5 class="text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide">Vitals</h5>
              <div class="grid grid-cols-3 sm:grid-cols-4 gap-2">
                ${data.vitals.slice(0, 8).map(v => `
                  <div class="text-xs bg-gray-800/50 rounded p-1.5">
                    <div class="text-gray-500">${esc(v.name)}</div>
                    <div class="text-gray-200 font-mono">${v.value} <span class="text-gray-600">${esc(v.unit)}</span></div>
                  </div>`).join("")}
              </div>
            </div>` : ""}
          ${data.medications?.length ? `
            <div class="mb-3">
              <h5 class="text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide">Medications (${data.medications.length})</h5>
              <div class="space-y-0.5">
                ${data.medications.slice(0, 5).map(m => `
                  <div class="text-xs text-gray-400">${esc(m.name)} ${m.dose ? "· " + esc(m.dose) : ""}</div>`).join("")}
                ${data.medications.length > 5 ? `<div class="text-xs text-gray-600">+ ${data.medications.length - 5} more…</div>` : ""}
              </div>
            </div>` : ""}
          ${enc.children?.length ? `
            <div>
              <h5 class="text-xs font-medium text-gray-500 mb-1 uppercase tracking-wide">ICU Stays (${enc.children.length})</h5>
              ${enc.children.map(icu => `
                <div class="text-xs bg-gray-800/40 rounded p-2 mb-1">
                  <span class="text-sky-400">${esc(icu.location || "ICU")}</span>
                  <span class="text-gray-600 ml-2">${esc(icu.start || "—")} → ${esc(icu.end || "ongoing")}</span>
                  ${icu.los != null ? `<span class="text-gray-600 ml-2">${icu.los} days</span>` : ""}
                </div>`).join("")}
            </div>` : ""}
        </div>
      </div>`;
  }).join("");
}

function toggleEncSection(id) {
  const el = $(id);
  if (!el) return;
  el.classList.toggle("hidden");
  const chevron = $(`chevron-${id}`);
  if (chevron) chevron.classList.toggle("rotate-180");
}

// ── Shared filter ─────────────────────────────────────────────────────────────
function filterTable(tbodyId, query) {
  const q = query.toLowerCase().trim();
  const tbody = $(tbodyId);
  if (!tbody) return;
  tbody.querySelectorAll("tr").forEach(row => {
    const name = row.dataset.name || "";
    row.style.display = !q || name.includes(q) ? "" : "none";
  });
}
