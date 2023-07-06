# 位置引数
def sample_function(a: int, b: int) -> int:
    sum = a + b
    return sum

print(sample_function(8, 9))


# デフォルト値を設定する
def sample_function2(a: int, b: int = 9) -> int:
    sum = a + b
    return sum

print(sample_function2(8))


# キーワード引数
# 引数の順番を気にしなくて良い
def sample_function3(a: int, b: int = 5) -> int:
    sum = a + b
    return sum

print(sample_function3(b=8, a=9))
# ただし、位置引数とキーワード引数を混在させる場合は、位置引数を先に記述する必要がある
# print(sample_function3(8, a=9)) # エラーになる 


# リストを使った引数 *listとすることで、リストの中身を展開して引数として渡すことができる
def sample_function4(a: int, b: int = 5) -> int:
    sum = a + b
    return sum

list = [8, 9]
print(sample_function4(*list))


# 辞書を使った引数 **dictとすることで、辞書の中身を展開して引数として渡すことができる
def sample_function5(a: int, b: int = 5) -> int:
    sum = a + b
    return sum

dict = {'a': 8, 'b': 9}
print(sample_function5(**dict))


# 可変長引数
# 引数の数が可変の場合に使用する
# 可変長引数は、引数の前に*をつける
def sample_function6(*args) -> int:
    sum = 0
    for i in args:
        sum += i
    return sum

print(sample_function6(8, 9, 10, 11, 12))


def sample_function7(x, y, *args):
    print(x, y, args)
 
sample_function7("a", "b")           # 引数2つ
# a b ()
 
sample_function7("a", "b", "c")      # 位置引数1つ追加
# a b ('c',)
 
sample_function7("a", "b", "c", "d") # 位置引数2つ追加
# a b ('c', 'd')


# キーワード可変長引数
# 引数の数が可変の場合に使用する
# 可変長引数は、引数の前に**をつける
def sample_function8(**kwargs):
    print(kwargs)
    
sample_function8(a=1, b=2, c=3)


# 関数内でグローバル変数を変更する
# globalをつけることで、関数内でグローバル変数を変更することができる
x = 0
def sample_function9():
    global x
    x = 1
    print(x)

sample_function9()
print(x) # 0ではなく1が出力される


# オブジェクト関数
def sample_function10():
    return "sample"

text = sample_function10() # 通常の呼び出し
print(text)

f = sample_function10 # 関数を変数に代入
text = f() # 関数オブジェクトを実行
print(text)


# 関数の引数に関数を渡す
def param_func():
    return 'sample'
 
def sample_function11(f):
    x = f()
    print(x)
 
sample_function11(param_func)