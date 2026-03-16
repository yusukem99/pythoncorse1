from learntools.core import *
from learntools.core.exceptions import Incorrect

class RoundFunctionProblem(FunctionProblem):
    _var = 'round_to_two_places'

    _test_cases = [
            (1.000001, 1.00),
            (1.23456, 1.23),
    ]
    _hint = ("コンソール（またはコードセル）で `help(round)` を実行して、round関数について詳しく調べてみましょう。"
            "この関数のオプションの第2引数を使う必要があります。")
    _solution = CS("return round(num, 2)")

class RoundNdigitsProblem(ThoughtExperiment):

    _solution = """これまで見てきたように、`ndigits=-1` は10の位に丸め、`ndigits=-2` は100の位に丸めます。これはどんな場面で便利でしょうか？大きな数を扱う場合を考えてみましょう：

> フィンランドの面積は 338,424 km²
> グリーンランドの面積は 2,166,086 km²

実際に 338,424 なのか、338,425 なのか、338,177 なのかはあまり気にしないでしょう。細かい桁の精度は邪魔なだけです。`round()` を `ndigits=-3` で呼び出すことで切り落とせます：

> フィンランドの面積は 338,000 km²
> グリーンランドの面積は 2,166,000 km²

（カンマの表示方法については、後で文字列のフォーマットについて学ぶときに説明します。）
"""

class PrintPrintProblem(ThoughtExperiment):

    _hint = "チュートリアルで `help(abs(-2))` を呼び出したときに何が起きたか思い出してみましょう。"

    _solution = """コードを実行してみると、次のように表示されることが分かります：

    Spam
    None

何が起きているのでしょうか？内側の `print` 関数の呼び出しは、当然文字列 "Spam" を表示します。外側の呼び出しは、`print` 関数の戻り値を表示します。そしてその戻り値は `None` です。

なぜこの順序で表示されるのでしょうか？*Pythonは関数を実行する前に、その引数を先に評価します*。つまり、入れ子になった関数呼び出しは内側から外側に向かって評価されます。Pythonは外側の `print` に渡す値を知るために、まず `print("Spam")` を実行する必要があるのです。"""

class CandySmashingFunctionProblem(FunctionProblem):
    _var = 'to_smash'

    _test_cases = [
           ((10, 2), 0),
           ((10, 3), 1),
           ((10, 4), 2),
           (10, 1),
           (9, 0),
           ((10, 10), 0),
           ((10, 11), 10),
            ]
    _hint = "前回のチュートリアルノートブックで、デフォルト引数について説明したセクションを参照してください。"
    _solution = CS(
"""def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends""")

    def check(self, fn):
        try:
            x = fn(10, 2)
        except TypeError:
            raise Incorrect("`to_smash` は2つの引数で呼び出せる必要があります（例：`to_smash(10, 2)`）")
        try:
            x = fn(10)
        except TypeError:
            raise Incorrect("`to_smash` は1つの引数で呼び出せる必要があります（例：`to_smash(10)`）")
        super().check(fn)

# How the heck to test this?
class TimeCallProblem(ThoughtExperiment):
    _var = 'time_call'

    _hint = "実行時間を測定するために、入力された関数を呼び出す前後で `time()` を呼び出す必要があります。テストには `sleep` 関数がとても役立ちます。"
    # TODO: Write out the whole function
    _solution = '''関数本体の例：
```python
t0 = time()
fn(arg)
t1 = time()
elapsed = t1 - t0
return elapsed
```
関数をテストするには、`time_call(sleep, 2)` のように実行して、戻り値が 2 に近いことを確認しましょう。
'''

class SlowestCallProblem(ThoughtExperiment):
    _hint = "`slowest_call` の本体で、前の問題で書いた関数（`time_call`）を呼び出すとよいでしょう。"
    _solution = """
```python
return max(time_call(fn, arg1), time_call(fn, arg2), time_call(fn, arg3))
```

`time_call` で書いたコードを3回コピー&ペーストして少し変数を変えることも*できます*が、あまりお勧めしません。タイピング量が増えますし、後で `time_call` にバグを見つけた場合、4箇所で修正が必要になります。[怠惰はプログラマーの三大美徳の一つです。](http://threevirtues.com/)
"""

class SmallestStringyDebug(ThoughtExperiment):
    _solution = (
"""`smallest_stringy_number('10', '2', '3')` は失敗する例の一つです。'2' ではなく '10' が返されます。

問題は、`min` を文字列に適用すると、Pythonは数値としての値ではなく、*辞書順*（辞書や電話帳の並び順のようなロジック）で最も早いものを返すことです。
""")

class SmallestStringyFix(FunctionProblem):
    _var = 'smallest_stringy_number'
    
    _test_cases =  [
            ( ('1', '2', '3'), '1'),
            ( ('10', '2', '3'), '2'),
            ( ('2', '3', '10'), '2'),
            ( ('-100', '10', '5'), '-100'),
            ]

    _hint = "`min` にはオプションで `key` 引数を渡すことができ、比較する前に各要素に適用する関数を指定できることを思い出しましょう。"
    _solution = CS('return min(s1, s2, s3, key=int)')

SmallestStringyProblem = MultipartProblem(SmallestStringyDebug,
        SmallestStringyFix)

qvars = bind_exercises(globals(), [
    RoundFunctionProblem,
    RoundNdigitsProblem,
    CandySmashingFunctionProblem,
    None, # Reading exceptions
    TimeCallProblem,
    SlowestCallProblem,
    PrintPrintProblem,
    SmallestStringyProblem,
    ],
)
__all__ = list(qvars)
