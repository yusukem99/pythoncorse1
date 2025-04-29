これまで作ってきた関数は、毎回同じ処理を実行されるものでした。

たとえば、次の`add_five`関数に、`7`を渡すと、`12`が返ってきます。

```
def add_five(x):
    return x + 5
```

ここで、引数で与えられたxが`10`以下のときは`3`を足し、`10`より大きいときは`8`を足す関数を作りたいときはどうすればいいでしょうか？

条件(condition)

条件とは、真か偽の二つの値を持つものです。Pythonでは、`True`と`False`で表現します。
たとえば、`2 > 3`は偽（False）です。

```
print(2 > 3)
False
```

比較演算子（Conditional Operators）を使うと、二つの値を比較することができます。


- `==` 等価（equals）
- `!=` 非等価（not equal）
- `<`  小なり（less than）
- `<=`  以下（less than or equal to）
- `>`  大なり（greater than）
- `>=`  以上（greater than or equal to）

if文（if statement）
条件に応じて、実行する処理を変えることができます。Pythonでは、`if`文を使います。

```
def evaluate_temp(temp):
    message = "平熱です。"
    if temp > 38:
        message = "熱があります！"
    return message
```

if...else文（if..else statement）
if文の後にelse文を使うと、条件が偽のときに実行する処理を指定できます。

```
def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "熱があります！"
    else:
        message = "平熱です。"
    return message
```