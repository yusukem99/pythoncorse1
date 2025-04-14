数学における関数

`y = x + 3`

x = 1 のとき、y = 4
x = 2 のとき、y = 5

xを変化させると、得られるyの値も変化する。

Pythonの関数
```
def add_three(input_var):
    output_var = input_var + 3
    return output_var
```

input_var = 1 のとき、output_var = 4 また input_var = 2 のとき、output_var = 5

def = 定義(define)

add_three = 関数名(function)

input_var = 引数(argument)

output_var = 戻り値(return value)

defの下の字下げされた（インデント）中身をbodyという

引数に特定の値を入れて実行することを「関数を呼び出す」（"call" a function）という

```
new_number = add_three(10)
```

bodyの中で作成した変数は、bodyの外では使えない。bodyの中の世界を「スコープ」という。
