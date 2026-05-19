-- MIMIC-IV Schema (supports v2.2 demo and v3.1 full dataset)
-- Modules: hosp (hospital), icu (intensive care unit), note (clinical notes)

CREATE SCHEMA IF NOT EXISTS hosp;
CREATE SCHEMA IF NOT EXISTS icu;
CREATE SCHEMA IF NOT EXISTS note;
CREATE SCHEMA IF NOT EXISTS ed;

-- ============================================================
-- HOSP MODULE
-- ============================================================

CREATE TABLE hosp.patients (
    subject_id        INTEGER NOT NULL,
    gender            VARCHAR(1),
    anchor_age        SMALLINT,
    anchor_year       SMALLINT,
    anchor_year_group VARCHAR(20),
    dod               DATE,
    PRIMARY KEY (subject_id)
);

CREATE TABLE hosp.admissions (
    subject_id          INTEGER NOT NULL,
    hadm_id             INTEGER NOT NULL,
    admittime           TIMESTAMP NOT NULL,
    dischtime           TIMESTAMP,
    deathtime           TIMESTAMP,
    admission_type      VARCHAR(50),
    admit_provider_id   VARCHAR(10),
    admission_location  VARCHAR(60),
    discharge_location  VARCHAR(60),
    insurance           VARCHAR(30),
    language            TEXT,
    marital_status      VARCHAR(30),
    race                VARCHAR(80),
    edregtime           TIMESTAMP,
    edouttime           TIMESTAMP,
    hospital_expire_flag SMALLINT,
    PRIMARY KEY (hadm_id)
);

CREATE TABLE hosp.transfers (
    subject_id  INTEGER NOT NULL,
    hadm_id     INTEGER,
    transfer_id INTEGER NOT NULL,
    eventtype   VARCHAR(20),
    careunit    VARCHAR(60),
    intime      TIMESTAMP,
    outtime     TIMESTAMP,
    PRIMARY KEY (transfer_id)
);

CREATE TABLE hosp.services (
    subject_id   INTEGER NOT NULL,
    hadm_id      INTEGER NOT NULL,
    transfertime TIMESTAMP NOT NULL,
    prev_service VARCHAR(20),
    curr_service VARCHAR(20)
);

CREATE TABLE hosp.provider (
    provider_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (provider_id)
);

-- Diagnosis dictionaries
CREATE TABLE hosp.d_icd_diagnoses (
    icd_code   VARCHAR(10) NOT NULL,
    icd_version SMALLINT NOT NULL,
    long_title  TEXT,
    PRIMARY KEY (icd_code, icd_version)
);

CREATE TABLE hosp.d_icd_procedures (
    icd_code    VARCHAR(10) NOT NULL,
    icd_version SMALLINT NOT NULL,
    long_title  TEXT,
    PRIMARY KEY (icd_code, icd_version)
);

CREATE TABLE hosp.d_hcpcs (
    code              VARCHAR(5) NOT NULL,
    category          SMALLINT,
    long_description  TEXT,
    short_description TEXT,
    PRIMARY KEY (code)
);

CREATE TABLE hosp.d_labitems (
    itemid   INTEGER NOT NULL,
    label    VARCHAR(100),
    fluid    VARCHAR(50),
    category VARCHAR(50),
    PRIMARY KEY (itemid)
);

-- Clinical events
CREATE TABLE hosp.diagnoses_icd (
    subject_id  INTEGER NOT NULL,
    hadm_id     INTEGER NOT NULL,
    seq_num     SMALLINT NOT NULL,
    icd_code    VARCHAR(10),
    icd_version SMALLINT
);

CREATE TABLE hosp.procedures_icd (
    subject_id  INTEGER NOT NULL,
    hadm_id     INTEGER NOT NULL,
    seq_num     SMALLINT NOT NULL,
    chartdate   DATE,
    icd_code    VARCHAR(10),
    icd_version SMALLINT
);

CREATE TABLE hosp.drgcodes (
    subject_id   INTEGER NOT NULL,
    hadm_id      INTEGER NOT NULL,
    drg_type     VARCHAR(10),
    drg_code     VARCHAR(10),
    description  TEXT,
    drg_severity SMALLINT,
    drg_mortality SMALLINT
);

CREATE TABLE hosp.hcpcsevents (
    subject_id        INTEGER NOT NULL,
    hadm_id           INTEGER NOT NULL,
    chartdate         DATE,
    hcpcs_cd          VARCHAR(5),
    seq_num           SMALLINT,
    short_description TEXT
);

CREATE TABLE hosp.labevents (
    labevent_id       INTEGER NOT NULL,
    subject_id        INTEGER NOT NULL,
    hadm_id           INTEGER,
    specimen_id       INTEGER,
    itemid            INTEGER,
    order_provider_id VARCHAR(10),
    charttime         TIMESTAMP,
    storetime         TIMESTAMP,
    value             TEXT,
    valuenum          DOUBLE PRECISION,
    valueuom          VARCHAR(20),
    ref_range_lower   DOUBLE PRECISION,
    ref_range_upper   DOUBLE PRECISION,
    flag              VARCHAR(10),
    priority          VARCHAR(10),
    comments          TEXT,
    PRIMARY KEY (labevent_id)
);

CREATE TABLE hosp.microbiologyevents (
    microevent_id       INTEGER NOT NULL,
    subject_id          INTEGER NOT NULL,
    hadm_id             INTEGER,
    micro_specimen_id   INTEGER,
    order_provider_id   VARCHAR(10),
    chartdate           DATE,
    charttime           TIMESTAMP,
    spec_itemid         INTEGER,
    spec_type_desc      VARCHAR(100),
    test_seq            SMALLINT,
    storedate           DATE,
    storetime           TIMESTAMP,
    test_itemid         INTEGER,
    test_name           VARCHAR(100),
    org_itemid          INTEGER,
    org_name            VARCHAR(100),
    isolate_num         SMALLINT,
    quantity            TEXT,
    ab_itemid           INTEGER,
    ab_name             VARCHAR(60),
    dilution_text       VARCHAR(10),
    dilution_comparison VARCHAR(10),
    dilution_value      DOUBLE PRECISION,
    interpretation      VARCHAR(10),
    comments            TEXT,
    PRIMARY KEY (microevent_id)
);

CREATE TABLE hosp.omr (
    subject_id   INTEGER NOT NULL,
    chartdate    DATE NOT NULL,
    seq_num      SMALLINT NOT NULL,
    result_name  VARCHAR(100),
    result_value TEXT
);

-- Medication tables
CREATE TABLE hosp.poe (
    poe_id                  VARCHAR(25) NOT NULL,
    poe_seq                 INTEGER,
    subject_id              INTEGER NOT NULL,
    hadm_id                 INTEGER,
    ordertime               TIMESTAMP,
    order_type              VARCHAR(30),
    order_subtype           VARCHAR(60),
    transaction_type        VARCHAR(20),
    discontinue_of_poe_id   VARCHAR(25),
    discontinued_by_poe_id  VARCHAR(25),
    order_provider_id       VARCHAR(10),
    order_status            VARCHAR(20),
    PRIMARY KEY (poe_id)
);

CREATE TABLE hosp.poe_detail (
    poe_id      VARCHAR(25) NOT NULL,
    poe_seq     INTEGER,
    subject_id  INTEGER NOT NULL,
    field_name  VARCHAR(100),
    field_value TEXT
);

CREATE TABLE hosp.prescriptions (
    subject_id          INTEGER NOT NULL,
    hadm_id             INTEGER NOT NULL,
    pharmacy_id         INTEGER,
    poe_id              VARCHAR(25),
    poe_seq             INTEGER,
    order_provider_id   VARCHAR(10),
    starttime           TIMESTAMP,
    stoptime            TIMESTAMP,
    drug_type           VARCHAR(20),
    drug                VARCHAR(100),
    formulary_drug_cd   VARCHAR(20),
    gsn                 TEXT,
    ndc                 VARCHAR(25),
    prod_strength       TEXT,
    form_rx             VARCHAR(20),
    dose_val_rx         VARCHAR(50),
    dose_unit_rx        VARCHAR(50),
    form_val_disp       VARCHAR(50),
    form_unit_disp      VARCHAR(50),
    doses_per_24_hrs    DOUBLE PRECISION,
    route               VARCHAR(30)
);

CREATE TABLE hosp.pharmacy (
    subject_id          INTEGER NOT NULL,
    hadm_id             INTEGER,
    pharmacy_id         INTEGER NOT NULL,
    poe_id              VARCHAR(25),
    starttime           TIMESTAMP,
    stoptime            TIMESTAMP,
    medication          TEXT,
    proc_type           VARCHAR(40),
    status              VARCHAR(60),
    entertime           TIMESTAMP,
    verifiedtime        TIMESTAMP,
    route               VARCHAR(30),
    frequency           VARCHAR(30),
    disp_sched          TEXT,
    infusion_type       VARCHAR(15),
    sliding_scale       VARCHAR(5),
    lockout_interval    VARCHAR(50),
    basal_rate          DOUBLE PRECISION,
    one_hr_max          VARCHAR(10),
    doses_per_24_hrs    DOUBLE PRECISION,
    duration            DOUBLE PRECISION,
    duration_interval   VARCHAR(20),
    expiration_value    DOUBLE PRECISION,
    expiration_unit     VARCHAR(20),
    expirationdate      TIMESTAMP,
    dispensation        VARCHAR(30),
    fill_quantity       VARCHAR(30),
    PRIMARY KEY (pharmacy_id)
);

CREATE TABLE hosp.emar (
    subject_id        INTEGER NOT NULL,
    hadm_id           INTEGER,
    emar_id           VARCHAR(25) NOT NULL,
    emar_seq          INTEGER,
    poe_id            VARCHAR(25),
    pharmacy_id       INTEGER,
    enter_provider_id VARCHAR(10),
    charttime         TIMESTAMP,
    medication        TEXT,
    event_txt         VARCHAR(100),
    scheduletime      TIMESTAMP,
    storetime         TIMESTAMP,
    PRIMARY KEY (emar_id)
);

CREATE TABLE hosp.emar_detail (
    subject_id                          INTEGER NOT NULL,
    emar_id                             VARCHAR(25) NOT NULL,
    emar_seq                            INTEGER,
    parent_field_ordinal                VARCHAR(10),
    administration_type                 VARCHAR(50),
    pharmacy_id                         INTEGER,
    barcode_type                        VARCHAR(10),
    reason_for_no_barcode               TEXT,
    complete_dose_not_given             VARCHAR(5),
    dose_due                            VARCHAR(100),
    dose_due_unit                       VARCHAR(50),
    dose_given                          VARCHAR(100),
    dose_given_unit                     VARCHAR(50),
    will_remainder_of_dose_be_given     VARCHAR(5),
    product_amount_given                VARCHAR(30),
    product_unit                        VARCHAR(30),
    product_code                        VARCHAR(30),
    product_description                 TEXT,
    product_description_other           TEXT,
    prior_infusion_rate                 VARCHAR(40),
    infusion_rate                       VARCHAR(40),
    infusion_rate_adjustment            VARCHAR(50),
    infusion_rate_adjustment_amount     VARCHAR(30),
    infusion_rate_unit                  VARCHAR(30),
    route                               VARCHAR(30),
    infusion_complete                   VARCHAR(5),
    completion_interval                 VARCHAR(30),
    new_iv_bag_hung                     VARCHAR(5),
    continued_infusion_in_other_location VARCHAR(5),
    restart_interval                    VARCHAR(30),
    side                                VARCHAR(10),
    site                                VARCHAR(60),
    non_formulary_visual_verification   VARCHAR(5)
);

-- ============================================================
-- ICU MODULE
-- ============================================================

CREATE TABLE icu.caregiver (
    caregiver_id INTEGER NOT NULL,
    PRIMARY KEY (caregiver_id)
);

CREATE TABLE icu.d_items (
    itemid          INTEGER NOT NULL,
    label           VARCHAR(100),
    abbreviation    VARCHAR(50),
    linksto         VARCHAR(30),
    category        VARCHAR(50),
    unitname        VARCHAR(50),
    param_type      VARCHAR(20),
    lownormalvalue  DOUBLE PRECISION,
    highnormalvalue DOUBLE PRECISION,
    PRIMARY KEY (itemid)
);

CREATE TABLE icu.icustays (
    subject_id      INTEGER NOT NULL,
    hadm_id         INTEGER NOT NULL,
    stay_id         INTEGER NOT NULL,
    first_careunit  VARCHAR(60),
    last_careunit   VARCHAR(60),
    intime          TIMESTAMP,
    outtime         TIMESTAMP,
    los             DOUBLE PRECISION,
    PRIMARY KEY (stay_id)
);

CREATE TABLE icu.chartevents (
    subject_id   INTEGER NOT NULL,
    hadm_id      INTEGER NOT NULL,
    stay_id      INTEGER NOT NULL,
    caregiver_id INTEGER,
    charttime    TIMESTAMP NOT NULL,
    storetime    TIMESTAMP,
    itemid       INTEGER NOT NULL,
    value        TEXT,
    valuenum     DOUBLE PRECISION,
    valueuom     VARCHAR(30),
    warning      SMALLINT
);

CREATE TABLE icu.datetimeevents (
    subject_id   INTEGER NOT NULL,
    hadm_id      INTEGER NOT NULL,
    stay_id      INTEGER NOT NULL,
    caregiver_id INTEGER,
    charttime    TIMESTAMP NOT NULL,
    storetime    TIMESTAMP,
    itemid       INTEGER NOT NULL,
    value        TIMESTAMP,
    valueuom     VARCHAR(20),
    warning      SMALLINT
);

CREATE TABLE icu.outputevents (
    subject_id   INTEGER NOT NULL,
    hadm_id      INTEGER NOT NULL,
    stay_id      INTEGER NOT NULL,
    caregiver_id INTEGER,
    charttime    TIMESTAMP NOT NULL,
    storetime    TIMESTAMP,
    itemid       INTEGER NOT NULL,
    value        DOUBLE PRECISION,
    valueuom     VARCHAR(20)
);

CREATE TABLE icu.inputevents (
    subject_id                        INTEGER NOT NULL,
    hadm_id                           INTEGER NOT NULL,
    stay_id                           INTEGER NOT NULL,
    caregiver_id                      INTEGER,
    starttime                         TIMESTAMP NOT NULL,
    endtime                           TIMESTAMP,
    storetime                         TIMESTAMP,
    itemid                            INTEGER NOT NULL,
    amount                            DOUBLE PRECISION,
    amountuom                         VARCHAR(20),
    rate                              DOUBLE PRECISION,
    rateuom                           VARCHAR(20),
    orderid                           INTEGER,
    linkorderid                       INTEGER,
    ordercategoryname                 VARCHAR(100),
    secondaryordercategoryname        VARCHAR(100),
    ordercomponenttypedescription     VARCHAR(100),
    ordercategorydescription          VARCHAR(50),
    patientweight                     DOUBLE PRECISION,
    totalamount                       DOUBLE PRECISION,
    totalamountuom                    VARCHAR(20),
    isopenbag                         SMALLINT,
    continueinnextdept                SMALLINT,
    statusdescription                 VARCHAR(20),
    originalamount                    DOUBLE PRECISION,
    originalrate                      DOUBLE PRECISION
);

CREATE TABLE icu.ingredientevents (
    subject_id          INTEGER NOT NULL,
    hadm_id             INTEGER NOT NULL,
    stay_id             INTEGER NOT NULL,
    caregiver_id        INTEGER,
    starttime           TIMESTAMP NOT NULL,
    endtime             TIMESTAMP,
    storetime           TIMESTAMP,
    itemid              INTEGER NOT NULL,
    amount              DOUBLE PRECISION,
    amountuom           VARCHAR(20),
    rate                DOUBLE PRECISION,
    rateuom             VARCHAR(20),
    orderid             INTEGER,
    linkorderid         INTEGER,
    statusdescription   VARCHAR(20),
    originalamount      DOUBLE PRECISION,
    originalrate        DOUBLE PRECISION
);

CREATE TABLE icu.procedureevents (
    subject_id              INTEGER NOT NULL,
    hadm_id                 INTEGER NOT NULL,
    stay_id                 INTEGER NOT NULL,
    caregiver_id            INTEGER,
    starttime               TIMESTAMP NOT NULL,
    endtime                 TIMESTAMP,
    storetime               TIMESTAMP,
    itemid                  INTEGER NOT NULL,
    value                   DOUBLE PRECISION,
    valueuom                VARCHAR(20),
    location                VARCHAR(100),
    locationcategory        VARCHAR(50),
    orderid                 INTEGER,
    linkorderid             INTEGER,
    ordercategoryname       VARCHAR(100),
    ordercategorydescription VARCHAR(50),
    patientweight           DOUBLE PRECISION,
    isopenbag               SMALLINT,
    continueinnextdept      SMALLINT,
    statusdescription       VARCHAR(20),
    originalamount          DOUBLE PRECISION,
    originalrate            DOUBLE PRECISION
);

-- ============================================================
-- NOTE MODULE (MIMIC-IV-Note v2.2)
-- ============================================================

CREATE TABLE note.discharge (
    note_id    VARCHAR(25) NOT NULL,
    subject_id INTEGER NOT NULL,
    hadm_id    INTEGER,
    note_type  VARCHAR(10),
    note_seq   SMALLINT,
    charttime  TIMESTAMP,
    storetime  TIMESTAMP,
    text       TEXT,
    PRIMARY KEY (note_id)
);

CREATE TABLE note.radiology (
    note_id    VARCHAR(25) NOT NULL,
    subject_id INTEGER NOT NULL,
    hadm_id    INTEGER,
    note_type  VARCHAR(10),
    note_seq   SMALLINT,
    charttime  TIMESTAMP,
    storetime  TIMESTAMP,
    text       TEXT,
    PRIMARY KEY (note_id)
);

-- ============================================================
-- NOTE DETAIL TABLES
-- ============================================================

CREATE TABLE note.discharge_detail (
    note_id       VARCHAR(25) NOT NULL,
    subject_id    INTEGER NOT NULL,
    field_name    VARCHAR(255),
    field_value   TEXT,
    field_ordinal SMALLINT
);

CREATE TABLE note.radiology_detail (
    note_id       VARCHAR(25) NOT NULL,
    subject_id    INTEGER NOT NULL,
    field_name    VARCHAR(255),
    field_value   TEXT,
    field_ordinal SMALLINT
);

-- ============================================================
-- ED MODULE
-- ============================================================

CREATE TABLE ed.edstays (
    subject_id         INTEGER NOT NULL,
    hadm_id            INTEGER,
    stay_id            INTEGER NOT NULL,
    intime             TIMESTAMP,
    outtime            TIMESTAMP,
    gender             VARCHAR(1),
    race               VARCHAR(60),
    arrival_transport  VARCHAR(50),
    disposition        VARCHAR(50),
    PRIMARY KEY (stay_id)
);

CREATE TABLE ed.diagnosis (
    subject_id  INTEGER NOT NULL,
    stay_id     INTEGER NOT NULL,
    seq_num     SMALLINT NOT NULL,
    icd_code    VARCHAR(10),
    icd_version SMALLINT,
    icd_title   TEXT
);

CREATE TABLE ed.medrecon (
    subject_id     INTEGER NOT NULL,
    stay_id        INTEGER NOT NULL,
    charttime      TIMESTAMP,
    name           TEXT,
    gsn            VARCHAR(10),
    ndc            VARCHAR(12),
    etc_rn         SMALLINT,
    etccode        VARCHAR(10),
    etcdescription TEXT
);

CREATE TABLE ed.pyxis (
    subject_id INTEGER NOT NULL,
    stay_id    INTEGER NOT NULL,
    charttime  TIMESTAMP,
    med_rn     SMALLINT,
    name       TEXT,
    gsn_rn     SMALLINT,
    gsn        VARCHAR(10)
);

CREATE TABLE ed.triage (
    subject_id     INTEGER NOT NULL,
    stay_id        INTEGER NOT NULL,
    temperature    DOUBLE PRECISION,
    heartrate      DOUBLE PRECISION,
    resprate       DOUBLE PRECISION,
    o2sat          DOUBLE PRECISION,
    sbp            DOUBLE PRECISION,
    dbp            DOUBLE PRECISION,
    pain           TEXT,
    acuity         DOUBLE PRECISION,
    chiefcomplaint TEXT
);

CREATE TABLE ed.vitalsign (
    subject_id  INTEGER NOT NULL,
    stay_id     INTEGER NOT NULL,
    charttime   TIMESTAMP,
    temperature DOUBLE PRECISION,
    heartrate   DOUBLE PRECISION,
    resprate    DOUBLE PRECISION,
    o2sat       DOUBLE PRECISION,
    sbp         DOUBLE PRECISION,
    dbp         DOUBLE PRECISION,
    rhythm      TEXT,
    pain        TEXT
);
