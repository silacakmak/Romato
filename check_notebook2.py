import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

nb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "data.ipynb")
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])

geo_keywords = ['gse42842', 'gse93272', 'das28', 'eular', 'responder', 'yanit', 'yanıt',
                'label', 'etiket', 'adalimumab', 'etanercept', 'drug', 'ilac', 'ilaç',
                'series_matrix', 'geo dataset', 'response']

print("=== GEO / ilaç yanıtı ile ilgili cell'ler ===\n")
found = False
for i, cell in enumerate(cells):
    src = ''.join(cell.get('source', []))
    if any(kw in src.lower() for kw in geo_keywords):
        found = True
        print(f"Cell {i} ({cell['cell_type']}):")
        print(src[:600])
        print("--- OUTPUTS ---")
        for out in cell.get('outputs', []):
            txt = ''.join(out.get('text', out.get('data', {}).get('text/plain', [])))
            print(txt[:300])
        print("===\n")

if not found:
    print("GEO ilaç yanıtı etiketi çıkarma kodu BULUNAMADI.")
    print("\n=== Tüm cell'lerin özeti ===")
    for i, cell in enumerate(cells):
        src = ''.join(cell.get('source', []))
        ctype = cell['cell_type']
        print(f"Cell {i} ({ctype}): {src[:80].strip()}")
