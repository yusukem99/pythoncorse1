from learntools.core import *

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    return value

class FloatToInt(ThoughtExperiment):
    _solution = ("負の小数は常に最も近い整数に切り上げられます（例えば、"
                 "-1.1 も -1.9 も -1 に切り上げられます）。正の小数は常に最も近い整数に"
                 "切り捨てられます（例えば、2.1 も 2.9 も 2 に切り捨てられます）。")
    
class MultiplyBooleans(ThoughtExperiment):
    _solution = ("整数や小数に `True` を掛けると、その数がそのまま返されます（1を掛けるのと同じです）。"
                 "`False` を掛けると、常に 0 が返されます。これは正の数でも負の数でも同じです。"
                 "文字列に `True` を掛けると、その文字列がそのまま返されます。"
                 "`False` を掛けると、空の文字列（長さゼロの文字列）が返されます。")
    
class EstimateHouseValueBool(FunctionProblem):
    _var = 'get_expected_cost'
    _test_cases = [
        ((1, 1, False), 120000),
        ((2, 1, True), 190000),
        ((3, 2, True), 230000),
        ((4, 5, False), 250000),
    ]
    _hint = ("変数 `has_basement` は `True` か `False` のどちらかです。"
             "これに 40000（地下室の価値）を掛けるとどうなるでしょうか？ "
             "分からない場合は前の問題を参照してください。")
    _solution = CS(
"""def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    return value
""")

class AddingBooleans(ThoughtExperiment):
    _solution = "ブール値を足し算すると、`False` を足すのは 0 を足すのと同じで、`True` を足すのは 1 を足すのと同じです。"
    
class CustomEngravings(FunctionProblem):
    _var = 'cost_of_project'
    _test_cases = [
        (("Charlie+Denver", True), 240),
        (("08/10/2000", False), 120),
        (("Adrian", True), 160),
        (("Ana", False), 71),
    ]
    _hint = ("選択肢は2つです。プロジェクトが純金を使うか使わないかです。これを踏まえて、解答を次のように構成できます: `cost = solid_gold * ____ + (not solid_gold) * ____`。空欄を埋める方法を考えてください。また、以下を思い出してください:\n"
             "- `solid_gold = True` の場合、`(not solid_gold) = False` であり、`solid_gold = False` の場合、`(not solid_gold) = True` です。\n"
             "- 整数に `True` を掛けるのは 1 を掛けるのと同じで、`False` を掛けるのは 0 を掛けるのと同じです。")
    _solution = CS(
"""def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost
""")


qvars = bind_exercises(globals(), [
    FloatToInt,
    MultiplyBooleans,
    EstimateHouseValueBool,
    AddingBooleans,
    CustomEngravings
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)
