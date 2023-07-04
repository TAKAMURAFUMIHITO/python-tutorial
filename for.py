# for文
datas = [1, 2, 3, 4, 5]
for data in datas:
    print(data)

print("-------------------")

# 辞書型のfor文はキーや値でループが回せる
dict = {'key1': 100, 'key2': 200, 'key3': 300}
for key in dict:
    print(key)
for key in dict:
    print(dict[key])

## 値を直接取得する時はvalues()メソッドを使う
for value in dict.values():
    print(value)

## キーと値を同時にループして取得する時はitems()メソッドを使う
for key, value in dict.items():
    print(key, value)

print("-------------------")

# 何番目の要素だけは処理をしない、等の処理を入れたい場合はループインデックスを利用しますが、これはenumerate関数で取得することができます。
l = ['a', 'b', 'c']
  
for i, value in enumerate(l):
    print(i, value) # ループインデックスとリストの値が出力
  
for i, (key, value) in enumerate(dict.items()):
    print(i, key, value) # ループインデックスとkeyと値が出力


dic = {'key1': 110, 'key2': 270, 'key3': 350}
  
for i, value in enumerate(dic):
    print(i, value) # ループインデックスと値が出力
  
for i, (key, value) in enumerate(dic.items()):
    print(i, key, value) # ループインデックスとkeyと値が出力

print("-------------------")

l = [0, 3, 1, -10, 11, 6]
for x in l:
    if x < 0:
        print("負の数を検知しました。処理をスキップします。")
        continue
        #　print("ここの処理はスキップされる")
    else:
        print(x)
