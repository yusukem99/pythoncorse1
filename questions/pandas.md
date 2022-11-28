# Creating, Reading and Writing

## 問１

変数`fruits`に図のような`DataFrame`を代入してください。

## 問２

変数`fruit_sales`に図のような`DataFrame`を代入してください。

## 問３

変数`ingredients`に以下のような`Series`を代入してください。

```
Flour     4 cups
Milk       1 cup
Eggs     2 large
Spam       1 can
Name: Dinner, dtype: object
```

## 問４

CSVファイルからデータを取得して、変数`reviews`に以下のような`DataFrame`を代入してください。

CSVファイルのパス
`../input/wine-reviews/winemag-data_first150k.csv`

このCSVファイルの最初の数行は以下のようになっています。

,country,description,designation,points,price,province,region_1,region_2,variety,winery
0,US,"This tremendous 100% varietal wine[...]",Martha's Vineyard,96,235.0,California,Napa Valley,Napa,Cabernet Sauvignon,Heitz
1,Spain,"Ripe aromas of fig, blackberry and[...]",Carodorum Selección Especial Reserva,96,110.0,Northern Spain,Toro,,Tinta de Toro,Bodega Carmen Rodríguez

# Indexing, Selecting & Assigning

まずコードセル[11]を実行して`animals`を定義してください。
次に`cows_and_goats.csv`という名前で`animals`をディスクに保存してください。

## 問１
`reviews`から`description`の列を選択して、変数`desc`に代入してください。また`desc`の型は何でしょうか？

`type()`関数を使って調べてみてください。

## 問２
`reviews`から`description`行の最初の値を選択して、変数`first_description`に代入してください。

## 問３
`reviews`から最初の行を選択して、変数`first_row`に代入してください。

## 問４
`reviews`の`description`列から最初の１０行を選択して、変数`first_descriptions`に代入してください。

## 問５
下の画像のように、`reviews`からインデックスが1,2,3,5,8の行を選択して`sample_review`に代入してください。

## 問６
下の画像のように、`reviews`からインデックスが0, 1, 10, 100の行かつprovince, region_1, and region_2の列を選択して`df`に代入してください。

## 問７
`loc()`または`iloc()`を使って、`reviews`から最初の100行を選択して`df`に代入してください。

**ヒント**

`iloc()`は最後のインデックスは含みません。一方で`loc()`は最後のインデックスも含めた行を選択します。

 例えば、`iloc[0:1000]`は1000個の行を選択しますが`loc[0:1000]`は1001個の列を取得します。

## 問８
`reviews`からイタリア産のワインのみ選択して、`italian_wines`に代入してください。

## 問９
`reviews`から生産国がオーストラリアまたはニュージーランドかつ、評点(points)が95以上の行をを選択して`top_oceania_wines`に代入してください。

# Summary Functions and Maps

## 問１
`points`列の中央値はいくつになるでしょうか？

## 問２
`reviews`のうち`country`はどのような値があるでしょうか？重複のないように`countries`に代入してください。

## 問３
それぞれの国のデータは合計でいくつずつ入っているでしょうか？`reviews_per_country`に各国の行数の合計値を入れてください。

## 問４

変数`centered_price`に`price`行のそれぞれの値から`price`の平均値を引いた引いたものを代入してください。

このような操作を中心化(centering)といい、機械学習の前処理として行われることがあります。

## 問５
もっともお買い得なワインはどれでしょうか？`bargain_wine`に`points`/`price`の比率がもっとも高いワイン名(`title`)を代入してください。

## 問６
`description`を読んでみると色々な言葉でワインの味が表現されています。

ここで`tropical`と`ftuity`のどちらで表現されることが多いでしょうか？

変数`descriptor_counts`に`Series`型でそれぞれの単語が使われた行の数をを代入してください。

例
```
>descriptor_counts

tropical    10
fruity      20
dtype: int64
```

## 問７

ワインレビューをウェブサイトで公開しようと思います。

しかしこのデータの評点(points)は80-100の範囲になっているため、３段階の星の格付けに変更します。

95点以上なら`3`, 85点以上で95より低ければ`2`,それ以外は`1`の値を持つように、`Series`型の値を`star_ratings`に代入してください。

さらにカナダワイン協会から支援を受けることになったので、カナダ産のワインは無条件で星3とします。