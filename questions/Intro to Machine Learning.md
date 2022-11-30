
# How Models Work

たとえば、あなたのいとこが不動産を運用していて、既にそのビジネスで成功していたとします。

彼はあなたがPythonを学校で習ったということを聞いて、一緒にビジネスをやろうと持ちかけてきました。

彼は資金と不動産のデータを提供するので、あなたはその不動産の価値を予測するモデル（機械学習で予測を算出する計算式）を作るということになりました。

不動産に関してあなたは知識がなかったので、これまでどのように不動産を価値を予測していたのか彼に聞いてみました。

彼はなんとなくは直観で分かるものだとい言いました。

さらに掘り下げて聞いてみると、どうやら過去の不動産の価格から特定のパターンを見出しているということが分かりました。

機械学習の行っていることも全く同じで過去のデータから一定の規則を見つけだし、その規則を計算式に変換しています。

モデルには様々な種類がありますが、ここではもっともシンプルな決定木と呼ばれるモデルを作成してみます。

まず下の画像を見てください。

まず住宅を二つの二つのカテゴリーに分けます。

さらにそれぞれの予想価格をその条件でのグループの価格の平均値とします。

この分岐条件を作るステップをモデルを学習、またはフィットするなどといいます。学習に使用したデータを訓練データといいます。

下の図でどちらがより住宅データのパターンをとらえているといえるでしょうか？

Improving the Decision Tree
Which of the following two decision trees is more likely to result from fitting the real estate training data?

First Decision Trees

The decision tree on the left (Decision Tree 1) probably makes more sense, because it captures the reality that houses with more bedrooms tend to sell at higher prices than houses with fewer bedrooms. The biggest shortcoming of this model is that it doesn't capture most factors affecting home price, like number of bathrooms, lot size, location, etc.

You can capture more factors using a tree that has more "splits." These are called "deeper" trees. A decision tree that also considers the total size of each house's lot might look like this:Depth 2 Tree

You predict the price of any house by tracing through the decision tree, always picking the path corresponding to that house's characteristics. The predicted price for the house is at the bottom of the tree. The point at the bottom where we make a prediction is called a leaf.

The splits and values at the leaves will be determined by the data, so it's time for you to check out the data you will be working with.

Continue