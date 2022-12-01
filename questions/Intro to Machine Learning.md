
# How Models Work

たとえば、あなたのいとこが不動産を運用していて、既にそのビジネスで成功していたとします。

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