from learntools.core import *
import math

def get_expected_cost(beds, baths):
    value = 80000 + 30000 * beds + 10000 * baths
    return value

def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

class GetExpectedCost(FunctionProblem):
    _var = 'get_expected_cost'
    _test_cases = [
        ((0, 0), 80000),
        ((0, 1), 90000),
        ((1, 0), 110000),
        ((1, 1), 120000),
        ((1, 2), 130000),
        ((2, 3), 170000),
        ((3, 2), 190000),
        ((3, 3), 200000),
        ((3, 4), 210000),
    ]
    _hint = ("この値は、基本価格（`80000`）に、ベッドルームの合計価格（`30000 * beds`）と"
             "バスルームの合計価格（`10000 * baths`）を足したものになります。")
    _solution = CS(
"""
def get_expected_cost(beds, baths):
    value = 80000 + 30000 * beds + 10000 * baths
    return value
""")
    
class RunGetExpectedCost(EqualityCheckProblem):
    _vars = ['option_one', 'option_two', 'option_three', 'option_four']
    _expected = [get_expected_cost(2, 3), get_expected_cost(3, 2), get_expected_cost(3, 3), get_expected_cost(3, 4)]
    _hint = ("もし `option_five` に5つのベッドルームと3つのバスルームを持つ家の"
             "予想価格を設定する必要がある場合は、`option_five = get_expected_cost(5, 3)` と書きます。")
    _solution = CS(
"""# get_expected_cost 関数を使用して、それぞれの値を埋めてください
option_one = get_expected_cost(2, 3)
option_two = get_expected_cost(3, 2)
option_three = get_expected_cost(3, 3)
option_four = get_expected_cost(3, 4)
""")
    
class GetCostPaint(FunctionProblem):
    _var = 'get_cost'
    _test_cases = [
        ((432, 144, 400, 15), 21.599999999999998),
        ((400, 400, 400, 10), 20.0),
        ((400, 500, 300, 16), 48.0),
    ]
    _hint = ("まず、塗装が必要な壁と天井の合計面積（平方フィート）を計算します。"
    "次に、それに基づいて必要なペンキのガロン数を導き出します。"
    "必要なガロン数がわかれば、プロジェクトの総コストを計算できます。")
    _solution = CS(
"""
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost
""") 

class GetCostPaintExample(EqualityCheckProblem):
    _var = 'project_cost'
    _expected = get_cost(432, 144, 400, 15)
    _hint = ("もし代わりに、800平方フィートの壁と160平方フィートの天井を持つ部屋に"
             "ペンキを1度塗りするコストを計算する必要があり、1ガロンのペンキが300平方フィートをカバーし"
             "10ドルかかる場合、`project_cost = get_cost(800, 160, 300, 10)` と設定します。")
    _solution = CS(
"""# project_cost 変数にプロジェクトのコストを設定してください
project_cost = get_cost(432, 144, 400, 15) 
""")
    
class NoMoreFractions(FunctionProblem):
    _var = 'get_actual_cost'
    _test_cases = [
        ((432, 144, 400, 15), 30),
        ((400, 500, 400, 10), 30),
        ((400, 900, 300, 16), 80),
    ]
    _hint = ("まずは `get_cost()` 関数を出発点として使用します。唯一変更する必要があるのは、"
             "購入すべきガロン数を切り上げるための `math.ceil()` を追加することです。"
             "関数のどこに追加すればよいかわかりますか？")
    _solution = CS(
"""def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    gallons_to_buy = math.ceil(gallons_needed)
    cost = cost_per_gallon * gallons_to_buy
    return cost
""")


qvars = bind_exercises(globals(), [
    GetExpectedCost,
    RunGetExpectedCost,
    GetCostPaint,
    GetCostPaintExample,
    NoMoreFractions
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)
