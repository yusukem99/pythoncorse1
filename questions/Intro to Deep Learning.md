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

## 2) Define a Model with Hidden Layers #

それでは、中間層に3つのレイヤーを含むモデルを作成しましょう。それぞれ512の出力と活性化関数にReLUを使います。

出力は1つで、活性化関数はつけません。最初のレイヤーには引数に`input_shape`をつける必要があります。

# 3) Activation Layers #

Let's explore activations functions some.

The usual way of attaching an activation function to a `Dense` layer is to include it as part of the definition with the `activation` argument. Sometimes though you'll want to put some other layer between the `Dense` layer and its activation function. (We'll see an example of this in Lesson 5 with *batch normalization*.) In this case, we can define the activation in its own `Activation` layer, like so:

```
layers.Dense(units=8),
layers.Activation('relu')
```

This is completely equivalent to the ordinary way: `layers.Dense(units=8, activation='relu')`.

Rewrite the following model so that each activation is in its own `Activation` layer.

# Optional: Alternatives to ReLU #

There is a whole family of variants of the `'relu'` activation -- `'elu'`, `'selu'`, and `'swish'`, among others -- all of which you can use in Keras. Sometimes one activation will perform better than another on a given task, so you could consider experimenting with activations as you develop a model. The ReLU activation tends to do well on most problems, so it's a good one to start with.

Let's look at the graphs of some of these. Change the activation from `'relu'` to one of the others named above. Then run the cell to see the graph. (Check out the [documentation](https://www.tensorflow.org/api_docs/python/tf/keras/activations) for more ideas.)

