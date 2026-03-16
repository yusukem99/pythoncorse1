import random

from learntools.core import *

class EarlyExitDebugging(FunctionProblem):
    _var = 'has_lucky_number'

    _test_cases = [
            ([], False),
            ([7], True),
            ([14], True),
            ([3, 14], True),
            ([3, 21, 4], True),
            ([7, 7, 7], True),
            ([3], False),
            ([3, 4, 5], False),
    ]

    _hint = ("長さnのリストに対して、ループの本体は何回実行されるでしょうか？"
            "（分からなければ、`if` の前の行に `print()` を追加して確認してみましょう。）")

    _solution = """`return` は関数を直ちに終了させることを思い出してください。つまり、元の実装ではループは1回しか実行されません。リストのすべての要素を確認して、ラッキーナンバーがないことを確認できた場合にのみ `False` を返すことができます。ただし、答えが `True` の場合は早期にリターンできます:

```python
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    # リストを全て調べたがラッキーナンバーは見つからなかった
    return False
```

Pythonの `any` 関数とリスト内包表記を使った1行バージョンもあります（`help(any)` で詳細を確認できます）:

```python
def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])
```
"""

class ElementWiseComparison(FunctionProblem):
    _var = 'elementwise_greater_than'

    _test_cases = [
            ( ([1, 2, 3, 4], 2), [False, False, True, True] ),
            ( ([1, 2, 3, 4], 5), [False, False, False, False] ),
            ( ([], 2), [] ),
            ( ([1, 1], 0), [True, True] ),
    ]

    _solution = """解法の一つを紹介します:
```python
def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res
```

リスト内包表記を使ったバージョンもあります:
```python
def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]
```
"""

class BoringMenu(FunctionProblem):
    _var = 'menu_is_boring'

    _test_cases = [
            ( ['Egg', 'Spam',], False),
            ( ['Spam', 'Eggs', 'Bacon', 'Spam'], False),
            ( ['Spam', 'Eggs', 'Spam', 'Spam', 'Bacon', 'Spam'], True),
            ( ['Spam', 'Spam'], True),
            ( ['Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top', 'Spam'], False),
            ( ['Spam'], False),
            ( [], False),
    ]

    _hint = ("この問題では、リストの要素そのものをイテレートするよりも、`range()` を使ってリストの*インデックス*をイテレートする方がよいかもしれません。インデックスでリストにアクセスする際は、「範囲外」にならないように注意しましょう（つまり、存在しないインデックスを使わないようにしましょう）。")

    # TODO: I don't think I want to mention any of the more 'clever' solutions involving zip or itertools. Though it depends on whether
    # we end up covering zip in the tutorial notebook.
    _solution = """

```python
def menu_is_boring(meals):
    # 最後の要素を除く全てのインデックスをイテレートする
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
```

この解法のポイントは `range` の呼び出しです。`range(len(meals))` を使うと `meals` の全てのインデックスが得られますが、その場合、ループの最後のイテレーションで最後の要素とその次の要素を比較しようとして... `IndexError` になってしまいます！ `range(len(meals)-1)` を使えば、最後の要素のインデックスを除く全てのインデックスが得られます。

`meals` が空かどうかをチェックする必要はないのでしょうか？実は `range(0) == range(-1)` で、どちらも空です。つまり、`meals` の長さが0または1の場合、forループは1回もイテレートされません。
"""

# Analytic solution for expected payout =
# .005 * 100 + (.05 - .005) * 5 + (.25 - .05) * 1.5
def play_slot_machine():
    r = random.random()
    if r < .005:
        return 100
    elif r < .05:
        return 5
    elif r < .25:
        return 1.5
    else:
        return 0

# TODO: Could probably make this checkable.
class ExpectedSlotsPayout(ThoughtExperiment):
    #_var = 'estimate_average_slot_payout'
    _solution = """

スロットマシンを1回引いたときの正確な期待値は0.025、つまり約2.5セントです。ほら、Python Challenge Casinoのゲームが全てプレイヤーに不利というわけではないでしょう！

この答えを得るには、`estimate_average_slot_payout(n_runs)` 関数を実装して、スロットマシンを `n_runs` 回引くシミュレーションを行う必要があります。この関数は `n_runs` 回の平均ペイアウトを返すようにします。

関数を定義したら、あとはその関数を呼び出すだけで平均ペイアウトを推定できます。

結果の分散が大きいため（非常にまれな高額ペイアウトが平均に大きく影響します）、真の期待値に近い安定した答えを得るには、`n_runs` に非常に大きな値を設定する必要があるかもしれません。例えば、`n_runs` を1000000にするとよいでしょう。

関数の実装例を示します:
```python
def estimate_average_slot_payout(n_runs):
    # スロットマシンをn_runs回プレイし、それぞれのペイアウトを計算する
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # 平均値を計算する
    avg_payout = sum(payouts) / n_runs
    return avg_payout

estimate_average_slot_payout(10000000)

```

これで0.025に近い答えが返ってくるはずです！

"""

class SlotsSurvival(FunctionProblem):
    _bonus = True
    _var = 'slots_survival_probability'
    
    _solution = CS("""def slots_survival_probability(start_balance, n_spins, n_simulations):
    # 指定回数のスピンを生き残れた回数
    successes = 0
    # Pythonでは使わない変数に '_' という名前をつける慣習があります
    for _ in range(n_simulations):
        balance = start_balance
        spins_left = n_spins
        while balance >= 1 and spins_left:
            # プレイ費用を差し引く
            balance -= 1
            balance += play_slot_machine()
            spins_left -= 1
        # 最後まで生き残れたか？
        if spins_left == 0:
            successes += 1
    return successes / n_simulations""")

    def check(self, fn):
        actual = fn(10, 10, 1000)
        assert actual == 1.0, "`slots_survival_probability(10, 10, 1000)` の結果は 1.0 になるはずですが、実際には {} でした。".format(repr(actual))

        actual = fn(1, 2, 10000)
        assert .24 <= actual <= .26, "`slots_survival_probability(1, 2, 10000)` の結果は約 .25 になるはずですが、実際には {} でした。".format(repr(actual))

        actual = fn(25, 150, 10000)
        assert .22 <= actual <= .235, "`slots_survival_probability(25, 150, 10000)` の結果は約 .228 になるはずですが、実際には {} でした。".format(repr(actual))


qvars = bind_exercises(globals(), [
    EarlyExitDebugging,
    ElementWiseComparison,
    BoringMenu,
    ExpectedSlotsPayout,
    SlotsSurvival,
    ],
)
__all__ = list(qvars) + ['play_slot_machine']
