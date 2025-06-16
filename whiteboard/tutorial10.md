# ループとリスト内包表現

# ループ

プログラミングでは、繰り返し処理を行う時は、ループ（for文）を使います。

```
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end=' ') # print all on same line

>>> Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune 
```

for文では、`in`の後ろに処理を行う対象を指定します。

ここでは、`planets`リストの要素を一つずつ取り出して、`planet`という変数に代入し、`print`関数で出力しています。

`for`の後ろに書いた`planet`は、ループの中で使う変数名です。関数のように、最後にコロン`:`を付けて、ループの本体をインデントして書きます。

ループの本体が、対象の要素の数だけ繰り返されます。


`in`の後ろには`イテレート可能なオブジェクト`（イテラブル）を指定します。タプルもイテラブルです。

```
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
product

>>> 360
```

実は文字もイテラブルです。文字列の各文字を一つずつ取り出すことができます。

```
s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')    

>>>HELLO
```

ステガノグラフィとは、あるデータの中に別の情報を埋め込んで隠ぺいする技術です。


`range`関数を使うと、指定した範囲の整数のシーケンスを生成できます。指定の回数分だけ繰り返し処理を行う時に便利です。

```
for i in range(5):
    print("Doing important work. i =", i)

>>> Doing important work. i = 0
>>> Doing important work. i = 1
>>> Doing important work. i = 2
>>> Doing important work. i = 3
>>> Doing important work. i = 4
```


`while`文を使ってもループを作ることができます。`while`文は、条件が真である限り繰り返し処理を行います。

ここでは、`i`が10未満の間、`i`の値を出力し、`i`を1ずつ増やしていきます。

```
i = 0
while i < 10:
    print(i, end=' ')
    i += 1 # increase the value of i by 1
```

# リスト内包表現(List Comprehensions)

リスト内包表記はPython特有のとても便利な機能で、for文を使って値を生成する際に、簡潔に書くことができます。

たとえば、次のように書くと、0から9までの整数の二乗を計算してリストを作成できます。

```
squares = [n**2 for n in range(10)]
squares

>>> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```


上のリスト内包表記は、次のfor文と同じ意味になります。

```
squares = []
for n in range(10):
    squares.append(n**2)
squares
```

さらに、リスト内包表記に条件分（if文）を追加することもできます。例えば、先ほどの惑星の名前のリストから、名前が6文字未満の惑星だけを取り出すには、次のように書きます。

```
short_planets = [planet for planet in planets if len(planet) < 6]
short_planets

>>> ['Venus', 'Earth', 'Mars']
```


`for`の後ろに書いた値が新たなリストの値になるので、次のように書くこともできます。

```
# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets

>>> ['VENUS!', 'EARTH!', 'MARS!']
```


通常は上のようにリスト内包表記は一行で書きますが、わかりやすく構造を示すために、複数行に分けて書くこともできます。

```
[
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]

>>> ['VENUS!', 'EARTH!', 'MARS!']
```


次の例は、現実的にはあまり使わないかもしれませんが、リスト内包表記の書き方を示すために書いています。
これはどのようなリストが生成されるのでしょうか？実際に試してみてください。

```
[32 for planet in planets]
```

リスト内包表記と、`min`や`max`などの組み込み関数を組み合わせることもできます。

たとえば次のような、与えられた引数`nums`の中から負の数の個数を数える関数を考えます。

```
def count_negatives(nums):
    """Return the number of negative numbers in the given list.
    
    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative
```


これは次のようにリスト内包表記を使って簡潔に書くことができます。

```
def count_negatives(nums):
    return len([num for num in nums if num < 0])
```

コードは短ければ短い方がいい、と考えるなら、次のように書くこともできますね。

```
def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])
```

どの書き方が一番良いかは、主観的なもので意見が分かれますが、次の「Pythonの禅」を読んでみましょう。
]

[Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)

次のようなことがかかれています。
```
Readability counts. 読みやすさは重要だ。
Explicit is better than implicit. 明示的な方が暗黙的なものより良い。
```
