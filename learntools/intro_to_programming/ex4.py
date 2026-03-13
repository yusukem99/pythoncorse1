from learntools.core import *

def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        bill = 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        bill = 7 * num_gallons / 1000
    else:
        bill = 10 * num_gallons / 1000
    return bill

def get_phone_bill(gb):
    # everyone pays $100/month
    bill = 100
    # number of GB over the 15GB plan (negative if under)
    gb_over = gb - 15
    # if gb_over is positive, there is an additional fee
    if gb_over > 0:
        # calculate cost of additional GB
        overage_fee = 100 * gb_over
        # add additional cost to bill
        bill = bill + overage_fee
    return bill

class GetGrade(FunctionProblem):
    _var = 'get_grade'
    _test_cases = [(i, get_grade(i)) for i in range(0,101)]
    _hint = ('`"A"` は `score >= 90` の場合のみ返すべきです。それ以外は、スコアが 80〜89（含む）、'
             '70〜79（含む）、60〜69（含む）、または 60 未満の場合にそれぞれ異なる成績を返します。'
             '関数が必ず `"A"`, `"B"`, `"C"`, `"D"`, `"F"` のいずれかを返すようにしてください。')
    _solution = CS(
"""def get_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
""")

class CostProjectPartDeux(FunctionProblem):
    _var = 'cost_of_project'
    _test_cases = [
        (("Charlie+Denver", True), 240),
        (("08/10/2000", False), 120),
        (("Adrian", True), 160),
        (("Ana", False), 71),
    ]
    _hint = ("`solid_gold = True` の場合、指輪のコストは \\$100（基本料金）に、"
             "刻印の長さ × \\$10 を加えたものです。刻印の長さは `len(engraving)` で取得できます。"
             "`solid_gold = False` の場合は、\\$50（基本料金）に、刻印の長さ × \\$7 を加えたものです。")
    _solution = CS(
"""# option 1
def cost_of_project(engraving, solid_gold):
    num_units = len(engraving)
    if solid_gold == True:
        cost = 100 + 10 * num_units
    else:
        cost = 50 + 7 * num_units
    return cost
    
# option 2 
def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = 100 + 10 * len(engraving)
    else:
        cost = 50 + 7 * len(engraving)
    return cost
""")
    
class GetWaterBill(FunctionProblem):
    _var = 'get_water_bill'
    _test_cases = [(1000*i, get_water_bill(1000*i)) for i in range (0, 41)]
    _hint = """
解答は次のような形になります:
```python
def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = ____
    elif num_gallons <= 22000:
        bill = ____
    elif num_gallons <= 30000:
        bill = ____
    else:
        bill = ____
    return bill
```
"""
    _solution = CS(
"""def get_water_bill(num_gallons):
    if num_gallons <= 8000:
        bill = 5 * num_gallons / 1000
    elif num_gallons <= 22000:
        bill = 6 * num_gallons / 1000
    elif num_gallons <= 30000:
        bill = 7 * num_gallons / 1000
    else:
        bill = 10 * num_gallons / 1000
    return bill
""")
    
class GetPhoneBill(FunctionProblem):
    _var = 'get_phone_bill'
    _test_cases = [(5 + .5*i, get_phone_bill(5 + .5*i)) for i in range (0, 35)]
    _hint = """
解答は次のような形になります:
```python
def get_phone_bill(gb):
    if gb <= 15:
        bill = ____
    else:
        bill = 100 + ____
    return bill
```
"""
    _solution = CS(
"""def get_phone_bill(gb):
    if gb <= 15:
        bill = 100
    else:
        bill = 100 + (gb - 15) * 100
    return bill
""")

class GetLabels(CodingProblem):
    _congrats = "すべての食品のラベルを決定できたら、次のレッスンに進む準備は完了です！"
    _correct_message = ""
    def check(self):
        pass

qvars = bind_exercises(globals(), [
    GetGrade, 
    CostProjectPartDeux, 
    GetWaterBill, 
    GetPhoneBill, 
    GetLabels
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)
