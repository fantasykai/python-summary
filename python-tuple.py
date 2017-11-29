#!/usr/local/bin/python3.6


print("Python 的元组与列表类似，不同之处在于元组的元素不能修改")
print("元组使用小括号，列表使用方括号")

tup1 = ('Google', 'Bing', 'Baidu', 2017, True, 1000.20)
tup2 = (1, 2, 3, 4, 5, 6, 7)
tup3 = ('a', 'b', 'c', 'd', 'e')
print("元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用")
tup4 = (1,)

print('tup1 ', tup1)
print('tup2 ', tup2)
print('tup3 ', tup3)
print('tup4 ', tup4)

print('元组可以使用下标索引来访问元组中的值')

print("tup1[1] ", tup1[1])

print("元组中的元素值是不允许修改的")

print("元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组")

print("元组运算符")

print("与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组")

print("len((1, 2, 3))	3	计算元素个数")
print("(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接")
print("('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制")
print("3 in (1, 2, 3)	True	元素是否存在")
print("for x in (1, 2, 3): print x,	1 2 3	迭代")

print("元组内置函数")

print("1	len(tuple)计算元组元素个数。")
print("2	max(tuple)返回元组中元素最大值。")
print("3	min(tuple)返回元组中元素最小值。")
print("4	tuple(seq)将列表转换为元组。")
