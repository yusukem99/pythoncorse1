import random

from learntools.core import *

import learntools.python.solns.jimmygraph as jg_module
import learntools.python.solns.blackjack_gt as bj_module
hand_gt_soln = bj_module.blackjack_hand_greater_than

class JimmySlots(ThoughtExperiment):
    _solution = CS.load(jg_module.__file__)

class LuigiAnalysis(ThoughtExperiment):
    _hint = ("いくつか考えてみましょう:\n\n"
            "- 変数 `i` の型は何でしょうか？\n"
            "- インポートした `full_dataset` リストを調べるとどうなるでしょうか？"
            "（心配しないでください、実際にはそれほど大きくありません。）"
            "エラーの原因となっているレーサーを見つけられますか？"
            )

    _solution = '''Luigiは racer['items'] の各要素を表すために変数名 `i` を使っていました。
しかし、外側のループ（`for i in range(len(racers))`）でもループ変数として `i` を使っていました。
この2つの `i` がお互いを上書きしてしまいます。これが問題になるのは、finish が 1 で name が `None` のレーサーに遭遇した場合だけです。その場合、"WARNING" メッセージを表示しようとすると、`i` は "green shell" のような文字列を参照しており、Pythonは文字列と整数を加算できないため、`TypeError` が発生します。

これは `math` と `numpy` から `*` でインポートしたときに見た問題と似ています。どちらにも `log` という変数があり、呼び出そうとしたときに間違った方が使われてしまいました。

内側と外側のループで異なるループ変数を使うことで修正できます。そもそも `i` は内側のループの変数名としてあまり適切ではありませんでした。`for item in racer['items']` に変更すれば、バグが修正され、コードも読みやすくなります。

このような変数のシャドウイングバグはそれほど頻繁には起こりませんが、起きたときは原因の特定に非常に時間がかかることがあります！
'''

def gen_bj_hand():
    cards = list(map(str, range(2, 11))) + ['J', 'Q', 'K', 'A']
    ncards = random.randint(1, 6)
    hand = [random.choice(cards) for _ in range(ncards)]
    return hand

def gen_bj_inputs(n):
    random.seed(1)
    return [
            (gen_bj_hand(), gen_bj_hand())
            for _ in range(n)
            ]

class BlackjackCmp(FunctionProblem):
    _var = 'blackjack_hand_greater_than'
    _hint = ("この問題は、少なくとも1つの「ヘルパー関数」を定義すると解きやすくなります。"
            "手札の合計ポイントを計算するロジックは、ヘルパー関数に切り出す良い候補です。"
            )
    _solution = CS.load(bj_module.__file__)

    # TODO: explicitly make sure to test multi-ace cases. e.g. [K, A, A]
    _test_cases = [
            (args, hand_gt_soln(*args))
            for args in gen_bj_inputs(100)
            ]


qvars = bind_exercises(globals(), [
    JimmySlots,
    LuigiAnalysis,
    BlackjackCmp,
    None,
    ],
    start=1,
)
__all__ = list(qvars)
