from learntools.core import *

# Complete fn that takes a list and returns the second element

class SelectSecondItem(FunctionProblem):
    #TODO: Wrap index errors
    _var = 'select_second'

    _test_cases = [
            ([1, 2, 3], 2),
            ([[1], [2], [4]], [2]),
            (list(range(10)), 1),
            ([1], None),
            ([], None),
    ]

    _hint = "Pythonでは0から数え始めます。つまり、2番目の要素のインデックスは2ではありません。"

    _solution = CS(
"""def select_second(L):
    if len(L) < 2:
        return None
    return L[1]""")

class LosingTeamCaptain(FunctionProblem):
    _var = 'losing_team_captain'

    _test_cases = [
            ([["Paul", "John", "Ringo", "George"]], "John"),
            ([["Paul", "John", "Ringo", "George"], ["Jen", "Jamie"]], "Jamie"),
            ([["Who", "What", "I don't Know", "I'll tell you later"], ["Al", "Bonnie", "Clyde"]], "Bonnie"),
    ]

    _hint = ("リスト `L` の最後の要素は `L[-1]` で取得できます。"
             "最初のサブリストの最初の要素は `L[0][0]` で取得できます。"
             )

    _solution = CS(
"""def losing_team_captain(teams):
    return teams[-1][1]""")

class PurpleShell(FunctionProblem):

    _var = 'purple_shell'


    _hint = ("関数は受け取ったリストを変更するだけで、何も返さないようにしてください。\n\n"
            "リストの要素を入れ替えるには、最初の演習で2つの変数を入れ替えたときのコードを"
            "思い出してみましょう。"
             )

    def check(self, fn):
        lists = (["M","L"],
                 ["M","L","J"],
                 [1,2,3,4,5]
                )
        def sol_fn(x): x[0], x[-1] = x[-1], x[0]
        for l in lists:
            copy_for_soln_fn = l.copy()
            copy_for_user_fn = l.copy()
            sol_fn(copy_for_soln_fn) # create desired output for comparison
            user_output = fn(copy_for_user_fn) # also applies swap in this line
            assert(type(user_output) == type(None)), ("関数は何も返さないようにしてください。"
                                                      "リストを返すのではなく、リスト自体を変更してください。")
            assert copy_for_user_fn == copy_for_soln_fn, (
                    "リスト {} に関数を実行した後、新しい値は {} になるはずですが、"
                    "実際には {} でした。").format(repr(l), repr(copy_for_soln_fn), repr(copy_for_user_fn))



    _solution = CS(
"""def purple_shell(racers):
    # スマートな入れ替え方法: x[0], x[-1] = x[-1], x[0]
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp""")

class UnderstandLen(EqualityCheckProblem):
    _var = 'lengths'
    _expected = [3, 2, 0, 2]
    _default_values = [ [] ]

    _hint = "`len` を使ってリストの長さを確認しましょう。解説は `solution()` で確認できます。"

    _solution = (
            """
- a: このリストには3つの要素があります。ここまでは簡単ですね。
- b: リスト `[2, 3]` は1つの要素として数えられます。その前に1つの要素があるので、合計2つの要素があります。
- c: 空のリストの要素数は0です。
- d: この式はリスト `[2, 3]` と同じで、長さは2です。""")

class FashionablyLate(FunctionProblem):
    _var = 'fashionably_late'



    _test_cases = [
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Adela"), False),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Fleda"), False),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Owen"), False),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "May"), False),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Mona"), True),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Gilbert"), True),
            ((['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford'], "Ford"), False),
            ((["Paul", "John", "Ringo", "George"], "John"), False),
            ((["Paul", "John", "Ringo", "George"], "Ringo"), True),
            ((["Lebron", "Kevin"], "Lebron"), False),
            ((["Lebron", "Kevin"], "Kevin"), False),
    ]

    _hint = ("`index` メソッドを使って、その人がいつ到着したかを調べましょう。"
            "リストの長さ (`len`) を使って、それが「おしゃれに遅刻」した位置かどうかを確認しましょう。"
            "0始まりのインデックスに注意してください。"
             )

    _solution = CS(
"""def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1""")

class CountNegativesRiddle(FunctionProblem):
    _bonus = True
    _var = 'count_negatives'

    _test_cases = [
            ([], 0),
            ([0, -1, -1], 2),
            ([3, -3, 2, -1, 4, -4, 5, 5], 3),
            ([1, 2, 3, 4, 5, 0], 0),
    ]

    _hint = ('入力リストがソート済みで、かつ必ず0を含んでいると仮定した場合、'
            'この問題をどう解けるか考えてみましょう。')

    _solution = """
チュートリアルで紹介したツールだけを使った、少し意外な解法を紹介します:
```python
def count_negatives(nums):
    nums.append(0)
    # list.sort() メソッドを使うこともできます。これはリストを昇順に並び替えます。
    nums = sorted(nums)
    return nums.index(0)
```

この実装は、`list.index` が値の*最初の*出現位置のインデックスを返すことを利用しています（`help(list.index)` で確認できます）。つまり、リストを昇順にソートした後、0がインデックス0にあれば負の数は0個です。0がインデックス2（つまり3番目の要素）にあれば、0より小さい要素が2つあるということです。

*注意*: 関数に渡されたリストを、ドキュメントなどで事前に知らせずに変更するのは一般的に「行儀が悪い」とされています。丁寧に書くなら、まず `list.copy()` メソッドを使ってコピーを作り（例: `our_nums = nums.copy()`）、元のリストではなくコピーに対して操作するとよいでしょう。

Lispが好きな方なら、こんな技術的に正しい解法を書いたかもしれません（再帰についてはまだ扱っていませんが、まだ見ていない構文や関数は使っていないはずです）:

```python
def count_negatives(nums):
    # "if len(nums) == 0" と同等です。空のリストはFalseyです。
    if not nums:
        return 0
    else:
        # ブール値を暗黙的にintに変換しています！
        # ブール値と条件分岐の演習の問題6を参照してください。
        return (nums[0] < 0) + count_negatives(nums[1:])
```"""


qvars = bind_exercises(globals(), [
    SelectSecondItem,
    LosingTeamCaptain,
    PurpleShell,
    UnderstandLen,
    FashionablyLate,
    CountNegativesRiddle,
    ],
)
__all__ = list(qvars)
