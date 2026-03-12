# エージェント引き継ぎ用ドキュメント (AGENT_HANDOVER.md)

次のPC・環境で作業を引き継ぐAIエージェントへの連絡事項です。
本プロジェクトは、Kaggle公式の「Intro to Programming」コースを専門学校の Colab 授業用にカスタマイズし、完全に日本語化したリポジトリ(`yusukem99/pythoncorse1`)を構築することを目的としています。

## 1. 現状の進捗（完了していること）
*   **採点パッケージ(`learntools`)の独立化**: Kaggleの独自システムである `learntools` をリポジトリ内に配置し、Colab等から `!pip install git+https://github.com/yusukem99/pythoncorse1.git` でロードできるよう `setup.py` の整備や依存ライブラリ名の修正を完了しました。
*   **教材の取得**: 全10章（解説5つ、演習5つ）の `.ipynb` ノートブックをローカルの `notebooks/intro_to_programming/` フォルダにKaggle APIを使ってダウンロード済みです。
*   **第1章（Arithmetic and Variables）の完全対応**:
    1.  `learntools/intro_to_programming/ex1.py` の採点メッセージ・ヒント・正解の日本語化完了。
    2.  `notebooks/intro_to_programming/arithmetic-and-variables.ipynb` (解説) のMarkdownテキストの自然な日本語化完了。
    3.  `notebooks/intro_to_programming/exercise-arithmetic-and-variables.ipynb` (演習) について、以下を完了。
        *   Markdownとコード内コメント群の日本語化
        *   ノートブック先頭へ、GitHubから `learntools` を pip install する「セットアップ用セル」の自動挿入
        *   外部データ(Titanic)のパスをKaggle固有のものから、作成したGitHub上のRAW URL(`https://raw.githubusercontent.com/yusukem99/pythoncorse1/main/datasets/titanic_train.csv`)へ置換

## 2. 次のエージェントへの重要指示（今後のタスク）

ここからは、第2章（関数 / Functions）以降の教材を同様に日本語化・Colab対応していく作業となります。

**✅ 必須の守るべきルール**:
Kaggleからダウンロードした Jupyter Notebook (`.ipynb`) ファイルは改行を削ったMinifiedなJSONとして保存されています。**ファイル全体を雑なスクリプトで一括置換しようとすると構造が壊れ、ノートブックとして開けなくなります。**
これまでの作業（`translation_scripts/translate_ex1_markdown.py` など参照）と同様に、**「必ずPythonの `json` モジュールで読み込み、テキスト部分の辞書のみを置換したうえで、`json.dump(nb, f, ensure_ascii=False, separators=(',', ':'))` を使って元のインデントなし構造を完全維持して保存する手法」**を徹底してください。

**🔄 今後の具体的なステップ**:
1.  **システムメッセージの翻訳**: `learntools/intro_to_programming/` 以下の `ex2.py`, `ex3.py` 等の中に書かれている英語のフィードバック、ヒント（`_hint`）、正答（`_solution`）を日本語に書き換えます。
2.  **ノートブックの翻訳**: `notebooks/intro_to_programming/` に格納されている残りのファイル（`functions.ipynb` 等）について、Markdownとコード内コメントをPythonスクリプトによる安全な手法で日本語化します。
3.  **セットアップセルの挿入**: 翻訳した演習用ノートブック（`exercise-*.ipynb`）の先頭に、第1章(ex1)と同様に `!pip install ...` とテストの `print("✅ インストールが完了しました。")` を行うセルを追加します。
4.  **CSVデータ等のパス修正**: 演習内に `../input/` などのローカル固有パスがある場合、先生のGitHub上にある提供データ等を参照するようにURLを差し替えてください。

よろしくお願いいたします。
