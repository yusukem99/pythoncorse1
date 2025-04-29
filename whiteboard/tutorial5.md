プログラミングにおいて適切な型を使って情報を管理することが重要です。Pythonでは大量のデータを扱うために`list`や`dict`,`tuple`といった型を使います。

今回は特に`list`の使い方を学んでいきます。


次のコードを見てみましょう。`flowers`という変数に花の名前が列挙されています。

```
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)
```

これは文字列型`str`で、カンマ`,`で区切られた文字列です。

この中に合計何種類の花があるでしょうか？数えるのはちょっと大変ですね...

pythonでは`list`型を使うと、こういうとき便利になります。

```
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
```

以前習った`len``関数を使うと、リストの要素数を数えることができます。

```
print(len(flowers_list))
```

リストの要素の取り出し`Indexing`は次のように行います。プログラミングにおいて、リストの要素は`0`から始まります。

```
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])
```

さらにPythonではリストの切り出し`Slicing`ができます。

最初のx個の要素を取り出すには、次のようにします。`[:x]`

例えば、最初の三つの要素を取り出すには、次のようにします。`flowers_list[:3]`

```
print("First three entries:", flowers_list[:3])
``` 

後ろから二つの要素を取り出すには、次のようにします。`[-x:]`

例えば、後ろから二つの要素を取り出すには、次のようにします。`folowers_list[-2:]`

```
print("Final two entries:", flowers_list[-2:])
```

リストから要素を削除するには、`remove`メソッドを使います。

```
flowers_list.remove("globe thistle")
print(flowers_list)
```

リストに要素を追加するには、`append`メソッドを使います。
```
flowers_list.append("snapdragon")
print(flowers_list)
```

他にもリストは便利な機能があります。

次のようなリストがあったとき

```
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
```

```
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))
```

最初の五日間で売り上げた本の数の平均はいくらでしょうか？それも一行でできてしまいます。