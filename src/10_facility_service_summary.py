import pandas as pd

INPUT_PATH = "data/processed/cms_outpatient_utilization_fact_2023.csv"
OUTPUT_PATH = "outputs/facility_service_summary.csv"

def main():
    df = pd.read_csv(INPUT_PATH)

    # Ensure numeric columns are numeric
    numeric_cols = ["total_persons", "total_visits", "visits_per_enrollee", "visits_per_person"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Basic summary table
    summary = (
        df.groupby(["facility_type", "service_type"], as_index=False)["total_visits"]
        .sum()
        .sort_values(["facility_type", "total_visits"], ascending=[True, False])
    )

    # % contribution within facility
    summary["facility_total_visits"] = summary.groupby("facility_type")["total_visits"].transform("sum")
    summary["pct_of_facility_visits"] = (summary["total_visits"] / summary["facility_total_visits"]) * 100

    # Save for Tableau/SQL later
    summary.to_csv(OUTPUT_PATH, index=False)

    print("Saved:", OUTPUT_PATH)
    print("\nTop rows:")
    print(summary.head(12).to_string(index=False))

if __name__ == "__main__":
    main()

