これまでPythonでいろんな変数を作成してきました。

x = 14

y = 3.14

greeting = "Hello, World!"

`x`は整数、`y`は浮動小数点数、`greeting`は文字です。これらの変数の種類を、プログラミング言語では「型」(data type)と呼びます。

型は、変数がどのようなふるまいをするかを決めるものでとても重要です。たとえば、12 / 2は6ですが、"dog" / "cat"という計算は出来ません。

Integer（整数）

x = 14

Float（小数）
y = 3.14

`round`関数を使うと、小数を指定した桁数に丸めることができます。

```
y = 3.14159265358979323846
y_rounded = round(y, 2) # 小数点以下2桁に丸める
print(y_rounded) # 3.14
```

Boolean（真偽値）

真か偽の二種類だけの値を持つ型です。Pythonでは`True`と`False`で表現します。

x = True
x = False 

`1`は`2`より小さいのでPythonではこのように書くと、`z_three`は`True`になります。

z_three = (1 < 2)

`not`を使うと、`True`を`False`に、`False`を`True`に変えることができます。

```
x = True
print(not x) # False
```

String（文字列）

文字の集まりを表す型です。Pythonでは`""`または`''`で囲みます。

```
greeting = "Hello, World!"
print(greeting) # Hello, World!
```

数字を""や''で囲むと文字列になります。

```
my_number = "1.12321"
print(my_number)
print(type(my_number))
# <class 'str'>
```

Pythonでは文字列に掛け算をすることができます。

```
newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))
```

"abc"*.3.14はどうなるでしょう？
