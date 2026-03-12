import json

path = r"c:\Users\yusuke\programs\pythoncorse1\notebooks\intro_to_programming\exercise-arithmetic-and-variables.ipynb"

with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

replacements = {
    "# Set up the exercise": "# 演習のセットアップ（変更しないでください）",
    "print('Setup complete.')": "print('セットアップ完了。')",
    "# DO NOT REMOVE: Mark this question as completed": "# 削除しないでください: 採点を実行します",
    "# DO NOT REMOVE: Mark this question as completed ": "# 削除しないでください: 採点を実行します",
    "# TODO: Change the message": "# TODO: メッセージを変更する",
    "\"Your message here!\"": "\"ここにメッセージ！\"",
    "# Uncomment to get a hint": "# コメントを外してヒントを見る",
    "# Uncomment to receive a hint": "# コメントを外してヒントを見る",
    "# Uncomment to view solution": "# コメントを外して解答を見る",
    "# Uncomment to view the solution": "# コメントを外して解答を見る",
    "# DO NOT REMOVE: Check your answer": "# 削除しないでください: 答えをチェックする",
    "# Create variables": "# 変数を作成する",
    "# Calculate number of seconds in four years": "# 4年間の総秒数を計算する",
    "# TODO: Set the value of the births_per_min variable": "# TODO: 1分あたりの出生数(births_per_min)をセットする",
    "# TODO: Set the value of the births_per_day variable": "# TODO: 1日あたりの出生数(births_per_day)を計算してセットする",
    "# Load the data from the titanic competition": "# タイタニックコンペティションのデータを読み込む",
    "# Show the first five rows of the data": "# データの最初の5行を表示する",
    "../input/titanic/train.csv": "https://raw.githubusercontent.com/yusukem99/pythoncorse1/main/datasets/titanic_train.csv",
    "# Number of total passengers": "# 総乗客数",
    "# Number of passengers who survived": "# 生存した乗客数",
    "# Number of passengers under 18": "# 18歳未満の乗客数",
    "# TODO: Fill in the value of the survived_fraction variable": "# TODO: 生存者の割合(survived_fraction)を計算してセットする",
    "# Print the value of the variable": "# 変数の値を表示する",
    "# TODO: Fill in the value of the minors_fraction variable": "# TODO: 未成年者の割合(minors_fraction)を計算してセットする",
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

# 既に同じセルがないか確認して先頭に追加
if nb["cells"][0].get("source", []) != setup_code_cell["source"]:
    nb["cells"].insert(0, setup_code_cell)

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, separators=(',', ':'))

print("Code comments translation and setup cell insertion completed successfully.")
