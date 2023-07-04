# リスト内包表記
data_list = [1, 2, 3, 4, 5]
new_list = [data * 2 for data in data_list]
print(new_list)

# 条件がつけられる
new_even_list = [data * 2 for data in data_list if data % 2 == 0]
print(new_even_list)

# 集合内包表記
data1 = [1, 2, 3, 4, 5]
data2 = {num * 2 for num in data1}
print(data2)

# 辞書内包表記
data3 = ["a", "b", "c", "d", "e"]
data4 = {word: word + word for word in data3}
print(data4)