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

# 3) Look at the weights

ニューラルネットの重み（`weight`）は`tensors`と呼ばれる型で保存されています。

`tensor`は`list`型と似たような機能を持っており、[GPU]](https://www.kaggle.com/docs/efficient-gpu-usage)や[TPU](https://www.kaggle.com/docs/tpu)を利用して高速に動作するため、ディープラーニングに特化しています。

モデルの重みは`weights`プロパティで参照することができます。

作ったモデルの重みを参照してみましょう。

例

```
print("重み\n{}\n\nバイアス\n{}".format(w, b))
``` 

# Optional: Plot the output of an untrained linear model

シリアルのカロリーのような、数値を予測するようなタスクは回帰(`regression`)タスクといいます。

この場合はシリアルのカロリーに一致するような一次関数の傾きと重みを探すことになります。

学習させる前のモデルのパラメーターはランダムに設定されています。

下のセルを実行して、どのような線になるか確認してみましょう。

# Deep Neural Networks

# Introduction #

In the tutorial, we saw how to build deep neural networks by stacking layers inside a `Sequential` model. By adding an *activation function* after the hidden layers, we gave the network the ability to learn more complex (non-linear) relationships in the data.

In these exercises, you'll build a neural network with several hidden layers and then explore some activation functions beyond ReLU. Run this next cell to set everything up!

# 1) Input Shape #

The target for this task is the column `'CompressiveStrength'`. The remaining columns are the features we'll use as inputs.

What would be the input shape for this dataset?

# 2) Define a Model with Hidden Layers #

Now create a model with three hidden layers, each having 512 units and the ReLU activation.  Be sure to include an output layer of one unit and no activation, and also `input_shape` as an argument to the first layer.

# 3) Activation Layers #

Let's explore activations functions some.

The usual way of attaching an activation function to a `Dense` layer is to include it as part of the definition with the `activation` argument. Sometimes though you'll want to put some other layer between the `Dense` layer and its activation function. (We'll see an example of this in Lesson 5 with *batch normalization*.) In this case, we can define the activation in its own `Activation` layer, like so:

```
layers.Dense(units=8),
layers.Activation('relu')
```

This is completely equivalent to the ordinary way: `layers.Dense(units=8, activation='relu')`.

Rewrite the following model so that each activation is in its own `Activation` layer.