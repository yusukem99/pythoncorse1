# Kaggle教材移行・日本語化プロジェクト

本ドキュメントでは、「Kaggle公式『Intro to Programming』コースの専門学校授業向けカスタマイズ・移行プロジェクト」の目的、これまでの進捗、および手法について記録します。

## 1. プロジェクトの目的
Kaggleが公式に提供している初学者向けプログラミング教材（Intro to Programming など）を、**専門学校の授業システム（Google Colab環境など）に合わせて独立した形で提供**し、かつ**日本人学生向けに自然な日本語化**を行うことを目的とします。

Kaggleの学習環境は「教材本体（Jupyter Notebook形式）」と「採点・正誤判定システム（learntools）」の2つで構成されています。これをKaggleのサイト外（Colabなど）でそのまま実行しようとすると、`learntools`にアクセスできないためのエラーが発生します。この仕組みを紐解き、外部環境でもスムーズに動作するクリーンな教材環境を構築します。

**【生徒の想定利用フロー】**
本教材は、生徒が **Google Colab上から直接GitHubリポジトリ内のノートブックを開いて（あるいはクローンして）利用する** ことを想定しています。
そのため、環境構築の手間を省くべく、各演習ノートブックの先頭には `!pip install git+https://github.com/yusukem99/pythoncorse1.git` で採点システムを自動導入するセットアップセルが初めから埋め込まれる仕組みにしています。

## 2. 教材移行と構築の手法
以下の手法で、Kaggleから独立した授業用の教材リポジトリ（Githubなど）を構築します。

1. **採点システム（`learntools`）のパッケージ化と分離**
    *   Kaggle公式の `learntools` ソースコードをリポジトリに配置し、`setup.py` を整備します。
    *   これにより、Colab等の外部環境から `!pip install git+https://github.com/yusukem99/pythoncorse1.git` の1行で簡単に採点システムをインストール・使用できる環境を用意します。
    *   外部から実行する上で不要だったライブラリによる循環参照エラー(`ml_insights`)や、名称依存エラー(`sklearn` -> `scikit-learn`)といった障壁を解消します。
2. **教材本体（Jupyter Notebook）の公式API経由での取得**
    *   Kaggle上の教材ノートブックはGitHub上には公開されていないため、Kaggle公式のコマンドラインAPI（`kaggle kernels pull`）を使用します。
    *   Kaggleの認証用キーを設定し、ローカル環境へ直接ノートブックファイル（`*.ipynb`）をダウンロードして保持します。
3. **ノートブックとシステムの日本語化**
    *   **採点システム（`ex1.py`など）の日本語化**: 学生へのフィードバック（正解時のお祝いメッセージや、ヒントの内容など）について、直接Pythonソースコード内の英語文（`_congrats`, `_hint` 等）を日本語に書き換えます。
    *   **ノートブック本体の日本語化**: 教材本体であるNotebook（`.ipynb`）については、ファイル構造（JSON）が壊れることを防ぐため、独自に構築した「翻訳専用の安全なPythonスクリプト」を用いて、JupyterのMarkdownセル（解説文）およびコードセル内のコメントのみを精緻に日本語へ置換します。

## 3. これまでの進捗状況

*   ✅ **インフラ構築**: GitHubリポジトリへの `learntools` の配置と `setup.py` パッケージ定義の修正。
*   ✅ **動作検証**: Colabから `pip install` で `learntools` を読み込み、`Correct` の正解判定が出るまでのシステム全体の疎通テストを完了。
*   ✅ **教材の一括ダウンロード**: Kaggle APIを用いて `Intro to Programming` コース（全5章分の解説・演習用ノートブック計10ファイル）を `notebooks/intro_to_programming/` フォルダへ格納。
*   ✅ **採点システムの日本語化**: 最初の演習課題（`learntools/intro_to_programming/ex1.py`）のメッセージ日本語化を完了。
*   ✅ **セキュリティ対策**: `.gitignore` にKaggle APIトークン（`.kaggle.json` 等）が含まれないよう設定を追加。
