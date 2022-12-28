
# How Models Work

たとえば、あなたのいとこが不動産を運用するビジネスで成功していたとします。

彼はあなたが学校でPythonを習ったということを聞いて、一緒にビジネスをやろうと持ちかけてきました。

彼は資金と不動産のデータを提供するので、あなたはその不動産の価値を予測するモデル（機械学習で予測を算出する計算式）を作るということになりました。

不動産に関してあなたは知識がなかったので、これまでどのように不動産を価値を予測していたのか彼に聞いてみました。

彼はなんとなく直観で分かるものだとい言いました。

しかしさらに掘り下げて聞いてみると、どうやら過去の不動産の価格から特定のパターンを見出しているということが分かりました。

機械学習の仕組みも彼のやっていることと同じで、過去のデータから一定の規則を見つけだし、その規則を計算式に変換しています。

モデルには様々な種類がありますが、ここではもっともシンプルな決定木(Decision Tree)と呼ばれるモデルを作成してみます。

まず下の画像を見てください。

まず住宅を二つの二つのカテゴリーに分けます。

さらにそれぞれの予想価格をその条件でのグループの価格の平均値とします。

この分岐条件を作るステップを、モデルを学習またはモデルをフィットするなどといいます。学習に使用したデータを訓練データといいます。

下の図でどちらがより住宅データのパターンをとらえているといえるでしょうか？

寝室が少ない家より多い家のほうがより高い値段がつくでしょうから、明らかに左の決定木のほうが良い決定木になっていると言えます。

しかしながら、住宅の価格を決定するものとして他にも敷地面積や浴室の数、立地など重要な要素があるのでこの決定木は完璧ではありません。

下の図はさらに多くの要素を使ってデータのパターンをとらえています。このように分岐を増やし決定木の深度を上げることによってよりよいモデルになります。

完成した決定木の分岐をたどることによって住宅の価格を予想することができます。たどり着いた最後の点を葉(leaf)と言います。

決定木の分岐条件や葉の値は訓練データによって決まります。まずは与えられたデータを詳しくみていきましょう。

# Basic Data Exploration

## 問１
アイオワ州の住宅データのファイル`'../input/home-data-for-ml-course/train.csv'`を`DataFrame`型として変数`home_data`に代入してください。

## 問２
チュートリアルで扱った`DataFrame`のメソッドを使って要約統計を作成してください。
さらに、その統計を用いて下の変数に適切な値を代入してください。

`avg_lot_size`:敷地面積の平均(整数)
`newest_home_age`:一番新しい家の築年数

## 問３
一番新しい家でも、作られてからかなりの年数がたっているようです。
これはなぜでしょうか？二つの仮説をたててみます。

- このデータが作られてから、新しい家は建てられていない
- このデータはかなり昔につくられたものであり、データがつくられた後に建てられた家はこのデータに含まれていない。

もし前者が正しければ、モデルの作成に悪影響を与えるでしょうか？また後者だとうでしょうか？

あなたの考えを書いてください。下のリンクのディスカッションを参考にしてアイデアを出してみましょう。

# Your First Machine Learning Model

## 問1 予測対象`y`を決める
予測対象の変数、ここでは住宅の販売価格を探して、`y`に代入してください。
販売価格を表す変数名が分からないときは列名の一覧を出力してみましょう。

## 問2 特徴量`X`を決定する
次は予測に使う因子(特徴量)を決定して,`X:DataFrame`に代入してください。

まずは特徴量として使用する項目のリストを作り、その後データ全体から対象の列を抜き出しましょう。

ここでは下の一覧をコピーして使ってもよいものとします。

- LotArea
- YearBuilt
- 1stFlrSF
- 2ndFlrSF
- FullBath
- BedroomAbvGr
- TotRmsAbvGrd

# Review Data¶
Before building a model, take a quick look at X to verify it looks sensible

Step 3: Specify and Fit Model¶
Create a DecisionTreeRegressor and save it iowa_model. Ensure you've done the relevant import from sklearn to run this command.

Then fit the model you just created using the data in X and y that you saved above.

Step 4: Make Predictions¶
Make predictions with the model's predict command using X as the data. Save the results to a variable called predictions.

Think About Your Results
Use the head method to compare the top few predictions to the actual home values (in y) for those same homes. Anything surprising?


# Model Validation

# Underfitting and Overfitting

# Random Forests

# Machine Learning Competitions