import inspect

from learntools.core import *
from learntools.core.problem import injected
from learntools.core.exceptions import Uncheckable
from learntools.core.utils import format_args

from learntools.python.blackjack import BlackJack

class SignFunctionProblem(FunctionProblem):
    _var = 'sign'

    _test_cases = [
            (-1, -1),
            (-100, -1),
            (-.001, -1),
            (0, 0),
            (0.0, 0),
            (0.001, 1),
            (1, 1),
            (1812, 1),
    ]

    _solution = CS(
"""def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0""")


# TODO: could try to intercept stdout to actually check this I guess?
class PluralizationProblem(ThoughtExperiment):

    _solution = """分かりやすい（そして全く問題ない）解法は、元の `print` の呼び出しを次のように置き換えることです：

```python
if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")
```

条件式を使ったもう少し簡潔な解法もあります：

```python
print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")
```"""

class WeatherDebug(EqualityCheckProblem):

    _vars = ['have_umbrella', 'rain_level', 'have_hood', 'is_workday']
    # Default EqualityCheckProblem logic says that if any vars haven't changed
    # from their initial/default values then the problem isn't attempted. Which
    # doesn't work here...
    #_default_values = [True, 0.0, True, True]

    _hint = ("メインレッスンで元の式をどう修正したかを見直してみましょう。"
            "特定の部分式に括弧を追加しましたね。"
            "このコードのバグは、Pythonが特定の演算を「間違った」順序で評価することが原因です。")

    _solution = """失敗するテストケースの一例です：

```python
have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False
```

この場合、明らかに天気に対する準備はできています。雨は降っていません。それだけでなく、仕事の日でもないので、家を出る必要すらありません！しかし、この関数はこれらの入力に対して False を返してしまいます。

重要な問題は、Pythonが最後の部分を暗黙的に次のように括弧をつけることです：

```python
(not (rain_level > 0)) and is_workday
```

一方、私たちが表現しようとしていたのは次のような意味です：

```python
not (rain_level > 0 and is_workday)
```
"""

    @staticmethod
    def canonical_prepared(have_umbrella, rain_level, have_hood, is_workday):
        return (have_umbrella or
                       (rain_level < 5 and have_hood) or
                        not (rain_level > 0 and is_workday)
                       )
    @staticmethod
    def ill_prepared(have_umbrella, rain_level, have_hood, is_workday):
        return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

    def check(self, *args):
        expected = self.canonical_prepared(*args)
        actual = self.ill_prepared(*args)
        assert actual != expected, ("{} を入力した場合、`prepared_for_weather` は"
                " `{}` を返しました。しかし、それは正しい結果だと思います。"
                "（`prepared_for_weather` が間違った結果を返すような入力を見つけてください。）").format(
                        format_args(self.ill_prepared, args),
                        repr(actual),
                        )


class ConciseIsNegative(FunctionProblem):
    # NB: looks like there's no clean way to check for single-line-ness. 
    # But they'll know whether they've accomplished it or not, and there's not much
    # point in cheating.

    _var = 'concise_is_negative'

    _test_cases = [
            (1, False),
            (0, False),
            (-100, True),
    ]

    _hint = ("式 `number < 0` の値が `True` なら `True` を返し、"
            "`False` なら `False` を返すということは...")
    _solution = CS("return number < 0")

class AllToppings(FunctionProblem):
    _var = 'wants_all_toppings'

    _hint = "`and` 演算子を使う必要があります。"
    _solution = CS("return ketchup and mustard and onion")

    _test_cases = [
            ((True, True, True), True),
            ((False, True, True), False),
            ((False, False, False), False),
            ((True, False, True), False),
            ((True, True, False), False),
    ]

class PlainDog(FunctionProblem):
    _var = 'wants_plain_hotdog'

    _hint = "`not` 演算子を使う必要があります。"
    _solution = (
"""一つの解法は次のとおりです：
```python
return not ketchup and not mustard and not onion
```

[ド・モルガンの法則](https://ja.wikipedia.org/wiki/%E3%83%89%E3%83%BB%E3%83%A2%E3%83%AB%E3%82%AC%E3%83%B3%E3%81%AE%E6%B3%95%E5%89%87)を使って not を「くくり出す」こともできます：

```python
return not (ketchup or mustard or onion)
```""")

    _test_cases = [
            ((True, True, True), False),
            ((False, True, True), False),
            ((False, False, False), True),
            ((True, False, True), False),
            ((False, False, True), False),
            ((False, True, False), False),
    ]

class OneSauce(FunctionProblem):
    _var = 'exactly_one_sauce'

    _hint = ("これを true にするために ketchup と mustard を設定する方法は"
            "ちょうど2通りあります。それは何でしょうか？"
            )
    _solution = CS("return (ketchup and not mustard) or (mustard and not ketchup)")

    _test_cases = [
            ((True, True, True), False),
            ((False, True, True), True),
            ((False, False, False), False),
            ((True, False, True), True),
    ]

HotDogGauntlet = MultipartProblem(
        AllToppings, PlainDog, OneSauce,
        )

class OneTopping(FunctionProblem):
    _var = 'exactly_one_topping'

    _hint = ("`int(True)` が 1 で、`int(False)` が 0 であることは既にご存知かもしれません。"
            "`ketchup`、`mustard`、`onion` を整数に変換した後、"
            "どのような基本的な算術演算を行えばよいか考えてみましょう。"
            )
    _solution = ("""この条件を `and`、`or`、`not` だけで表現するのはかなり複雑になりますが、ブール値から整数への変換を使えば、次のような短い解法が得られます：
```python
return (int(ketchup) + int(mustard) + int(onion)) == 1
```

豆知識：技術的には引数に `int` を呼び出す必要はありません。ブール値で足し算をするだけで、Pythonが暗黙的に整数変換を行います。したがって、次のようにも書けます...

```python
return (ketchup + mustard + onion) == 1
```""")
    
    _test_cases = [
            ((True, True, True), False),
            ((False, True, True), False),
            ((False, False, False), False),
            ((True, False, True), False),
            ((False, False, True), True),
    ]

class BlackJackProblem(CodingProblem):
    _counts_for_points = False
    _var = 'should_hit'


    def check(self, should_hit):
        raise Uncheckable

    def is_legacy(self, phit):
        # Check for old call signature of should_hit
        # i.e. should_hit(player_total, dealer_total, player_aces):
        sig = inspect.signature(phit)
        nparams = len(sig.parameters)
        assert nparams in (3, 4), ("should_hit の呼び出しシグネチャが予期しないものです："
                " `{}`\n（パラメータを追加または削除しましたか？）").format(
                        ', '.join(sig.parameters.keys())
                        )
        return nparams == 3


    @injected
    def simulate_one_game(self, phit):
        game = BlackJack(phit, True, self.is_legacy(phit))
        game.play()

    @injected
    def simulate(self, phit, n_games=100):
        wins = 0
        legacy = self.is_legacy(phit)
        for _ in range(n_games):
            wins += 1 == BlackJack(phit, legacy=legacy).play()
        print("プレイヤーは {} ゲーム中 {} 勝しました（勝率 = {:.1%}）".format(
            n_games, wins, wins/n_games
            ))

qvars = bind_exercises(globals(), [
    SignFunctionProblem,
    PluralizationProblem,
    WeatherDebug,
    ConciseIsNegative,
    HotDogGauntlet,
    OneTopping,
    BlackJackProblem,
    ],
)
__all__ = list(qvars)
