import json
import pathlib
import re

p = pathlib.Path('c:/Users/PC/Desktop/AI2008-Group-7-Python_Notebook/Group_7_AI_Driven_Dynamic_Pricing_in_Freight_&_Shipping_Logistics.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))
found = 0
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source'])
        if re.search(r'drop\(|train_test_split|OneHotEncoder', src):
            print('=== CELL', i, '===')
            print(src)
            print()
            found += 1
            if found >= 20:
                break
print('FOUND', found, 'cells')
