
# pythonプログラミングⅠ&Ⅱ

## 第一回
- 自己紹介
- 授業全体の解説
- pythonについて
    - pythonでできること
    - 強み
- Kaggleについて
    - Kaggleとは
- プログラミング導入 [Intro to Programming]
    - 演算子と変数 [Arithmetic and Variables]
    - 関数 [Functions]
    - 型 [Data Types]
    - 比較演算子とIF文 [Conditions and Conditional Statements]
    - リスト [Intro to Lists]

## 第二回

- Python入門Ⅰ
    - Hello World [Hello, Python]
    - 関数定義とヘルプ関数 [Functions and Getting Help]
    - Booleansと比較演算子 [Booleans and Conditionals]
    - リスト [Lists]

## 第三回

- Python入門Ⅱ
    - ループとリスト操作 [Loops and List Comprehensions]
    - 文字列型と辞書型 [Strings and Dictionaries]
    - 外部ライブラリの使い方 [Working with External Libraries]    

## 第四回

- PandasⅠ
    - データフレームの作成と書き込み [Creating, Reading and Writing]
    - インデックスと選択、 [Indexing, Selecting & Assigning]    
    - 要約関数とマップ [Summary Functions and Maps]

 - データ可視化Ⅰ
    - Seabornの使い方 [Hello, Seaborn]
    - 折れ線グラフ [Line Charts]

## 第五回

- PandasⅡ
    - 集約と整列 [Grouping and Sorting]
    - 型とデータ補完 [Data Types and Missing Values]
    - 改名と結合 [Renaming and Combining]

 - データ可視化Ⅱ
    - 棒グラフとヒートマップ [Bar Charts and Heatmaps]
    - 散布図 [Scatter Plots]

## 第六回

- 機械学習I
    - モデルの仕組み [How Models Work]
    - データを読む [Basic Data Exploration]  

## 第七回

- 機械学習Ⅱ
    - シンプルなモデル [Your First Machine Learning Model]
    - モデルの評価 [Model Validation]        


## 第八回

- 機械学習Ⅲ
    - 学習不足と過学習 [Underfitting and Overfitting] 
    - モデルの仕組み [How Models Work]

## 第九回

- 機械学習Ⅲ 
    - インデックスと選択、 [Basic Data Exploration] 
    - 要約関数とマップ [Summary Functions and Maps]

## 第十回

- 機械学習Ⅳ
    - ランダムフォレスト [Random Forests] 

## 第十一回

- 機械学習Ⅴ
    - ニューロンのしくみ [A Single Neuron]
    - 深層ニューラルネットワーク、 [Deep Neural Networks]

## 第十二回

- 機械学習Ⅵ
    - 確率的勾配降下法 [Stochastic Gradient Descent]
    - 学習不足と過学習 [Overfitting and Underfitting]      

## 第十三回

- 機械学習Ⅵ
    - ドロップアウトと正規化 [Dropout and Batch Normalization] 
    - 二値分類 [Binary Classification]                                 

## 第十四回

- 機械学習Ⅶ
    - 畳み込み [The Convolutional Classifier]
    - 畳み込みとReakyLeLU [Convolution and ReLU]    
    - スライディングウインドウ [The Sliding Window]   

## 第十五回

- 機械学習Ⅷ
    - 畳み込みネットワークを改造してみる [Custom Convnets]
    - データの水増し [Data Augmentation]



以下　旧シラバス

# pythonプログラミングⅠ

## 第一回
- 自己紹介
- 授業全体の解説
- pythonについて
- pythonでできること、強み
- PEPとは
- インタープリター、機械語
- hello world

## 開発環境(docker, vscode, git, venv)

- dockerのインストール
- docker images
    - docker ps
    - docker attach
    - docker exec -it [containername] /bin/bash
    - docker start
    - docker stop
- linuxの基本操作
    - ls,cd,cat,touch
    - apt-get
    - apt-cache
- git
    - config
    - add
    - commit 
    - push
    - pull    

 - https://docs.microsoft.com/ja-jp/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
 - ハイパーバイザとコンテナ

教科書（Kaggle Courses) https://www.kaggle.com/learn

## 第n回
プログラミングの基本となる3つの処理【順次・分岐・反復】
- if
- for, while

### ビルドイン関数
- help
- enumerate

### リスト
- 操作(slicing, indexing)
- 関数(len,remove,append,sum,max,min,sort)
list結合

## 第n回

### パッケージマネジャとサードパーティー製パッケージ
# pip
    - pip install
    - pip freeze

requirement.txt

randomモジュール

### 課題
サイコロアプリ（n個, 和,積、いかさまサイコロ）

## 第n回
ファイル入出力
with open r rb w wb
正規表現
画像を読み取ってサイズを出力する
imgs/

- 圧縮画像(jpg)
- 無圧縮画像(bmp)

jpg判定関数

### 組み込み関数format(), 文字列メソッドstr.format(), f文字列
2,8,16進数
 - 16 == 0o20 == 0b10

文字コードとは
- asciiコード https://www.k-cube.co.jp/wakaba/server/ascii_code.html
- shift-jis http://charset.7jp.net/sjis.html
- uff-8

URLエンコードとは

base64とは

シフト演算
参照渡し、値渡し

### 課題
- https://www.setsuki.com/hsp/ext/segment/app0.htm
- https://beyondjapan.com/blog/2016/11/start-binary-reading-with-jpeg-exif/

- SOI(0xFF oxD8)
- 最後（0xff 0xd9)

###  画像


PILモジュール
cv2
crip
figure, axis
settitle
subplot
cmap

## 第n回
シーケンス図とは

ステートレス・ステートフル

get post

ステータスコード

200/401/500...etc

# リクエストデータのダンプ
req.prepare

urllib.request

header body
multipart json xml

http(s) websocket webrtc rtp webtransport

## 第n回
- timeモジュール
- スレッド

### 課題
- tcpのシーケンス図を描く

## 第n回

ハッシュ値
- MD5
- SHA-256

HTTP認証とは

https://developer.mozilla.org/ja/docs/Web/HTTP/Authentication#basic_%E8%AA%8D%E8%A8%BC%E6%96%B9%E5%BC%8F

- Basic認証/Digest認証

www-Authorizationヘッダー

https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/WWW-Authenticate

セッション、トークン

https://magazine.techcareer.jp/technology/skill/11273/


## 第n回
webサーバ構築(flask, uwsgi)

## 第n回
ユーザ認証
ログイン
公開鍵暗号

## 第n回
tcp/udpソケットプログラミング

## 第n回
- ブロードキャスト
- マルチキャスト　
- ユニキャスト　
- ループバック

## 第n回 
いろいろなプロトコル
- rtp, rtsp
- HLS
- webrtc(aiortc)
    - STUN
    - ステートフルインスペクション
    - SDP
    - ICE

## 第n回
パケット構造
リトルエンディアン/ビックエンディアン

# pythonプログラミングⅡ

## 第n回
データベース連携

postgres連携

- 射影,選択,結合（select,where,join)
- 挿入,削除,更新（insert, delete, update)

## 第n回
グラフ描画(matplotlib.pyplot)

##
 - 中央値
 - 平均値
 - 分散
 - 

## 第n回
- numpy
- scikit-learn

## 画像処理
画像をndarrayで扱ってみる
- RGB（A)とは

- 平均プーリング,Maxプーリング
- グレースケール
- 適応的閾値処理
- 二値画像
- アフィン変換
- 射影変換

グレースケールとは
https://qiita.com/yoya/items/96c36b069e74398796f3

- 演習
ビルボード置き換え

## 第n回
### 機械学習Ⅰ
評価指標

- 回帰タスク
- 分類タスク
- 多分類タスク

## 第n回

### 機械学習Ⅱ

- 行列の基礎
- 畳み込みニューラルネットワーク(CNN)
- ストライド
- フィルター

## 課題
fashion-mnistでの分類モデルの作成

https://www.kaggle.com/code/pavansanagapati/a-simple-cnn-model-beginner-guide/notebook