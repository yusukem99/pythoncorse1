# 外部ライブラリの使い方

実際の開発では、Pythonの標準ライブラリ以外にも、様々な外部ライブラリを使うことになります。

ここでは`import`文を使って外部ライブラリを読み込む方法を紹介します。さらに、オペレータを上書きする方法についても触れます。

# import文

pythonが最も人気のプログラミング言語の一つである理由の一つは、高品質で多機能な外部ライブラリが豊富に存在することです。

これまで扱ってきた`max`, `min`, `sum`などの関数は、Pythonの標準ライブラリと呼ばれる、Pythonに最初から組み込まれているものでしたが、外部ライブラリを使う際は、`import`文を使ってライブラリを読み込みます。

例えば、円周率や三角関数などの数学的な計算を行うための`math`ライブラリを使う場合は、次のようにします。

```
import math

print("It's math! It has type {}".format(type(math)))

>>> It's math! It has type <class 'module'>
```

`matth`の型は`module`となっています。モジュールというのは、Pythonのコードをまとめたもので、関数や変数の集まりです。

`dir()`関数を使って`math`モジュールの中にどのような関数や変数があるかを確認してみましょう。

```
print(dir(math))
>>> ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
```

これらの変数や関数にアクセスするときは、モジュール名の後にドット`.`を付けます。例えば、円周率(`pi`)を使いたい場合は次のようにします。

```print(math.pi)
>>> 3.141592653589793
```

対数を扱う関数`log()`を使う場合は、次のようにします。

```
math.log(32, 2)
>>> 5.0
```

詳しい使い方を知りたい場合は`help()`関数を使いましょう。

```
help(math.log)

>>>
Help on built-in function log in module math:

log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.
```

`math`ライブラリの全部のドキュメントを読みたい場合は

```
help(math)
```

のようにします。

# エイリアス

もし`math`モジュールを頻繁に使う場合、毎回`math.`と書くのは面倒です。そこで、エイリアスを使うことができます。

```
import math as mt
mt.pi

>>>3.141592653589793
```


mathモジュールの関数を`math.`と書くのが面倒な場合は、`**`を使って全ての値をインポートすることもできます。

```
from math import *
print(pi, log(32, 2))

>>> 3.141592653589793 5.0
```

ただし、これは注意が必要です。なぜなら、他のモジュールと名前が衝突する可能性があるからです。

```
from math import *
from numpy import *
print(pi, log(32, 2))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_19/3018510453.py in <module>
      1 from math import *
      2 from numpy import *
----> 3 print(pi, log(32, 2))

TypeError: return arrays must be of ArrayType
```

このエラーの原因はなんでしょうか？実は、`numpy`モジュールにも`pi`や`log`という名前の関数が存在するためです。
そのため、`math`モジュールの`pi`や`log`が上書きされてしまい、`numpy`の関数が呼び出されてしまいます。
このような名前の衝突を避けるためには、必要な関数だけをインポートするようにしましょう。

```
from math import log, pi
from numpy import asarray
print(pi, log(32, 2))

>>> 3.141592653589793 5.0
```

# サブモジュール

オブジェクトの子のオブジェクトに、さらに子のオブジェクトを持つことがあります。その場合は`.`を繰り返し使ってアクセスします。

```
# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
rolls

>>> array([3, 4, 3, 4, 5, 5, 2, 1, 3, 3])
```

# わからなくなった時には

高機能なライブラリは、非常に多くの関数や変数を持っています。そのため、どのように使うか分からなくなったら次の方法で調べてみましょう。

1. `type()`関数を使って、オブジェクトの型を確認する。

```
type(rolls)

>>> <class 'numpy.ndarray'>
```

2. `dir()`関数を使って、オブジェクトの中にどのような関数や変数があるかを確認する。

```
dir(rolls)
>>> ['T', '__abs__', '__add__', '__and__', '__array____', '__array_priority__', '__array_ufunc__', '__array_function__', '__array_interface__', '__array_struct__', '__array_wrap__', '__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__int__', '__invert__', '__le__'
```

3. `help()`関数を使って、特定の関数や変数の使い方を確認する。

```
help(rolls.sum)
>>> Help on built-in function sum:
sum(...)
    sum(a, axis=None, dtype=None, out=None, keepdims=<no value>)
    Sum of array elements over a given axis.
    Returns the sum of the array elements over the given axis.     
    The sum of an empty array is the neutral element 0.
```

# オペレータの上書き

```
[3, 4, 1, 2, 2, 1] + 10
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_19/2144087748.py in <module>
----> 1 [3, 4, 1, 2, 2, 1] + 10

TypeError: can only concatenate list (not "int") to list
```

リストに整数を加えるとエラーが出ます。これは、`list`型を作ったPythonの開発者が、リストに整数を加えることを意図していないためです。

一方で、NumPyの配列は、要素ごとに演算を行うことができます。NumPyはそのような演算を行うために、オペレータを上書きして作られているからです。

```
rolls + 10

>>> array([13, 14, 13, 14, 15, 15, 12, 11, 13, 13])
```

オペレータを上書きするためには、`__add__`や`__sub__`などの特殊メソッドを定義します。これにより、`+`や`-`などの演算子を使ってオブジェクト同士の演算が可能になります。これは別のレッスンで詳しく学ぶことにします。