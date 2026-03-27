import pandas as pd
import os

base = os.path.dirname(os.path.abspath(__file__))

# NASA sample table
nasa_sample = pd.read_csv(os.path.join(base, "temp_additional", "GSM1145430_sample_table.txt"), sep='\t', nrows=5)
print("=== NASA Sample Table (GSM1145430) ===")
print(nasa_sample.head())
print("Columns:", nasa_sample.columns.tolist())
print()

# NASA fold change
nasa_fc = pd.read_csv(os.path.join(base, "temp_additional", "GSE47126_Fold_change_data.txt"), sep='\t', nrows=10, header=1)
print("=== NASA Fold Change ===")
print(nasa_fc.head(10))
print("Shape:", nasa_fc.shape)
print()

# GEO RA data
geo_path = os.path.join(base, "GEO dataset", "GSE42842_series_matrix.txt")
with open(geo_path, 'r') as f:
    lines = f.readlines()
print(f"=== GEO RA Data: {len(lines)} lines total ===")
for i, line in enumerate(lines[:120]):
    if '!Sample_' in line or 'ID_REF' in line or 'characteristics' in line.lower() or 'geo_accession' in line.lower():
        print(f"Line {i}: {line[:150].strip()}")
