# Syntax, Variables, and Numbers - 文法、変数、数値

## 問０

これはちょっとおかしな設問なのですが、これからの演習問題を解くための準備です。

次の質問に答えてください。

*what is your favorite color?*

`color`に適切な値を代入して、`q0.check()`を実行してください。

正解が分からないときは、下のコードセルの`q0.hint()`関数を使うことができます。

## 問１

円周率`pi`と円の直径`diameter`を表す変数が宣言されています。

円の半径`radius`と円の面積`area`を表す変数を宣言してください。

下の表を参考にしてください。

| Operator     | Name           | Description                                            |
|--------------|----------------|--------------------------------------------------------|
| ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
| ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
| ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
| ``-a``       | Negation       | The negative of ``a``                                  |


## 問２

`a`と`b`の値を入れ替えてください。

つまり、`a`は`b`が参照していたオブジェクトを参照し、`b`は`a`が参照していたオブジェクトを参照するようにしてください。

下のコードセルの`# Your code goes here. ...`の部分を書き換えてください。

`Setup code - don't touch this part`と書かれている部分を変更してはいけません。

## 問３a
1になるように以下の式に括弧を付け加えてください。

## 問３b

0になるように以下の式に括弧を付け加えてください。

## 問４

ハロウィンの日、アリスとボブとキャロルでアメを持ち寄って均等に分けあうことにしました。

3人の友情のために、余ったアメは砕いてしまうことにします。

以下の変数に持ち寄ったアメの数が入っています。

```
alice_candies = 121
bob_candies = 77
carol_candies = 109
```

`to_smash = -1`の右辺を書き換えて、砕くアメの数を`to_smash`に代入してください。