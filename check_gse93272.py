import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# GSE93272 dosyasını bul
base = os.path.dirname(os.path.abspath(__file__))
search_dirs = [base, os.path.join(base, "venv"), os.path.join(base, "GEO dataset")]

for d in search_dirs:
    for f in os.listdir(d):
        if "93272" in f:
            print(f"Bulundu: {os.path.join(d, f)}")

# Dosya varsa başlık bilgilerini oku
for d in search_dirs:
    fp = os.path.join(d, "GSE93272_series_matrix.txt")
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                if line.startswith("!Series_title") or line.startswith("!Series_summary") or line.startswith("!Series_overall_design"):
                    print(line.strip()[:300])
        break
