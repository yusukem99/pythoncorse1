import json
import os

notebook_path = r"c:\Users\yusuke\programs\pythoncorse1\notebooks\intro_to_programming\arithmetic-and-variables.ipynb"

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

replacements = {
    "# Multiply 3 by 2": "# 3に2を掛ける",
    "Multiply 3 by 2": "3に2を掛ける",
    "# Create a variable called test_var and give it a value of 4+5": "# test_varという変数を作成し、4+5の値を割り当てる",
    "# Print the value of test_var": "# test_varの値を出力する",
    "# Set the value of a new variable to 3": "# 新しい変数に3の値を設定する",
    "# Print the value assigned to my_var": "# my_varに割り当てられた値を出力する",
    "# Change the value of the variable to 100": "# 変数の値を100に変更する",
    "# Print the new value assigned to my_var": "# my_varに割り当てられた新しい値を出力する",
    "# Increase the value by 3": "# 値を3増やす",
    "# Create variables": "# 変数を作成する",
    "# Calculate number of seconds in four years": "# 4年間の秒数を計算する",
    "# Update to include leap years": "# うるう年を含めるように更新する",
}

for cell in nb['cells']:
    if cell.get('cell_type') == 'code':
        source = cell['source']
        if isinstance(source, list):
            new_source = []
            for line in source:
                for k, v in replacements.items():
                    line = line.replace(k, v)
                new_source.append(line)
            cell['source'] = new_source
        elif isinstance(source, str):
            for k, v in replacements.items():
                source = source.replace(k, v)
            cell['source'] = source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Notebook code cells translation completed successfully.")
