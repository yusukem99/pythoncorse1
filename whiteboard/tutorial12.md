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