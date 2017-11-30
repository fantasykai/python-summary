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





