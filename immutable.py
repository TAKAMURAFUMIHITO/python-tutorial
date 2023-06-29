# Pythonのオブジェクトには、固有の番号が振られています。組込みのid関数はそのオブジェクトの固有の番号を取得します。
num = 100
text = "aaaa"
dic = {'key': 200}
 
print(id(num)) # 変数numの固有番号が出力される
print(id(text)) # 変数textの固有番号が出力される
print(id(dic)) # 変数decの固有番号が出力される

print("-------------------")

text1 = "aaa"
text2 = text1
text3 = text1 + 'bbb'
 
print(id(text1))
print(id(text2)) # text1を参照しているためtext1と同じID
print(id(text3)) # text1とはIDが異なる
 
print("-------------------")

text1 = "bbb"
print(id(text1)) # もともとのIDとは異なる