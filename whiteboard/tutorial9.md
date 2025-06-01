# List型（Lists）

`List`型は、複数の値を一つの変数として扱うことができます。

たとえば、次の変数`primes`は4つの素数(`prime numbers`)を含んでいます。

```
primes = [2, 3, 5, 7]
```

リストに格納できるのは整数`int`型だけではなく、文字列`str`型や他の型の値も格納できます。

```
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```


リストの中に、さらにリストを入れ子にすることもできます。たとえば、ある三人のプレイヤーがそれぞれ持っているトランプの手札を表すリストは次のように書けます。
```
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # 最後のカンマは省略可能ですが、書いておくと後で要素を追加しやすいです
]
# (I could also have written this on one line, but it can get hard to read)
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
```

複数の異なる型の値をリストに格納することもできます。たとえば、次のリストは整数、文字列、関数を含んでいます。
```python
my_favourite_things = [32, 'raindrops on roses', help]
# helpは関数ですが、関数も一つの値として扱うことができますね。
```

# インデックス(Indexing)

インデックス`indexing`を使ってリストの要素にアクセスすることができます。さっき宣言した`planets`リストの要素にアクセスするには、次のように書きます。

```python
planets[0]  # 'Mercury'
planets[1]  # 'Venus'
```

地球から最も遠い惑星はどれでしょうか？インデックスに負の値を使うと、リストの末尾から数えることができます。

```python
planets[-1]  # 'Neptune'
planets[-2]  # 'Uranus'
```

# スライシング(Slicing)

スライシングを使うと、リストの一部を取り出すことができます。たとえば、次のように書くと、最初の3つの惑星を取り出すことができます。

太陽系のうち最初の3つの惑星を取り出すには、次のように書きます。

```python
first_three_planets = planets[0:3]  # ['Mercury', 'Venus', 'Earth']
```

スライシングの始点と終点は、コロン`:`で区切ります。いずれも省略可能です。

例えば次のように書くと始点の`0`を省略した場合と同じ結果になります。

```python
first_three_planets = planets[:3]  # ['Mercury', 'Venus', 'Earth']
```

地球より後の惑星を取り出すには、次のように書きます。終点を省略すると、リストの最後まで取り出すことになります。

```python
after_earth = planets[3:]  # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

# リストの要素の変更

先ほどの`planets`の中の火星を`Malacandra`に変えてみましょう。

```
planets[3] = 'Malacandra'
planets
```

惑星の名前が長いので、最初の三つの惑星の名前を３文字で表そうと思ったら、次のようにします。

```
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# もとに戻しておきます
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
```

 pythonのリストに使える関数をいくつか紹介します。

 ```
 # sorted関数を使うと、リストをソートできます。
sorted(planets)
>>>['Earth', 'Jupiter', 'Mars', 'Mercury', 'Neptune', 'Saturn', 'Uranus', 'Venus']
```

sum関数を使うと、リストの要素の合計を求めることができます。

```python
primes = [2, 3, 5, 7]
print(sum(primes))  # 17
```

max関数を使うと、リストの最大値を求めることができます。

```python
primes = [2, 3, 5, 7]
print(max(primes))  # 7
```

ところで

今まで`オブジェクト`という言葉を時々使ってきました。

Pythonでは、すべての値は`オブジェクト`です。リストもオブジェクトの一種ですし、整数や文字列もオブジェクトです。

オブジェクトは、いくつかの関数や変数をひとまとめにしたものです。`.`を使うと、オブジェクトの関数や変数にアクセスできます。

例えば、実はpythonの整数オブジェクトは`imag`という変数を持っています。これは整数の虚数部を表します。

```python

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)
```

また、整数は`bit_length`というメソッドを持っています。これは整数のビット長を返します。

```python
x = 12
print(x.bit_length())  # 4
```

メソッドについても関数と同じように`help`関数を使って調べることができます。

```python
help(x.bit_length)

Help on built-in function bit_length:

bit_length() method of builtins.int instance
    Number of bits necessary to represent self in binary.
    
    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6
```

話をリストに戻しましょう。リストには、いくつかの便利なメソッドがあります。

例えば、`append`メソッドを使うと、リストの末尾に要素を追加することができます。

```python
planets.append('Pluto')
print(planets)  # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
```

`pop`メソッドを使うと、リストの末尾の要素を取り出して削除することができます。

```python
last_planet = planets.pop()
print(last_planet)  # 'Pluto'
print(planets)  # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```


`index`メソッドを使うと、リストの中から特定の要素のインデックスを取得することができます。

```python
index_of_earth = planets.index('Earth')
print(index_of_earth)  # 2
```

今、`planets`リストの中に`Earth`がありますが、それを確かめるために`in`演算子を使うこともできます。

```python
is_earth_in_planets = 'Earth' in planets
print(is_earth_in_planets)  # True
```

```
# Is Calbefraques a planet?
is_calbefraques_a_planet = 'Calbefraques' in planets
print(is_calbefraques_a_planet)  # False
```

# タプル
`Tuple`型は、リストと似ていますが、変更できない（immutable）点が異なります。

```
t = (1, 2, 3)
```

```
t = `1, 2, 3`  # タプルはカンマで区切られた値の並びで表現できます
```
タプルは、リストと同様に複数の値を一つの変数として扱うことができますが、要素を変更することはできません。

タプルを使うと便利な場面もあります。例えば、関数の戻り値として複数の値を返す場合にタプルを使うことができます。

```
a = 1
b = 0
a, b = b, a  # タプルを使ってaとbの値を入れ替えることができます
print(a, b)  # 0 1
```