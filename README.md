# Healthcare Utilization Analytics  
**CMS Medicare Outpatient (2023)**

## Overview
This project analyzes **Medicare outpatient utilization** using public **CMS Program Statistics (2023)** data.  
The objective is to transform a **human-formatted government report** into an **analysis-ready fact table** and uncover how utilization patterns differ across **facility types** and **service categories**.

---

## Data Source (Public, Non-PHI)
- **CMS Program Statistics – Medicare Outpatient Facility (2023)**
- Source format: multi-sheet Excel workbook with reporting-oriented layout
- No proprietary, confidential, or patient-identifiable information is used

---

## Problem Statement
**How do outpatient utilization patterns differ across facility types and services, and which services drive the majority of visits?**

---

## Methods

### Data Ingestion & Understanding
- Identified the relevant worksheet: `MDCR OUTPATIENT 5_CPS_09UOT`
- Validated metrics and definitions using CMS methodology and glossary

### Data Structuring
Converted a hierarchical, report-style table into a **tidy fact table** by:
- Detecting facility header rows (`Total -- ...`)
- Forward-filling facility context to service rows
- Filtering to atomic observations (facility × service)
- Normalizing dimension values (removing report-only labels)

### Analysis
- Aggregated total visits by service and facility type
- Computed service-level contribution and utilization intensity

---

## Key Outputs
- **Clean fact table:**  
  `data/processed/cms_outpatient_utilization_fact_2023.csv`
- **Summary table (SQL/Tableau-ready):**  
  `outputs/facility_service_summary.csv`

---

## Key Findings (2023)
- **Hospital Outpatient** utilization is diagnostics-driven  
  - Laboratory (~21%), Radiology (~16%), Pharmacy (~14%) dominate visit volume
- **Other Outpatient** utilization is concentrated in chronic-care services  
  - Rehabilitation (~31%) and ESRD (~27%) account for ~60% of visits
- Facility types exhibit **distinct care patterns**  
  - Hospital Outpatient is diversified across services  
  - Other Outpatient is more concentrated

---

## Business Implications
- Diagnostic-heavy utilization implies sustained demand on imaging and lab workflows
- Chronic-care concentration suggests repeat-visit patterns requiring stable staffing and scheduling
- Resource planning should be **facility-specific**, not uniform across outpatient settings

---

## Tableau Dashboard – Outpatient Utilization (CMS 2023)
This dashboard compares **service volume** (total visits) with **utilization intensity** (visits per person) to highlight differences in outpatient care patterns.

🔗 **Live Dashboard**  
https://public.tableau.com/app/profile/mimansha.khadka/viz/OutpatientUtilizationVolumevsIntensityCMS2023/OutpatientUtilizationVolumevsIntensityCMS2023

**Dashboard Insights**
- Diagnostic services drive the highest outpatient visit volume
- Chronic services (e.g., ESRD, Rehabilitation) show very high utilization intensity
- Volume and intensity differ substantially across services, informing care planning

---

## How to Run
```bash
# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl

# Generate facility–service summary
python src/10_facility_service_summary.py

