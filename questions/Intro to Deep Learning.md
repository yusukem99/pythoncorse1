# A Single Neuron

## Introduction
ニューラルネットワークの構成要素の一つである`liner unit`（線形ユニット）について学びました。

シリアルのカロリー予測の例で見たように、ただ一つの線形ユニットを含むモデルは一次関数になります。

これは単純な線形回帰と同じです。

この練習では線形モデルの使い方を学びましょう。

ここに`Red Wine Quality`という1600点のポルトガル産ワインの成分データがあります。

このデータは評論家によるブラインドテストの評点(quality rating)を含んでいます。

下のコードを実行して数行を表示してみましょう。

さらに`DataFrame`型の持つ`shape` メソッドを使って、このデータセットがいくつの行と列を持つのか確認しましょう。

## 1) Input shape

ワインのどの成分から評点を予想できるでしょうか？

ここで予測したいものは品質（`quality`）とし、残りの項目を特徴量とします。

モデルの入力`input_shape`にはどのような値を設定すればよいでしょうか？

## 2) Define a linear model

それでは線形モデルを定義しましょう。

ヒント：モデルはいくつの入力と出力をもつべきでしょうか？

## 3) Look at the weights

ニューラルネットの重み（`weight`）は`tensors`と呼ばれる型で保存されています。

`tensor`はインデックスやスライスの機能を持っており、`numpy`や`list`型と似た性質があります。

また、[GPU](https://www.kaggle.com/docs/efficient-gpu-usage)や[TPU](https://www.kaggle.com/docs/tpu)を利用して高速に動作するため、ディープラーニングに特化しています。

モデルの重みは`weights`プロパティで参照することができます。

作ったモデルの重みを参照してみましょう。

例

```
print("重み\n{}\n\nバイアス\n{}".format(w, b))
``` 

## Optional: Plot the output of an untrained linear model

シリアルのカロリーのような、数値を予測する問題を回帰(`regression`)タスクといいます。

この場合はシリアルのカロリーに一致するような一次関数の傾きと重みを探すことになります。

学習させる前のモデルのパラメーターはランダムに設定されています。

下のセルを実行して、どのような線になるか確認してみましょう。

# Deep Neural Networks

## Introduction

`Sequential` レイヤーを積み重ねることで、階層型のニューラルネットワークを構築することができました。

さらに、中間層(`hidden layers`)に活性化関数(`activation function`)を追加することで、ニューラルネットワークにより複雑なデータの関係性を学習させることができます。

この練習問題では、中間層に複数のレイヤーを含むニューラルネットワークを作成します。また、`ReLU`以外の活性化関数について見ていきましょう。

コンクリートのデータセットが用意されています。ここではコンクリートの成分に基づいて、その圧縮強度(`compressive strength`)を予測してみましょう。

## 1) Input Shape

ここでの予測対象は`CompressiveStrength`の列で、残りのすべての列を特徴量とします。

`input_shape`はどのような値になるでしょうか？

## 2) Define a Model with Hidden Layers

それでは、中間層に3つのレイヤーを含むモデルを作成しましょう。それぞれ512の出力と活性化関数にReLUを使います。

出力は1つで、活性化関数はつけません。最初のレイヤーには引数に`input_shape`をつける必要があります。

## 3) Activation Layers

全結合層(`Dense layer`)の引数に`activation`を指定することで活性化関数を追加することができました。

しかし、全結合層(`Dense layer`)と活性化関数(`Activation Function`)の間に*別のレイヤーを追加したい場合はどうすればいいでしょうか？

このようなときは下のように各レイヤを独立して記述することができます。

```
layers.Dense(units=8),
layers.Activation('relu')
```

これはと下の処理と全く同じです。

```
layers.Dense(units=8, activation='relu')
```

*たとえばバッチ正規化(`batch normalization`)などがあります。

次のモデルを独立した活性化レイヤを使うように書き直してください。

## Optional: Alternatives to ReLU

活性化関数には`'relu'` の他にも`'elu'`や`'selu'`、`'swish'`などがあります。

ときには他に活性化関数を使ってみると、より高い予測精度がでることがあります。

ReLUは一般的に多くのタスクでよい性能がでるため、広く使われています。

他の活性化関数をグラフを書いて確認してみましょう。

下のセルの活性化関数の名前を`'relu'`から別のものに変更して、セルを実行してみてください。

活性化関数の[ドキュメント](https://www.tensorflow.org/api_docs/python/tf/keras/activations)も読んでみましょう。

