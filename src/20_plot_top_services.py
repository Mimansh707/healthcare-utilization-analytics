import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_PATH = "outputs/facility_service_summary.csv"
OUT_DIR = Path("outputs")
OUT_DIR.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(INPUT_PATH)

    # For each facility, keep top 5 services by visits
    top = (
        df.sort_values(["facility_type", "total_visits"], ascending=[True, False])
          .groupby("facility_type")
          .head(5)
    )

    for facility, g in top.groupby("facility_type"):
        plt.figure()
        plt.bar(g["service_type"], g["total_visits"])
        plt.xticks(rotation=45, ha="right")
        plt.title(f"Top 5 Services by Total Visits ({facility}) - 2023")
        plt.ylabel("Total Visits")
        plt.tight_layout()

        out_path = OUT_DIR / f"top5_services_{facility.lower().replace(' ', '_')}.png"
        plt.savefig(out_path)
        plt.close()

    print("Saved charts to outputs/*.png")

if __name__ == "__main__":
    main()

