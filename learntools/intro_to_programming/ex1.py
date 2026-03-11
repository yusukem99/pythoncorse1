from learntools.core import *

num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
births_per_min = 250

survived = 342
minors = 113
total = 891

class RunHelloWorld(CodingProblem):
    _congrats = ("上に 'Hello, world!' と表示されていれば成功です。これでメッセージの表示方法を学びました。"
                 "次の問題に進む準備は完了です。")
    _correct_message = ""
    def check(self):
        pass 
    
class PrintAnotherMsg(CodingProblem):
    _congrats = "あなた独自のメッセージを表示できたら、次の問題に進む準備は完了です。"
    _correct_message = ""
    def check(self):
        pass 
    
class LearnCheckingCode(CodingProblem):
    _hint = "問題に行き詰まったら、とりあえず解答を見る前にヒント (`hint()`) を確認する習慣をつけましょう。"
    _solution = ("ヒントを見たりチュートリアルを読み返したりしても分からない場合は、"
                 "解答 (`solution()`) を見ることができます。また、自力で正解した後に"
                 "公式の解答が自分の書いたコードと違うかどうかを確認するためにも使えます"
                 "（プログラミングには複数の正解があることがよくあります！）。")
    _congrats = "ヒントと解答の両方を表示できたら、次の問題に進む準備は完了です。"
    _correct_message = ""
    def check(self):
        pass 

class BirthsPerYear(EqualityCheckProblem):
    _vars = ['births_per_min', 'births_per_day']
    _expected = [250, births_per_min * mins_per_hour * hours_per_day]
    _hint = ("1日の分数を計算するには、どの変数を使えばいいでしょうか？ "
             "それが分かれば、あとは1分あたりの出生数(`births_per_min`)を掛けるだけです。")
    _solution = CS(
"""# births_per_min 変数に値をセットする
births_per_min = 250

# births_per_day 変数の値を計算してセットする
births_per_day = births_per_min * mins_per_hour * hours_per_day
""")
    
class BonusTitanic(EqualityCheckProblem):
    _vars = ['survived_fraction', 'minors_fraction']
    _expected = [survived/total, minors/total]
    _hint = ("タイタニック号の生存者の割合を求めるには、生存者の数を総人数で割る必要があります。"
             "この問題で使える変数を確認しましょう: `survived`（生存者数）、`total`（総人数）、"
             "そして `minors`（未成年者数）です。")
    _solution = CS(
"""# survived_fraction 変数に計算した代入する
survived_fraction = survived / total

# survived_fraction の値を画面に表示（プリント）する
print(survived_fraction)

# minors_fraction 変数に計算して代入する
minors_fraction = minors / total

# minors_fraction の値を画面に表示（プリント）する
print(minors_fraction)
""")


qvars = bind_exercises(globals(), [
    RunHelloWorld,
    PrintAnotherMsg,
    LearnCheckingCode,
    BirthsPerYear,
    BonusTitanic
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)
