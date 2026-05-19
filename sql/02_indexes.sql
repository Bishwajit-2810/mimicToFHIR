-- MIMIC-IV Performance Indexes
-- Run AFTER data is fully loaded for maximum load speed.
-- Every table queried with WHERE subject_id = %s gets an index here.

-- ── hosp ─────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_admissions_subject        ON hosp.admissions        (subject_id);
CREATE INDEX IF NOT EXISTS idx_diagnoses_icd_subject     ON hosp.diagnoses_icd     (subject_id);
CREATE INDEX IF NOT EXISTS idx_procedures_icd_subject    ON hosp.procedures_icd    (subject_id);
CREATE INDEX IF NOT EXISTS idx_labevents_subject         ON hosp.labevents         (subject_id);
CREATE INDEX IF NOT EXISTS idx_labevents_subject_time    ON hosp.labevents         (subject_id, charttime DESC);
CREATE INDEX IF NOT EXISTS idx_prescriptions_subject     ON hosp.prescriptions     (subject_id);
CREATE INDEX IF NOT EXISTS idx_microbiologyevents_subject ON hosp.microbiologyevents (subject_id);
CREATE INDEX IF NOT EXISTS idx_omr_subject               ON hosp.omr               (subject_id);
CREATE INDEX IF NOT EXISTS idx_poe_subject               ON hosp.poe               (subject_id);
CREATE INDEX IF NOT EXISTS idx_drgcodes_subject          ON hosp.drgcodes          (subject_id);
CREATE INDEX IF NOT EXISTS idx_hcpcsevents_subject       ON hosp.hcpcsevents       (subject_id);
CREATE INDEX IF NOT EXISTS idx_emar_subject              ON hosp.emar              (subject_id);
CREATE INDEX IF NOT EXISTS idx_emar_detail_subject       ON hosp.emar_detail       (subject_id);
CREATE INDEX IF NOT EXISTS idx_pharmacy_subject          ON hosp.pharmacy          (subject_id);
CREATE INDEX IF NOT EXISTS idx_poe_detail_subject        ON hosp.poe_detail        (subject_id);
CREATE INDEX IF NOT EXISTS idx_services_subject          ON hosp.services          (subject_id);
CREATE INDEX IF NOT EXISTS idx_transfers_subject         ON hosp.transfers         (subject_id);

-- ── icu ───────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_icustays_subject          ON icu.icustays           (subject_id);
CREATE INDEX IF NOT EXISTS idx_chartevents_subject       ON icu.chartevents        (subject_id);
CREATE INDEX IF NOT EXISTS idx_chartevents_subject_item  ON icu.chartevents        (subject_id, itemid);
CREATE INDEX IF NOT EXISTS idx_datetimeevents_subject    ON icu.datetimeevents     (subject_id);
CREATE INDEX IF NOT EXISTS idx_inputevents_subject       ON icu.inputevents        (subject_id);
CREATE INDEX IF NOT EXISTS idx_ingredientevents_subject  ON icu.ingredientevents   (subject_id);
CREATE INDEX IF NOT EXISTS idx_outputevents_subject      ON icu.outputevents       (subject_id);
CREATE INDEX IF NOT EXISTS idx_procedureevents_subject   ON icu.procedureevents    (subject_id);

-- ── ed ────────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_edstays_subject           ON ed.edstays             (subject_id);
CREATE INDEX IF NOT EXISTS idx_ed_diagnosis_subject      ON ed.diagnosis           (subject_id);
CREATE INDEX IF NOT EXISTS idx_ed_triage_subject         ON ed.triage              (subject_id);
CREATE INDEX IF NOT EXISTS idx_ed_vitalsign_subject      ON ed.vitalsign           (subject_id);
CREATE INDEX IF NOT EXISTS idx_ed_medrecon_subject       ON ed.medrecon            (subject_id);
CREATE INDEX IF NOT EXISTS idx_ed_pyxis_subject          ON ed.pyxis               (subject_id);

-- ── note ─────────────────────────────────────────────────────────────────────
CREATE INDEX IF NOT EXISTS idx_discharge_subject         ON note.discharge         (subject_id);
CREATE INDEX IF NOT EXISTS idx_discharge_note_id         ON note.discharge_detail  (note_id);
CREATE INDEX IF NOT EXISTS idx_radiology_subject         ON note.radiology         (subject_id);
CREATE INDEX IF NOT EXISTS idx_radiology_note_id         ON note.radiology_detail  (note_id);
