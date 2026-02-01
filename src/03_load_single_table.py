import pandas as pd

FILE_PATH = "data/raw/cms_outpatient_utilization_2023.xlsx"

SHEET_NAME = "MDCR OUTPATIENT 5_CPS_09UOT"

df = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)

print("Loaded sheet:", SHEET_NAME)
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())


