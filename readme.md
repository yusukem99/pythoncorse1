
# pythonプログラミングⅠ

## 第一回
- 自己紹介
- 授業全体の解説
- pythonについて
- pythonでできること、強み
- PEPとは
- インタープリター、機械語
- hello world

## 開発環境(docker, vscode, venv)

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

https://docs.microsoft.com/ja-jp/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

 - ハイパーバイザとコンテナ

教科書（Kaggle Courses)

https://www.kaggle.com/learn

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
requirement.txt

randomモジュール

### 課題
サイコロアプリ（n個, 和,積、いかさまサイコロ）

## 第n回
ファイル入出力
with open r rb w wb

2,8,16進数
 - 16 == 0o20 == 0b10

 ### 課題
 - 100 = 
 - 150 =

文字コードとは
- asciiコード
- shift-jis
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

# 課題
jpg判定関数

## 第n回
git
- config
- add
- commit 
- push
- pull


###  画像
- 圧縮画像(jpg)
- 無圧縮画像(bmp)

PILモジュール
cv2
crip
figure, axis
settitle
subplot
cmap

正規表現

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

## 第n回
- numpy
- scikit-learn

## 画像処理
画像をndarrayで扱ってみる
- RGB（A)とは

- 平均プーリング,Maxプーリング
- グレースケール
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