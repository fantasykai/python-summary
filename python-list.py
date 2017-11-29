#!/usr/local/bin/python3.6

print('Python有6个序列的内置类型，但最常见的是列表和元组。')
print('序列都可以进行的操作包括索引，切片，加，乘，检查成员。')
print('Python已经内置确定序列的长度以及确定最大和最小的元素的方法。')
print('列表的数据项不需要具有相同的类型')

list1 = ['Google', 'Bing', 'Baidu', 2017, True, 1000.20]
list2 = [1, 2, 3, 4, 5, 6, 7]
list3 = ['a', 'b', 'c', 'd', 'e']

print('list1 = ', list1)
print('list2 = ', list2)
print('list3 = ', list3)

print('list1[0] ', list1[0])
print('list1[1:5] ', list1[1:5])

print(' list1[3] 为 ', list1[3])
list1[3] = 2018
print(' list1[3] 更新为 ', list1[3])

print()
print('删除列表元素')

print('可以使用 del 语句来删除列表的的元素')

list = ['Google', 'Bing', 'Baidu', 2017, True, 1000.20]

print('list = ', list)

del list[3]

print(' del list[3] ', list)
