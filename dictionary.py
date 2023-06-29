# 辞書型
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(d)

# 値へのアクセス
## この方法は、キーが存在しない場合にエラーとなる
print(d["key1"])
## getメソッドを使うと、キーが存在しない場合にNoneを返す
print(d.get("key2"))

# 値の追加
d["key4"] = "value4"
print(d)

# dictによる生成
d2 = dict()
print(d2)
d2["ドラえもん"] = "のび太"
print(d2)
d3 = dict(d2)
print(d3)

# 要素数
print(len(d))