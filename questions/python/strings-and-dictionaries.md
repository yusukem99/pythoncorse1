# Strings and Dictionaries

## 問0a-0e

まずはウォーミングアップとして文字列の長さを予想してみましょう。

`a`～`e`で宣言された文字列の長さを、`length`に代入してください。

ここで`len()`関数を使用しないこと。

## 問１

個人や企業が蓄積して扱えるデータを活用し、新しい価値を提案する仕事を「データサイエンティスト」といいます。

データサイエンティスト仕事のうち8割はデータクレンジングに、残りの2割はその作業に不満をいうことだと言われています。

ここではZIPコードのデータクレンジングに関する関数を作ってみます。

ZIPコードとはアメリカ合衆国の郵便番号で、ちょうど５桁の数字で構成されています。

与えられた`zip_code`が正しいフォーマットか判定し`True`または`False`で返す関数`is_valid_zip`を完成させてください。

ヒント：`str`型は便利なメソッドを備えています。`help(str)`を使ってみてください。

*データクレンジングとは*

破損したデータ、不正確なデータ、無関係なデータを検出し、データベースに格納する前に修正または削除することです。

## 問２

ある研究者が論文を集めています。

研究者は集めた何千もの論文の中から、特定の単語を含むものだけを抽出したいと思いました。

 `word_search`関数では`doc_list`に論文の内容のリスト、`keyword`に検索する単語が渡されます。

検索する単語`keyword`が含まれる論文のインデックスを含むリストを返すように、`word_search`関数を完成させてください。

ここで、論文の抽出条件は以下のルールに従うものとします。

- キーワードの一部のみが一致するものは、不一致とする。例えばkeyword="closed"のとき、"enclosed."は不一致とする。
- 大文字と小文字を区別しない。例えば、"keyword=closed"のとき"Closed the case."は一致とする。
- ピリオドとカンマは検索条件に影響しない。例えば、keyword="closed"のとき、"It is closed."は一致とする。

例:
```
>>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
>>> word_search(doc_list, 'casino')
[0]
```

## 問３

研究者は先に作った関数`word_search`を複数の単語で検索できるようにしたいと思いました。

`multi_word_search()`関数は、引数`keywords`で検索する複数の単語がリストで渡されます。

それぞれの単語を**キー**、論文のインデックスを含むリストをバリューとしたペアの辞書を返すように関数を完成させてください。

ここでは問２で作成した`word_search`を活用してください。

例:
```
def multi_word_search(doc_list, keywords):
    # 関数内でword_search関数を呼び出す
    hit_list = word_search(doc_list, 'casino')
```

```
    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
```    