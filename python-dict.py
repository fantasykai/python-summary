#!/usr/local/bin/python3.6

print("字典是另一种可变容器模型，且可存储任意类型对象。")
print("字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ")

print("键必须是唯一的，但值则不必。")
print("值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。")
print("")

dict1 = {'name': 'kai.fantasy', 'age': 28}
print("dict1 = ", dict1)

print("访问字段的值")
print(" dict1['name'] = ", dict1['name'])

print("向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对")


dict = {'name': 'kai.fanasy', 'age': 28,
        'language': ['java', 'javascript', 'python']}

print("dict = ", dict)

dict['age'] = 29

print("更新 age | dict['age'] = 29 | ", dict)

dict['site'] = 'fantasykai.cc'
print("添加字段 | dict['site'] = ", dict)

print()
print("删除字典元素")
print("能删单一的元素也能清空字典，清空只需一项操作")
print("用 del 命令进行删除操作")

dict2 = {'name': 'kai.fanasy', 'age': 28,
        'language': ['java', 'javascript', 'python']}

print("dict2 = ", dict2)        

del dict2['age']
print("删除字典某个元素 del dict2['age'] ", dict2)
dict2.clear()
print("清空字段数据 dict2.clear() ", dict2)

del dict2

print("删除字典 del dict2 ")


print("字典内置函数&方法 ")
print("1	len(dict) 计算字典元素个数，即键的总数。")
print("2	str(dict) 输出字典，以可打印的字符串表示。")
print("3	type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。")
print("")

print("1	radiansdict.clear() 删除字典内所有元素")
print("2	radiansdict.copy() 返回一个字典的浅复制")
print("3	radiansdict.fromkeys() 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值")
print("4	radiansdict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值")
print("5	key in dict 如果键在字典dict里返回true，否则返回false")
print("6	radiansdict.items() 以列表返回可遍历的(键, 值) 元组数组")
print("7	radiansdict.keys() 以列表返回一个字典所有的键")
print("8	radiansdict.setdefault(key, default=None) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default")
print("9	radiansdict.update(dict2) 把字典dict2的键/值对更新到dict里")
print("10	radiansdict.values() 以列表返回字典中的所有值")
print("11	pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。")
print("12	popitem() 随机返回并删除字典中的一对键和值(一般删除末尾对)。")
print("")
print("")




