# Syntax, Variables, and Numbers - 文法、変数、数値

## 問０

これはちょっとおかしな設問なのですが、これからの演習問題を解くための準備です。

次の質問に答えてください。

*what is your favorite color?*

`color`に適切な値を代入して、`q0.check()`を実行してください。

正解が分からないときは、下のコードセルの`q0.hint()`関数を使うことができます。

## 問１

円周率`pi`と円の直径`diameter`を表す変数が宣言されています。

円の半径`radius`と円の面積`area`を表す変数を宣言してください。

下の表を参考にしてください。

| Operator     | Name           | Description                                            |
|--------------|----------------|--------------------------------------------------------|
| ``a + b``    | Addition       | Sum of ``a`` and ``b``                                 |
| ``a - b``    | Subtraction    | Difference of ``a`` and ``b``                          |
| ``a * b``    | Multiplication | Product of ``a`` and ``b``                             |
| ``a / b``    | True division  | Quotient of ``a`` and ``b``                            |
| ``a // b``   | Floor division | Quotient of ``a`` and ``b``, removing fractional parts |
| ``a % b``    | Modulus        | Integer remainder after division of ``a`` by ``b``     |
| ``a ** b``   | Exponentiation | ``a`` raised to the power of ``b``                     |
| ``-a``       | Negation       | The negative of ``a``                                  |


## 問２

`a`と`b`の値を入れ替えてください。

つまり、`a`は`b`が参照していたオブジェクトを参照し、`b`は`a`が参照していたオブジェクトを参照するようにしてください。

下のコードセルの`# Your code goes here. ...`の部分を書き換えてください。

`Setup code - don't touch this part`と書かれている部分を変更してはいけません。

## 問３a
1になるように以下の式に括弧を付け加えてください。

## 問３b

0になるように以下の式に括弧を付け加えてください。

## 問４

ハロウィンの日、アリスとボブとキャロルでアメを持ち寄って均等に分けあうことにしました。

3人の友情のために、余ったアメは砕いてしまうことにします。

以下の変数に持ち寄ったアメの数が入っています。

```
alice_candies = 121
bob_candies = 77
carol_candies = 109
```

`to_smash = -1`の右辺を書き換えて、砕くアメの数を`to_smash`に代入してください。


# Functions and Getting Help - 関数とヘルプ

## 問１

docsringを参考に、以下の関数を完成させてください。 

```
Return the given number rounded to two decimal places. 
（与えられた数を小数点以下2桁で四捨五入して返す。）
```

`round`関数を使うことができます。

## 問２
help関数によると、`round`関数は第二引数に負の値を受けることができます。

以下のコードセルでどうなるか試してください。またその処理内容について説明してください。

どのような処理か説明できるようになったら、`q2.solution()`を実行してください。

## 問３

前回のコースで、ボブとキャロルがアメを分け合うときに、余ったアメを砕く数を計算する関数を作成しました。

たとえば、3人で91個のアメを持ち寄った場合、3人とも30個ずつ持って帰り、余った1個を砕くことになります。

今回は任意の人数で分け合うことができるように、以下の関数に**分け合う人数を**表す第二引数を追加してください。

ただし、第二引数が設定されなかった場合のデフォルト値は3人としてください。

また、docstringも修正してください。

## 問４

エラーが出たときに、どのようなエラーが出たのか確認することはとても重要です。

以下のコードには何らかのバグを抱えています。それぞれで以下の手順を実行してください。

1. コードを読んで、何が起こるか予想する。
2. コメントアウトして実行結果を確認する。
3. コードを修正してエラーが出ないようにする。

ctrl+/を使うと、指定した行をコメントアウトすることができます。

# Booleans and Conditionals

## 問１

多くのプログラミング言語では、[`sign`](https://en.wikipedia.org/wiki/Sign_function)という組み込み関数が用意されています。Pythonにはありませんが、独自に定義することができます。

下のセルに、数値を引数にとり、負の場合は-1、正の場合は1、0の場合は0を返す`sign`という関数を定義してください。

## 問２

前回の練習で作った `to_smash` 関数に ログを追加してみることにしました。
```
print("Splitting", total_candies, "candies")
```
このように関数の途中に出力することで、その途中経過を確かめることができます。

`total_candies = 1`となるように実行するとどうでしょうか？

```
to_smash(1)
```

これは文法としてよくありません。アメの数が一つなら複数形の「candies」ではなく単数形の「candy」となるべきです。コードを修正してください。

## 問３

雨に備えて、出かける準備ができているか判定する関数`prepared_for_weather`を作成しました。

以下の条件を満たしていれば準備ができているものとします。

- 傘を持っている(`have_umbrella==True`)
- 雨がそれほどひどくなくて(`rain_level<5`)、フードがある(`have_hood==True`)
- 雨が降っていない、または休日(`is_workday==False`)。言い換えると、雨が降ってかつ稼働日である以外のとき。

しかし、以下のコードはバグを抱えています。どのような引数を与えたときに問題が起こるでしょうか？

以下の引数の値を変更して、バグを起こす値を見つけてください。

```
have_umbrella = True
rain_level = 0.0
have_hood = True
is_workday = True
```

たとえば
```
have_umbrella=True
rain_level=0.0
have_hood=True
is_workday=True
```

のとき`prepared_for_weather`関数は`True`を返します。これは期待したとおりの値です。

この問題では期待していない値を返す引数の値を見つけてください。

## 問４

以下の`is_negative`関数は与えられた数が負であれば`True`を、それ以外であれば`False`を返します。

しかしながら、処理内容がシンプルのわりに、コードが複数行にわたり冗長です。

`is_negative`関数と同等の処理を一行で実現する`concise_is_negative`関数を作成してください。

**concise** 一致する,等しいという意味

## 問５

`ketchup`/`mustard`/`onion` はそれぞれ顧客が注文したホットドッグのトッピングを有無を`True`または`False`で表しています。

顧客のオーダーに応じた値を返す関数を完成させてください。例えば`onionless`関数は以下のようになります。

## 問５a

顧客がすべてのトッピングを希望している場合に`True`を返すように、`wants_all_toppings`関数を完成させてください。

## 問５b

顧客がトッピングを一つも希望していない場合に`True`を返すように、`wants_plain_hotdog`関数を完成させてください。


## 問５c

顧客が`ketchup`又は`mustard`のどちらか一つだけを希望している場合に`True`を返すように、`exactly_one_sauce`関数を完成させてください。両方を希望している場合は`False`になります。

## 問６

bool関数に整数型の値を渡すと、その値が0なら`False`、それ以外なら`True`を返します。

`int`関数に`bool`型の値を渡すとどうなるでしょうか？この`int`関数の特性を利用して`exactly_one_topping`関数を実装してください。

この関数はいずれか一つのトッピングだけを使う場合に`True`を返します。

## 問７

プレイヤー(あなた)は2枚のカードを表向きに、ディーラーは2枚のカードのうち1枚を裏向きにして配られます。

この状態でプレイヤーはもう一枚カードをひく（ヒット）か選べます。ただしカードの合計が21を超えるとその時点で負けになります。

同様にディーラーは17以上になるまでカードを引きます。最終的にプレイヤーとディーラーでカードの合計が大きい方が勝ちです。

絵札は10、エースは1または11いずれかの値をとることができます。

与えられた状況で**ヒット**するべきか判定する関数`should_hit`関数を完成させてください。引数は以下のようになります。

- dealer_total：ディーラーの合計
- player_total：プレイヤーの合計
- player_low_aces：プレイヤーの1としてカウントするエースの数
- player_high_aces：プレイヤーの11としてカウントするエースの数

たとえば、手持ちが{A, A, A, 7}なら、11 + 1 + 1 + 7になり、player_total=20 player_low_aces=2 player_high_aces=1

# Lists

## 問１

`docstring`にしたがって、以下の関数を完成させてください。

`docstring`和訳：与えられたリスト内の2番めの要素を返す。二番目の要素が存在しない場合は`None`を返してください。

## 問２

スポーツチームのデータを分析しています。

チームのメンバーの名前が格納されたリストがあります。リストの先頭がコーチで、次にキャプテン、そのあとに他の選手が続いています。

さらに、上記のようなチームリストが成績上位順にそれぞれ親のリストに格納されています。

例

```
[
    ['Paul', 'John', 'Ringo', 'George'], 
    ['Jen', 'Jamie']
]
```

もっとも成績が悪かったチームのキャプテンの名前を返す関数`losing_team_captain`を作成してください。

## 問３

マリオカートの次回作では、新しいアイテム**紫甲羅**が登場します。

このアイテムはなんと最初と最後の走者を入れ替えてしまいます。

以下の関数`purple_shell`を完成させてください。

例.
```
r = ["Mario", "Bowser", "Luigi"]
purple_shell(r)
print(r)
# ["Luigi", "Bowser", "Mario"]
```

## 問４

以下のリストの長さはそれぞれいくつになるでしょうか？`length`にそれぞれの要素数を代入してください。

ここでは関数`len()`を使わずに、自分で予想してください。

## 問５

次のリストはパーティに出席した人が、到着した順に並べられています。

```
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
```

`Adela`さんは一番初めに、`Ford`さんは一番最後に到着しました。

海外ではパーティーなどのカジュアルな場に呼ばれたときには、ちょっと遅れるくらいがかっこいいという感覚があります。（ただし、一番最後はNGです。）

このことを**fashionably late**といい、あえて約束の時間に遅れてくることを表します。

全体の半分より後に到着した人を`fashionably late`だと定義します。

`arrivals`に到着した名前が順に格納されています。`name`で指定された参加者が`fashionably late`かどうかを`True`または`False`で判定する関数を完成させてください。

# Loops and List Comprehensions

## 問１

`has_lucky_number`関数は、引数`nums`で与えられたリストの中に一つでも7で割り切れる数があれば`True`を返します。

しかしこの関数はバグを抱えています。下のコードセル（２つめ）を編集して`has_lucky_number`関数を完成させてください。

## 問２

下のコードセルはどのような結果を返すでしょうか？結果を予想したらコメントアウトして実行してください。

```
[1, 2, 3, 4] > 2
```

`numpy`や`pandas`では上のような演算子が有効で、それぞれの要素を比較し`[False, False, True, True]`を返してくれます。

`L`で与えられたリストのそれぞれの要素に対し、`thresh`より大きい値であれば`True`、小さければ`False`に変換する関数`elementwise_greater_than`を完成させてください。

例
```
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
```

threshold：しきい値

## 問３

引数`meals`にある期間に提供される料理のリストが渡されます。

同じメニューが２日続いた場合に`True`をそうでなければ`False`を返すように、`menu_is_boring`関数を完成させてください。

## 問４

前回のブラックジャックに続いて、今度はスロットマシーンをつくりました。`play_slot_machine()`を実行してみてください。出力された額のお金（ドル）がもらえます。

```
play_slot_machine()
```

大抵の場合は0$しかでませんが、運が良ければたくさんお金がでてきます。

平均してこのスロットマシーンは一回あたり何ドル利益が出るのでしょうか？このカジノでは期待値を公開していませんが、統計的な手法を用いて推定することができます。[モンテカルロ法](https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%B3%E3%83%86%E3%82%AB%E3%83%AB%E3%83%AD%E6%B3%95)を用いて計算してみましょう。

[モンテカルロ法で円周率を求める](https://manabitimes.jp/math/1182)

# Strings and Dictionaries

## 問0a-0e

まずはウォーミングアップとして文字列の長さを予想してみましょう。

`a`～`e`で宣言された文字列の長さを、`length`に代入してください。

ここで`len()`関数を使用しないこと。

## 問１

個人や企業が蓄積して扱えるデータを活用し、新しい価値を提案する仕事を「データサイエンティスト」といいます。

データサイエンティスト仕事のうち8割はデータクレンジングに、残りの2割はその作業に不満をいうことだと言われています。

ここではZIPコードのデータクレンジングに関する関数を作ってみます。

ZIPコードとはアメリカ合衆国の郵便番号で、ちょうど５桁の数字で構成されています。

与えられた`zip_code`が正しいフォーマットか判定し`True`または`False`で返す関数`is_valid_zip`を完成させてください。

ヒント：`str`型は便利なメソッドを備えています。`help(str)`を使ってみてください。

*データクレンジングとは*

破損したデータ、不正確なデータ、無関係なデータを検出し、データベースに格納する前に修正または削除することです。

## 問２

ある研究者が論文を集めています。

研究者は集めた何千もの論文の中から、特定の単語を含むものだけを抽出したいと思いました。

 `word_search`関数では`doc_list`に論文の内容のリスト、`keyword`に検索する単語が渡されます。

検索する単語`keyword`が含まれる論文のインデックスを含むリストを返すように、`word_search`関数を完成させてください。

ここで、論文の抽出条件は以下のルールに従うものとします。

- キーワードの一部のみが一致するものは、不一致とする。例えばkeyword="closed"のとき、"enclosed."は不一致とする。
- 大文字と小文字を区別しない。例えば、"keyword=closed"のとき"Closed the case."は一致とする。
- ピリオドとカンマは検索条件に影響しない。例えば、keyword="closed"のとき、"It is closed."は一致とする。

例:
```
>>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
>>> word_search(doc_list, 'casino')
[0]
```

## 問３

研究者は先に作った関数`word_search`を複数の単語で検索できるようにしたいと思いました。

`multi_word_search()`関数は、引数`keywords`で検索する複数の単語がリストで渡されます。

それぞれの単語を**キー**、論文のインデックスを含むリストをバリューとしたペアの辞書を返すように関数を完成させてください。

ここでは問２で作成した`word_search`を活用してください。

例:
```
def multi_word_search(doc_list, keywords):
    # 関数内でword_search関数を呼び出す
    hit_list = word_search(doc_list, 'casino')
```

```
    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
```    

# Working with External Libraries

## 問１

レッスン4の`List`では`estimate_average_slot_payout`関数を作成し、スロットマシーンをモンテカルロ法を用いて分析してみました。

スロットマシーンは長期的に見ると利益がでることが分かったので、`matplotlib`を使ってグラフを作成してみます。

Jimmyさんは$200から始めて500回スロットを回した時の手持ち金の推移をグラフにしました。

```
# Import the jimmy_slots submodule
from learntools.python import jimmy_slots
# Call the get_graph() function to get Jimmy's graph
graph = jimmy_slots.get_graph()
graph
```

グラフを見るとわかるように、Jimmyさんは最後の方で運が悪く手持ち金が減っています。

Jimmyさんはこのグラフをツイートしようと思いました。しかしこのグラフのままでは見た人の誤解を招きそうです。

引数`graph`で与えられたグラフに、以下の変更を加える`prettify_graph()`関数を完成させてよりよい図にしてください。

- タイトルを"Results of 500 slot machine pulls"にする
- y軸のスタートを0にする
- y軸のラベルを"Balance"にする
- y軸の刻みに$150のように単位を加える

まずは` type(graph) `を実行して`graph`の型を調べてみましょう。
さらに`dir(graph)`を使用してみると`.set_title()`, `.set_ylim()`, `.set_ylabel()`のようなメソッドがあることがわかります。
これらのメソッドの使い方が分からなければ`help()`関数を使いましょう。

## 問２

マリオカートで優勝するために、最も有効なアイテムは何でしょうか。

過去のレースのデータセットを分析してみましょう。

データセットは以下のように、リストの中に複数の辞書型の要素が含まれています。

```
[
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    # 走者の名前が入っていない(None)のときがあります。
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
```

リスト内の要素がそれぞれ一人の走者を表し、`items`はその走者が獲得したアイテムのリスト、`finish`がその走者の順位です。

例えば、上のデータセットの一つ目の要素はPeachのデータで、Peachは3位で、獲得したアイテムは`green shell`, `banana`, `green shell`の3つです。

best_items()`関数は引数に上記のようなリストを受け、一位の走者が獲得したアイテムをカウントして辞書型で返します

```
def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts
```

`best_items()`関数を実行してみると正しい結果が得られます。次のコードセルを実行してみてください。

```
sample = [
    {'name': 'Peach', 'items': ['green shell', 'banana', 'green shell',], 'finish': 3},
    {'name': 'Bowser', 'items': ['green shell',], 'finish': 1},
    {'name': None, 'items': ['mushroom',], 'finish': 2},
    {'name': 'Toad', 'items': ['green shell', 'mushroom'], 'finish': 1},
]
best_items(sample)
```

しかし、全データを用いて実行してみると`TypeError`の例外を出力してしまいました。

この原因を調査して、下のコードが正常に動作するように修正してください。

## 問３

前回のレッスンでトランプのブラックジャックで勝つための戦略を考えました。

ブラックジャックの手札を表す型(`BlackjackHand`)を作成したいとします。

この型では、`>`や`<=`のような比較演算子をオーバーロードして、二つの手札の大小を比較できるようにしたいとします。

もし下の例のように、手札の合計を比較演算子を使ってその大小を比較出来たら便利ですね。

```
>>> hand1 = BlackjackHand(['K', 'A'])
>>> hand2 = BlackjackHand(['7', '10', 'A'])
>>> hand1 > hand2
True
```

この授業では独自のクラス作成については扱いませんが、`__gt__`メソッドをオーバーロードすることでその機能が実現できます。

ここではその機能を関数`blackjack_hand_greater_than()`で実装してみましょう。

二つの手札がそれぞれ引数`hand_1`,`hand_2`で渡されます。

`hand_1`が`hand_2`に勝つ場合`True`を、そうでなければ`False`を返します。

以下の条件のとき`hand_1`の勝ちとします
- `hand_1`が21以下
- `hand_1`が`hand_2`より大きい。または`hand_2`が21を超えている

'J'、'Q'、'K' は10、'A'は1または11の有利なほうの値をとることができます。

例
```
>>> blackjack_hand_greater_than(['K'], ['3', '4'])
True
>>> blackjack_hand_greater_than(['K'], ['10'])
False
>>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
False
```