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