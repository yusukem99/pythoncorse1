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

```python









真偽型（Booleans）

Pythonは、真偽値（TrueまたはFalse）を表すために`bool`型を使用します。

`bool`型は、条件式の結果や論理演算の結果を表すために使用されます。Pythonでは、`True`と`False`の2つの値しか持ちません。

```python
# 真偽値の例
x = True
print(x)  # True
print(type(x))  # <class 'bool'>
```

実際には、`True`や`False`を直接コードに書くことは少なく、比較演算子を使って真偽値を得ることが多いです。以下に、いくつかの比較演算子を示します。

// テーブル
| 演算子 | 説明                     | 演算子 | 説明                      |
|--------|--------------------------|--------|---------------------------|
| `a == b` | aがbに等しい             | `a != b` | aがbに等しくない          |
| `a < b`  | aがbより小さい           | `a > b`  | aがbより大きい            |
| `a <= b` | aがb以下                 | `a >= b` | aがb以上                  |


アメリカ合衆国の憲法では、大統領に立候補するためには35歳以上である必要があります。以下の関数は、与えられた年齢が35歳以上かどうかを判定します。

```python
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    # The US Constitution says you must be at least 35 years old
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))
```


比較演算子は、期待通りに動作することが多いですが、時には予想外の結果になることもあります。

```python
# 3.0は3と等しい
print(3.0 == 3)  # True
# '3'は3と等しくない
print('3' == 3)  # False
```

比較演算子は、算術演算子と組み合わせて使うこともできます。

例えば、数が奇数かどうかを判定する関数は以下のように書けます。

```python
def is_odd(n):
    return (n % 2) == 1
print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))
```

`==`と`=`を混同しないように注意してください。

`n == 2`はの値が2であるかを判定し`True`または`False`を返しますが、`n = 2`はnの値を2に設定することを意味します。 

複数の条件を組み合わせることもできます。

アメリカ合衆国の大統領に立候補するためには35歳以上である必要があるということでしたが、さらにアメリカ合衆国で生まれた人である必要もあります。

以下の関数は、年齢と市民権の状態を考慮して、大統領に立候補できるかどうかを判定します。

```python

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35)

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

```