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
