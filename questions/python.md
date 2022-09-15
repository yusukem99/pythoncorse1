# Syntax, Variables, and Numbers

## 問０

`color`に好きな色を入れてください。

## 問１

円の半径と円の面積を表す変数`radius`と`area`を宣言してください。

## 問２

`a`と`b`の値を入れ替えてください

## 問３a
1になるように以下の式に括弧を付け加えてください。

## 問３b

0になるように以下の式に括弧を付け加えてください。

## 問４

ハロウィンの日、アリスとボブとキャロルでアメを持ち寄って均等に分けあうことにしました。

3人の友情のために、余ったアメは砕いてしまうことにします。

以下の変数に持ち寄ったアメの数が入っています。

砕くアメの数を`to_smash`に代入してください。


# Functions and Getting Help

## 問１

docsringを参考に、以下の関数を完成させてください。 two decimal places: 小数点第二位

## 問２
help関数によると、`round`関数は第二引数に負の値を受けることができます。

以下のコードセルでどうなるか試してください。またその処理内容について説明してください。

## 問３

前回のコースでアメを均等に分け合うために、砕くアメの数を計算する関数を作りました。

今回は任意の人数で分け合うことができるように、以下の関数に第二引数を追加してください。

## 問４

以下のコードには何らかのバグを抱えています。それぞれで以下の手順を実行してください。

1. コードを読んで、何が起こるか予想する。
2. コメントアウトして実行結果を確認する。
3. コードを修正してエラーが出ないようにする。

# Booleans and Conditionals

## 問１

多くのプログラミング言語では`sign`関数があります。残念ながらpythonにはありません。

与えられた引数が負なら-1を、正なら0を返す`sign`関数を定義してください。

## 問２

これまで何度か作成してきた`to_smash`関数にログを加えました。`total_candies = 1`で実行するとどうでしょうか？

これは文法としてよくありません。アメの数が一つならcandiesではなくcandyとなるべきです。コードを修正してください。

## 問３

雨に備えて、出かける準備ができているか判定する関数`prepared_for_weather`を作成しました。

以下の条件を満たしていれば準備ができているものとします。

- 傘を持っている
- 雨がそれほどひどくなくて、かっぱを持っている
- 休日

以下のコードはバグを抱えています。どのような引数を与えたときに問題が起こるでしょうか？

引数の値をいろいろ変更して、バグを起こす値を見つけてください。

## 問４

以下の`is_negative`関数は処理内容がシンプルのわりに、コードが複数行にわたり冗長です。同等の内容を一行で実現する`concise_is_negative`関数を作成してください。

## 問５a-c/問６

`ketchup`/`mustard`/`onion` はそれぞれホットドッグのトッピングを表します。それぞれの関数を完成させてください。

## 問７

トランプのブラックジャックでひき*ヒット*するべきか判定する関数`should_hit`関数を完成させてください。

- dealer_total：ディーラの合計
- player_total：プレイヤーの合計
- player_low_aces：プレイヤーの1としてカウントするエースの数
- player_high_aces：プレイヤーの11としてカウントするエースの数

たとえば、手持ちが{A, A, A, 7}なら、11 + 1 + 1 + 7になり、player_total=20 player_low_aces=2 player_high_aces=1