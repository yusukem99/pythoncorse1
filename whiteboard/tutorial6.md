Python言語の名前の由来は、イギリスのコメディアンの「モンティ・パイソン」から来ています。

モンティ・パイソンのコント「Spam」

=====

ウェイトレス：
「本日のメニューは、スパム＆卵、スパム＆ベーコン＆スパム、スパム＆ソーセージ＆スパム…（全部スパム入り）」

奥さん：
「スパムが入ってない料理はないの？」

ウェイトレス：
「ありません」

奥さん：
「スパムは嫌いなの！」

（ここで後ろのバイキングたちが「♪スパム スパム スパム スパム～」と合唱を始める）

=====

「Intro to Programming」で習った内容を振り返って見ましょう

```
spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)
```

- 変数の宣言と代入`Variable assignment`
- 関数の呼び出し`Function calls`
- コメント`Comments`
- 条件とIF文`Conditionals and IF statements`
- コードブロック
- 型`Types`


| 演算子     | 名前           | 説明                                            |
|--------------|----------------|--------------------------------------------------------|
| ``a + b``    | 加算       | `a`と`b`の合計                                   |
| ``a - b``    | 減算       | `a`から`b`を引いた差                               |
| ``a * b``    | 乗算       | `a`と`b`の積                                       |
| ``a / b``    | 真の除算    | `a`と`b`の商                                      |
| ``a // b``   | 切り捨て除算 | `a`と`b`の商（小数部分を取り除く）               |
| ``a % b``    | 剰余        | `a`を`b`で割った余り                              |
| ``a ** b``   | 指数       | ``a``を``b``の累乗                                 |
| ``-a``       | 負号       | ``a``の負数                                       |

演算子の優先順位は`PEMDAS`です。

PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

ビルトイン関数とは、Pythonに組み込まれている関数のことです。`def`で定義しなくても、Pythonに最初から用意されています。

- print

```
print("Hello, world!")
```

- abs

```
print(abs(-5))
# >>> 5
```

- min,max

```
print(min(1, 2, 3))
# >>> 1
print(max(1, 2, 3))
# >>> 3
```

- int, float, str

```
print(int(3.14))
# >>> 3
print(float(3))
# >>> 3.0
print(str(3.14))
# >>> '3.14'
```