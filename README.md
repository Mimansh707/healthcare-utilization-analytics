# Healthcare Utilization Analytics (CMS Medicare Outpatient, 2023)

## Overview
This project analyzes Medicare outpatient utilization using public CMS Program Statistics data (Medicare Outpatient Facility, 2023). The goal is to convert a human-formatted government report into an analysis-ready fact table and extract actionable insights about utilization patterns across facility types and services.

## Data Source (Public, Non-PHI)
- CMS Program Statistics: Medicare Outpatient Facility (2023)
- The raw dataset is provided as a multi-sheet Excel workbook with reporting-oriented formatting.
- No proprietary, confidential, or patient-identifiable information is used.

## Problem Statement
How do outpatient utilization patterns differ across facility types and service categories and which services drive the majority of visits?

## Methods
1. **Data understanding & ingestion (Phase 1)**
   - Identified the relevant worksheet: `MDCR OUTPATIENT 5_CPS_09UOT`
   - Validated table structure and metric definitions using CMS documentation (methodology + glossary)

2. **Data structuring (Phase 2)**
   - Converted a hierarchical report-style table into a tidy fact table by:
     - Detecting facility header rows (`Total -- ...`)
     - Forward-filling facility context to service rows
     - Filtering to atomic observations (facility × service)
     - Normalizing dimension values (e.g., removing `Total --`)

3. **Analysis (Phase 3)**
   - Summarized total visits and percentage contribution by service within each facility type.

## Key Outputs
- Clean fact table:
  - `data/processed/cms_outpatient_utilization_fact_2023.csv`
- Summary table (Tableau/SQL-ready):
  - `outputs/facility_service_summary.csv`

## Key Findings (2023)
- **Hospital Outpatient** utilization is diagnostics/ancillary-driven:
  - Laboratory (~21%), Radiology (~16%), Pharmacy (~14%) are top contributors.
- **Other Outpatient** utilization is concentrated in chronic-care services:
  - Rehabilitation (~31%) and ESRD (~27%) together account for nearly 60% of visits.
- Facility types show different care patterns:
  - Hospital Outpatient is more diversified across services, while Other Outpatient is more concentrated.
## Business Insights 
- **Hospital Outpatient is diagnostics/ancillary-driven:** Laboratory and Radiology together account for a large share of visits, suggesting high operational demand for diagnostic workflows and supporting services.
- **Other Outpatient is chronic-care concentrated:** Rehabilitation and ESRD dominate visit volume, reflecting repeat-care patterns that may require consistent staffing, scheduling capacity, and continuity-focused operations.
- **Operational implication:** Different facility types exhibit different service mixes (diversified vs concentrated), so resource planning should be tailored by facility type rather than assuming uniform outpatient demand.

## How to Run
```bash
# Create and activate environment
python3 -m venv .venv
source .venv/bin/activate
pip install pandas openpyxl

# Generate facility-service summary
python src/10_facility_service_summary.py

## Tableau Dashboard – Outpatient Utilization (CMS 2023)

This dashboard compares outpatient **volume** (total visits) with **intensity**
(visits per person) using CMS 2023 data to highlight utilization patterns
across services.

 **Live Dashboard**  
https://public.tableau.com/app/profile/mimansha.khadka/viz/OutpatientUtilizationVolumevsIntensityCMS2023/OutpatientUtilizationVolumevsIntensityCMS2023?publish=yes

**Key Insights**
- Diagnostic services drive the highest outpatient visit volume
- Chronic services (e.g., ESRD, Rehabilitation) show very high utilization intensity
- Volume and intensity differ substantially across services, informing care planning
