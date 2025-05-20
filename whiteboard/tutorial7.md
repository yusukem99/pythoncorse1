これまで`print`や`abs`などの組み込み関数（Pythonに最初から用意されている関数）を見てきましたが、実はPythonにはもっとたくさんの組み込み関数があります。

`round`や`len`などの関数もPythonに最初から用意されている関数です。

`abs`がどのような関数か覚えていますか？もし忘れてしまったら、`help()`関数を使ってみましょう。

```
help(round)
```

たとえば、`help`関数に、`round`関数を渡すと、次のようにこの関数の処理内容や引数を確認することができます。

```
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
```

関数のヘッダー部分に`round(number, ndigits=None)`と書いてあります。

これは、`round`関数は`number`という引数を受け取ることを示しています。

また、`ndigits=None`となっている部分は、`ndigits`という引数は省略可能で、デフォルト値は`None`であることを示しています。


`help`関数の引数には**関数の名前**を渡す必要があります。よくある間違いとして、次のように関数を実行した結果を渡してしまうことがあります。

```
help(round(-2.01))
```



Pythonは、内側の式から計算を始めます。まず、`round(-2.01)`を計算して、その結果に対して`help`関数を実行します。
そのため、`help`関数は`int`型のオブジェクトに対して実行されることになります。

```
# これと同じ
help(-2)

これらのような組み込み関数は便利ですが、自分で関数を定義することが必要になることもあります。

たとえば、3つの数値の差の最小値を求める関数はPythonには組み込まれていないので、自分で定義してみましょう。

```python
def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
```

`return`は、関数の実行をその時点でただちに終了させ、`return`の右側にある値を呼び出し元に返すためのキーワードです。

`return`の右側に続く値は、関数の戻り値と呼ばれます。

ちなみに`help`関数で`least_difference`関数を実行してみるとどうなるでしょうか？

```
help(least_difference)

>>>
Help on function least_difference in module __main__:
least_difference(a, b, c)
```

Pythonは自分で書いたコードを説明してくれるほど賢くはありません。

しかし、関数の説明を`docstring`として書いておくことで、`help`関数を使って説明を表示することができます。

```python
def least_difference(a, b, c):
    """
        a, b, cの3つの数値のうち、最小の差を返す関数
    
        >>> least_difference(1, 5, -5)
        4        
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
```

を見てきましたが、Pythonにはもっとたくさんの関数があり、自分で関数を定義することもPythonプログラミングの大きな部分です。

関数にはデフォルトの値が設定されているものもあります。`help`関数で`print`関数の説明を見てみましょう。たとえば`print`関数には`sep`という引数があります。

```
print(1, 2, 3, sep=' < ')
>>> 1 < 2 < 3
```


このように、`sep`引数に`' < '`を指定すると、出力の間に`' < '`が挿入されます。

もし`sep`引数を指定しなかった場合、デフォルト値の`' '`（半角スペース）が使われます。

```
print(1, 2, 3)
>>> 1 2 3
```


また、関数を引数として他の関数に渡すこともできます。たとえば、次のような関数を定義してみましょう。

```python
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
```