l = [1, 2, 3, 4, 5]

#リストの要素数を取得
print(len(l))

#リストの最後の要素を取得
print(l[-1])
print(l[len(l)-1])

#リストに要素を追加
l.append(6)
print(l)

#リストの好きなところに要素を追加
l.insert(0, 0)
print(l)

#リストの要素を削除
l.remove(0)
l.remove(6)
print(l)

#取り出して削除
x = l.pop(0)
print(x)
print(l)