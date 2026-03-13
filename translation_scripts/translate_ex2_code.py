import json

path = r"/Users/yusuke/programs/pythoncorse1/notebooks/intro_to_programming/exercise-functions.ipynb"

with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

replacements = {
    "# Set up the exercise": "# 演習のセットアップ（変更しないでください）",
    "print('Setup complete.')": "print('セットアップ完了。')",
    "# TODO: Complete the function": "# TODO: 関数を完成させる",
    "# Check your answer ": "# 答えをチェックする ",
    "# Check your answer": "# 答えをチェックする",
    "# Uncomment to see a hint": "# コメントを外してヒントを見る",
    "# Uncomment to receive a hint": "# コメントを外してヒントを見る",
    "# Uncomment to view the solution": "# コメントを外して解答を見る",
    "# TODO: Use the get_expected_cost function to fill in each value": "# TODO: get_expected_cost 関数を使用して、それぞれの値を埋める",
    "# TODO: Finish defining the function": "# TODO: 関数の定義を完成させる",
    "# TODO: Set the project_cost variable to the cost of the project": "# TODO: project_cost 変数にプロジェクトのコストを設定する"
}

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        if isinstance(cell["source"], list):
            new_source = []
            for line in cell["source"]:
                for eng, jpn in replacements.items():
                    line = line.replace(eng, jpn)
                new_source.append(line)
            cell["source"] = new_source
        elif isinstance(cell["source"], str):
            src = cell["source"]
            for eng, jpn in replacements.items():
                src = src.replace(eng, jpn)
            cell["source"] = src

# インストール用セルの追加
setup_code_cell = {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# GitHub (yusukem99/pythoncorse1) から learntools パッケージをインストールする\n",
    "!pip install --upgrade --no-cache-dir git+https://github.com/yusukem99/pythoncorse1.git\n",
    "\n",
    "print(\"✅ インストールが完了しました。\")"
   ]
}

if nb["cells"][0].get("source", []) != setup_code_cell["source"]:
    nb["cells"].insert(0, setup_code_cell)

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, separators=(',', ':'))

print("Code translation and setup cell insertion completed successfully.")
