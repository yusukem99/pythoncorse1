from learntools.core import *

# problem 1
correct_menu = ['stewed meat with onions', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro', 'roasted beet salad']

# problem 2
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# problem 3
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# problem 4
def percentage_liked_solution(ratings):
    list_liked = [i >= 4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

# problem 5
def percentage_growth_solution(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
num_users_test2 = [920224, 1009553, 1219334, 1478996, 1503423, 1593862, 1620963, 1841064, 1930952, 2001232]


class FoodMenu(CodingProblem):
    _var = 'menu'
    _hint = ("メニューを作成した元のコードはこちらです: "
             "`menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp', "
             "'fish soup with cream and onion', 'gyro']`。`.append()` でアイテムを追加し、"
             "`.remove()` でアイテムを削除してください。")
    _solution = CS(
"""# 変更しないでください: レストランの初期メニュー
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

# 'bean soup' を削除し、'roasted beet salad' をメニューの末尾に追加する
menu.remove('bean soup')
menu.append('roasted beet salad')
""")
    def check(self, menu):
        
        # is python list
        assert isinstance(menu, list), \
            '`menu` needs to be a Python list.'
        
        # extra items need to be removed
        assert set(menu) - set(correct_menu) == set(), \
            'These item(s) should be removed from `menu`: {}'.format(list(set(menu) - set(correct_menu)))
        
        for item in correct_menu:
            # contains all needed items
            assert item in menu, '`menu` needs to have this item, but it is missing: `{}`'.format(item)
            # no items duplicated
            assert menu.count(item) == 1, 'Each item should appear in `menu` once, but `{}` appears {} times.'.format(item, menu.count(item))
        

class NumCustomers(EqualityCheckProblem):
    _vars = ['avg_first_seven', 'avg_last_seven', 'max_month', 'min_month']
    _expected = [sum(num_customers[:7])/7, sum(num_customers[-7:])/7, max(num_customers), min(num_customers)]
    _hint = ("リストの平均を求めるには、合計を計算してから要素数で割ります。"
             "リスト `my_list` の最後の `y` 個の要素を取得するには、`my_list[-y:]` を使います。")
    _solution = CS(
"""# 以下の変数に値を設定してください
avg_first_seven = sum(num_customers[:7])/7
avg_last_seven = sum(num_customers[-7:])/7
max_month = max(num_customers)
min_month = min(num_customers)
""")

class SplitString(EqualityCheckProblem):
    _vars = ['letters', 'formatted_address']
    _expected = [alphabet.split("."), address.split(",")]
    _hint = ("どちらの場合も `.split()` を使う必要があります。")
    _solution = CS(
"""letters = alphabet.split(".")
formatted_address = address.split(",")
""")
    
class PercentageLiked(FunctionProblem):
    _var = 'percentage_liked'
    _test_cases = [
        ([1, 2, 3, 4, 5, 4, 5, 1], percentage_liked_solution([1, 2, 3, 4, 5, 4, 5, 1])),
        ([1, 2, 3, 4], percentage_liked_solution([1, 2, 3, 4])),
        ([1, 2, 3, 4, 5, 4, 5, 1, 2, 2, 2], percentage_liked_solution([1, 2, 3, 4, 5, 4, 5, 1, 2, 2, 2])),
        ([1, 4, 4, 4, 5, 4, 5, 1], percentage_liked_solution([1, 4, 4, 4, 5, 4, 5, 1])),
    ]
    _hint = ('ブール値を足し算すると、`True` の要素の合計数が返されることを思い出してください。')
    _solution = CS(
"""
# 関数を完成させてください
def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked
""")
    
class WebsiteAnalytics(FunctionProblem):
    _var = 'percentage_growth'
    _test_cases = [
        ((num_users_test, 1), percentage_growth_solution(num_users_test, 1)),
        ((num_users_test2, 2), percentage_growth_solution(num_users_test2, 2)),
        ((num_users_test, 3), percentage_growth_solution(num_users_test, 3)),
        ((num_users_test2, 4), percentage_growth_solution(num_users_test2, 4)),
        ((num_users_test, 5), percentage_growth_solution(num_users_test, 5)),
        ((num_users_test2, 6), percentage_growth_solution(num_users_test2, 6)),
        ((num_users_test, 7), percentage_growth_solution(num_users_test, 7)),
        ((num_users_test2, 8), percentage_growth_solution(num_users_test2, 8)),
        ((num_users_test, 9), percentage_growth_solution(num_users_test, 9)),
    ]
    _hint = ("リストから2つの数値を引き算してからリストの要素で割るという考え方は合っています。"
             "変更が必要なのは、リストから取り出す要素の位置だけです。\n\n"
             "`num_users` リストの最後の要素を取得するには `num_users[len(num_users)-1]` を使います。"
             "これは直近の年のユーザー数に対応します。\n\n"
             "1年前のユーザー数を取得するには `num_users[len(num_users)-2]` を使います。\n\n"
             "`yrs_ago` 年前のユーザー数を取得するには `num_users[len(num_users)-yrs_ago-1]` を使います。")
    _solution = CS(
"""def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth
""")

qvars = bind_exercises(globals(), [
    FoodMenu, 
    NumCustomers, 
    SplitString, 
    PercentageLiked,
    WebsiteAnalytics, 
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)
