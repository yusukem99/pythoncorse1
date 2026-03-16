from learntools.core import *
from learntools.core.problem import injected

class ExerciseFormatTutorial(CodingProblem):
    _var = 'color'
    _hint = "あなたの好きな色は *glue* と韻を踏みます。"
    _solution = CS('color = "blue"')
    def check(self, color):
        assert color.lower() == "blue"

    @property
    def _correct_message(self):
        history = self._view.interactions
        if history['hint'] == 0 and history['solution'] == 0:
            return ("えっ！ヒントも何も使わずに正解しましたか？"
                    "やりますね。でも、ヒントの確認や解答の表示を練習するために、"
                    "次のステップにも進んでみてください。"
                    "（ここでは助けが必要ないのは明らかですが。）"
                    )
        return ''

    def _failure_message(self, var, actual, expected):
        if (
                any(actual.endswith(suff) for suff in ['oo', 'ue', 'ew'])
                and actual.strip().lower() != 'blue'
            ):
            return "ハハ、面白いですね。"
        elif actual.strip(' .!').lower() == 'ni':
            return "お願いです！もうやめて！低木を見つけてあげますから。"
        return ("{} はあなたの好きな色ではありません！"
                "まあ、本当はそうかもしれませんが、ここではルールに従ってください。"
                "この問題のポイントは、ヒントを使う練習をすることです。"
                "下のコードセルで `q0.hint()` の呼び出しのコメントを外して、"
                "あなたの*本当の*好きな色のヒントを確認してみましょう。").format(actual)


class CircleArea(EqualityCheckProblem):
    _vars = ['radius', 'area']
    _expected = [3/2, (3/2)**2 * 3.14159]

    _hint = "`a` を `b` 乗するための構文は `a ** b` です。"
    _solution = CS('radius = diameter / 2',
            'area = pi * radius ** 2')

class VariableSwap(CodingProblem):
    _vars = ['a', 'b']

    _hint = "3つ目の変数を使ってみましょう。"
    _solution = """最も分かりやすい方法は、3つ目の変数を使って一方の値を一時的に保存することです。例えば：

    tmp = a
    a = b
    b = tmp

Pythonのコードをたくさん読んだことがある人は、1行で2つの変数を入れ替える次のテクニックを見たことがあるかもしれません：

    a, b = b, a

このPythonの魔法のような書き方については、後で*タプル*について学ぶときに詳しく説明します。"""

    @injected
    def store_original_ids(self, a, b):
        self.id_a = id(a)
        self.id_b = id(b)

    def check(self, a, b):
        ida = id(a)
        idb = id(b)
        orig_values = [1, 2, 3], [3, 2, 1]
        if ida == self.id_b and idb == self.id_a:
            return
        assert not (ida == self.id_a and idb == self.id_b), ("`a` と `b` はまだ"
                "元の値のままです。")
        orig_ids = (self.id_a, self.id_b)
        if (b, a) == orig_values:
            # well this is ridiculous in its verbosity
            assert False, (
        "次のように書きましたか？\n"
        "```python\na = [3, 2, 1]\nb = [1, 2, 3]```\n?\n"
        "そう考えるのは不自然ではありませんが、2つの問題があります：\n"
        "1. `a` と `b` の値を事前に知っていることに依存しています。"
        "もし値が分からない2つの変数を入れ替えたい場合はどうしますか？\n"
        "2. このコードでは実際には `a` が *新しい* オブジェクト（`b` の以前の値と同じ値を持つ）を参照するようになり、`b` も同様です。なぜそうなるか理解するために、次のコードを考えてみましょう...\n"
        "```python\n"
        "a = [1, 2, 3]\n"
        "b = [1, 2, 3]```\n"
        "これは実際には次のコードとは*異なります*：\n"
        "```python\n"
        "a = [1, 2, 3]\n"
        "b = a```\n"
        "2番目の場合、`a` と `b` は同じオブジェクトを参照します。1番目の場合、`a` と `b` はたまたま同じ値を持つ別々のオブジェクトを参照します。これは単なる哲学的な違いに見えるかもしれませんが、オブジェクトを*変更*し始めると重要になります。2番目のシナリオで `a.append(4)` を実行すると、`a` と `b` の両方が `[1, 2, 3, 4]` になります。1番目のシナリオで `a.append(4)` を実行すると、`a` は `[1, 2, 3, 4]` になりますが、`b` は `[1, 2, 3]` のままです。（リストとミュータビリティについては後のレッスンで詳しく説明します。）"
        )
        assert ida in orig_ids, ("`a` に予期しないものが代入されました（IDが変わりましたが、"
                "`b` のIDとも異なります）")
        assert idb in orig_ids, ("`b` に予期しないものが代入されました（IDが変わりましたが、"
                "`a` のIDとも異なります）")
        assert ida != idb, "`b` と `a` が同じになっています！両方とも値は `{}` です。".format(
                repr(a))
        assert False, "予期しない方法で失敗しました！"

# It's an interesting question whether to make these parens questions checkable.
# Making them non-checkable for now.
class ArithmeticParensEasy(ThoughtExperiment):
    _hint = ('Pythonはデフォルトの「BEDMAS」のような演算順序のルールに従い、'
            'まず 3 を 2 で割り、その結果を 5 から引きます。'
            '先に引き算を行わせるには、括弧を追加する必要があります。')
    _solution = CS("(5 - 3) // 2")

class ArithmeticParensHard(ThoughtExperiment):
    _hint = '複数の括弧のペアを使う必要があるかもしれません。'
    _solution = "`(8 - 3) * (2 - (1 + 1))` が一つの解答です。他にも解答があるかもしれません。"

ArithmeticParens = MultipartProblem(ArithmeticParensEasy, ArithmeticParensHard)

class CandySplitting(EqualityCheckProblem):
    _var = 'to_smash'
    _expected = (121 + 77 + 109) % 3
    _default_values = [-1]

    _hints = [
            "剰余演算子 `%` を使うとよいでしょう。",
            "`j % k` は `j` を `k` で割った余りです。",
    ]
    _solution = CS("(alice_candies + bob_candies + carol_candies) % 3")


class MysteryExpression(EqualityCheckProblem): 
    _bonus = True
    _var = 'ninety_nine_dashes'
    _expected = 4

    _hint = ("`-` がちょうど1つだけの場合、式の値はいくつになりますか？"
            "2つの場合はどうでしょう？括弧を追加して分かりやすくできますか？")
    _solution = """元の式の値は `10` です。もし `-` を99個使った場合、式の値は 4 になります。なぜでしょうか？簡単なバージョンから始めましょう。
`7-3` はもちろん 7 から 3 を引いた 4 です。重要なのは、もう1つ `-` を追加したときに何が起こるかです。

`7--3` は `10` です。Pythonがこの式を評価する方法に合わせて括弧をつけると `7-(-3)` になります。最初の `-` は減算演算子として扱われますが、2番目の `-` は*符号の反転*として扱われます。つまり、負の3を引いている（3を足すのと同じ）ことになります。それ以降の `-` はすべて追加の符号反転として扱われるため、引かれる値は 3 と -3 の間で交互に切り替わります。したがって、`-` の数が奇数の場合、式の値は 4 になります。偶数の場合は 10 になります。
"""

class QuickdrawGridProblem(ThoughtExperiment):
    _bonus = True
    _hint = """いくつかの解法があります。これまでに学んだツールの中では、`//` と `%`（整数除算と剰余演算子）、そして `min` 関数が役立つでしょう。"""
    _solution = """一つの解答例を示します：
```python
rows = n // 8 + min(1, n % 8)
cols = min(n, 8)
height = rows * 2
width = cols * 2
```
`rows` の計算が一番難しい部分です。別の方法もあります：
```python
rows = (n + 7) // 8```
`math` モジュールはまだ紹介していませんが、天井関数（切り上げ）に馴染みがあれば、次のアプローチのほうが直感的かもしれません：
```python
import math
rows = math.ceil(n / 8)
rows = int(rows) # ceil は float を返します```
"""

class SameValueInitializationRiddle(ThoughtExperiment):
    _bonus = True
    _hints = [
            "初期化する値がintの場合、実用的な違いはほとんど見られません。しかし、他のPythonの型について考えてみてください...",
            """`a = b = <式>` は次と同等です...
```python
b = <式>
a = b```""",
    ]

    _solution = """1行で書く構文では、`a` と `b` が同じメモリアドレスを持つことになります。つまり、同じオブジェクトを参照します。これは、そのオブジェクトがリストのような**ミュータブル（変更可能）**な型の場合に重要になります。次のコードを考えてみましょう：
```python
odds = evens = []
for i in range(5):
    if (i % 2) == 0:
        evens.append(i)
    else:
        odds.append(i)
print(odds)
print(evens)```

これは `[1, 3]`、次に `[0, 2, 4]` と表示されることを期待するかもしれません。しかし実際には、`[0, 1, 2, 3, 4]` が2回連続で表示されます。`evens` と `odds` は同じオブジェクトを参照しているため、一方に要素を追加すると両方に追加されます。これは時々、頭を抱えるようなデバッグの原因になります。

もう一つの考慮点は、副作用のある式です。例えば、`list.pop` はリストの最後の要素を削除して返すメソッドです。`L = [1, 2, 3]` のとき、`a = b = L.pop()` を実行すると、`a` と `b` の両方が値 3 を持ちます。しかし、`a = L.pop()` を実行してから `b = L.pop()` を実行すると、`a` の値は 3、`b` の値は 2 になります。
"""


qvars = bind_exercises(globals(), [
    ExerciseFormatTutorial,
    CircleArea,
    VariableSwap,
    ArithmeticParens,
    CandySplitting,
    MysteryExpression,
    QuickdrawGridProblem,
    SameValueInitializationRiddle,
    ],
    start=0,
    )
__all__ = list(qvars)
