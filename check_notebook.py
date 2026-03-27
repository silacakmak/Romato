import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

nb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "data.ipynb")
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])
print(f"Toplam cell sayisi: {len(cells)}\n")

nasa_keywords = ['nasa', 'glds', 'astronaut', 'preflight', 'postflight',
                 'fold_change', 'gse47126', 'differential', 'deg',
                 'ttest', 't_test', 'pvalue', 'log2fc', 'gsm114', 'space',
                 'fc', 'accession']

print("=== NASA ile ilgili cell'ler ===")
for i, cell in enumerate(cells):
    src = ''.join(cell.get('source', []))
    if any(kw in src.lower() for kw in nasa_keywords):
        print(f"\nCell {i} ({cell['cell_type']}):")
        print(src[:500])
        print("--- OUTPUTS ---")
        for out in cell.get('outputs', []):
            txt = ''.join(out.get('text', out.get('data', {}).get('text/plain', [])))
            print(txt[:200])
        print("===")
