# 文字列と辞書型

# 文字列の宣言

これまでたくさんの文字列型を使ってきましたが、文字列は次のようにシングルクォート`'`またはダブルクォート`"`で囲むことで宣言できます。

どちらを使っても全く同じなので、比較演算子`==`を使って確認してみましょう。

```
x = 'Pluto is a planet'
y = "Pluto is a planet"
x == y
>>> True
```

扱いたい文字列の中にシングルクォート`'`が含まれている場合は、ダブルクォート`"`で囲むと便利です。その逆も同様です。

```
print("Pluto's a planet!")
print('My dog is named "Pluto"')

>>> Pluto's a planet!
>>>> My dog is named "Pluto"
```

シングルクォートとダブルクォートを混ぜて使うと、次のようなエラーになります。

```
'Pluto's a planet!'

  File "/tmp/ipykernel_19/1561186517.py", line 1
    'Pluto's a planet!'
           ^
SyntaxError: invalid syntax
```

シングルクォートを文字列の中で使いたい場合は、エスケープシーケンスを使います。

バックスラッシュ`\`をエスケープしたい文字の前に付けることで、その文字を特別な意味を持たない文字として扱います。

```
'Pluto\'s a planet!'
>>> "Pluto's a planet!"
```

The table below summarizes some important uses of the backslash character.

| 入力 | 出力 | 例 | printすると |
| --- | --- | --- | --- |
| `\'` | `'` | `'What's up?'` | What's up? |
| `\"` | `"` | `"That's \"cool\""` | That's "cool" |
| `\\` | `\` | `"Look, a mountain: /\\ "` | Look, a mountain: /\ |
| `\n` | 改行 | `"1\n2 3"` | 1<br>2 3 |


次のように、文字列の中に改行を含めるとprintしたときに改行されます。
```
hello = "hello\nworld"
print(hello)
>>> hello
>>> world
```

`docstring`で使用したトリプルクォートを使うと、複数行の文字列を簡単に書くことができます。

```
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
triplequoted_hello == hello
>>> True
```

文字列はシーケンスなので、リストのようにインデックスを使って特定の文字を取得することができます。

```
# Indexing
planet = 'Pluto'
planet[0]

>>> 'P'
```

```
# スライシング
planet[-3:]

>>> 'uto'
```

```
# len関数を使うと、文字列の長さを取得できます
len(planet)
>>> 5
```

```
# ループを使って文字列の各文字を出力することもできます
[char+'! ' for char in planet]
['P! ', 'l! ', 'u! ', 't! ', 'o! ']
```

ただし、文字列はイミュータブル（変更不可）なので、要素を変更することはできません。

```
planet[0] = 'B'

# planet.appendも使えません
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_19/2683731249.py in <module>
----> 1 planet[0] = 'B'
      2 # planet.append doesn't work either

TypeError: 'str' object does not support item assignment
```

# 文字列型のメソッド

`upper()`を使うと、文字列をすべて大文字に変換できます。

```
claim = "Pluto is a planet!"
claim.upper()

>>> 'PLUTO IS A PLANET!'
```

`lower()`を使うと、文字列をすべて小文字に変換できます。

```
# all lowercase
claim.lower()
>>> 'pluto is a planet!'
```

`index()`を使うと、文字列の中で特定の文字列が最初に出現する位置を取得できます。

```
# Searching for the first index of a substring
claim.index('plan')
>>> 11
```

`startswith()`を使うと、文字列が特定の文字列で始まるかどうかを確認できます。

```
claim.startswith(planet)
>>> True
```

`endswith()`を使うと、文字列が特定の文字列で終わるかどうかを確認できます。

```
# false because of missing exclamation mark
claim.endswith('planet')
>>> False
```

`split()`を使うと、文字列を特定の区切り文字で分割してリストに変換できます。

```
words = claim.split()
words

>>> ['Pluto', 'is', 'a', 'planet!']
```

空白文字で分割するのがデフォルトですが、他の文字で分割することもできます。

```
datestr = '1956-01-31'
year, month, day = datestr.split('-')
```

`join()`を使うと、リストの要素を特定の文字列で結合して一つの文字列にすることができます。

```
'/'.join([month, day, year])
>>> '01/31/1956'
```

# 辞書型

辞書型は、値とキーが紐づいた構造の型です。例えば次の例は`one`, `two`, `three`というキーに対して、それぞれ1, 2, 3という整数値が紐づいています。

```
numbers = {'one':1, 'two':2, 'three':3}
```

値を取り出す際は、次のように変数名の後に角括弧`[]`を使ってキーを指定します。

```
numbers['one']
>>> 1
```

新しいキーを追加するには次のようにします。

```
numbers['eleven'] = 11
numbers

>>> {'one': 1, 'two': 2, 'three': 3, 'eleven': 11}
```

すでに存在するキーの値を変更することもできます。

```
numbers['one'] = 'Pluto'
numbers
>>> {'one': 'Pluto', 'two': 2, 'three': 3, 'eleven': 11}
```


辞書型は`イテラブル`なので、ループを使ってキーと値を取り出すことができます。

```
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial
>>>
{'Mercury': 'M',
 'Venus': 'V',
 'Earth': 'E',
 'Mars': 'M',
 'Jupiter': 'J',
 'Saturn': 'S',
 'Uranus': 'U',
 'Neptune': 'N'}
```

`in`を使って特定のキーが辞書に存在するかどうかを確認できます。

```
'Saturn' in planet_to_initial
>>> True
```


辞書型のキーを一覧で取り出したい場合は、`keys()`メソッドを使うことができます。値の一覧が欲しい場合は`values()`が使えます。

```
# Get all the initials, sort them alphabetically, and put them in a space-separated string.
' '.join(sorted(planet_to_initial.values()))
>>> 'E J M M N S U V'
```

値とキーのペアでそれぞれ取り出したい場合は`items()`を使ってイテレートします。

```
The very useful dict.items() method lets us iterate over the keys and values of a dictionary simultaneously. (In Python jargon, an item refers to a key, value pair)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))

>>>
   Mercury begins with "M"
     Venus begins with "V"
     Earth begins with "E"
      Mars begins with "M"
   Jupiter begins with "J"
    Saturn begins with "S"
    Uranus begins with "U"
   Neptune begins with "N"
```