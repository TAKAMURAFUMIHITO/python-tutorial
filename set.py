s = {"A", "B", "C", "A"}
print(s)

# 要素の追加
s.add("D")
print(s)

# 要素の削除
s.remove("A")
print(s)

# 要素の削除(存在しない要素でもエラーが出ない)
s.discard("A")
print(s)

# 変更させないset
f = frozenset({"A", "B", "C"})
print(f)

print("--------------------")

# 集合演算
s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}

## 和集合
wa = s1.union(s2)
print(wa)

## 積集合
seki = s1.intersection(s2)
print(seki)

## 差集合
### s1だけ持っている要素
sas1 = s1.difference(s2)
print(sas1)

### s2だけ持っている要素
sas2 = s2.difference(s1)
print(sas2)

## 包含判定
s1 = {'A', 'B', 'C'}
s2 = {'A', 'B'}
### 含んでいるか
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s1.issubset(s1)) # true

### 含まれているか
print(s2.issuperset(s1))
print(s1.issuperset(s2))
print(s1.issubset(s1)) # true