import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

nb_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "data.ipynb")
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])

keywords = ['shap', 'cinsiyet', 'gender', 'interaction', 'etkilesim', 'etkileşim',
            'stratiф', 'stratif', 'erkek', 'kadin', 'kadın']

print("=== SHAP / Cinsiyet analizi cell'leri ===\n")
for i, cell in enumerate(cells):
    src = ''.join(cell.get('source', []))
    if any(kw in src.lower() for kw in keywords):
        print(f"Cell {i} ({cell['cell_type']}):")
        print(src[:600])
        print("--- OUTPUTS ---")
        for out in cell.get('outputs', []):
            txt = ''.join(out.get('text', out.get('data', {}).get('text/plain', [])))
            print(txt[:400])
        print("===\n")
