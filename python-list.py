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

print('删除列表元素 del list[3] ', list)

print('')
print('Python列表脚本操作符')

print('列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。')

print('len([1, 2, 3])	3	长度')
print('1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	组合')
print(r"['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复")
print('3 in [1, 2, 3]	True	元素是否存在于列表中')
print('for x in [1, 2, 3]: print(x, end=" ")	1 2 3	迭代')
print('')

print('Python列表截取与拼接')
print('Python的列表截取与字符串操作类型')
print(r"L[2]	'Google'	读取第三个元素")
print(r"L[-2]	'Kai.fantasy'	从右侧开始读取倒数第二个元素: count from the right")
print(r"L[1:]	['Google', 'Bing']	输出从第二个元素开始后的所有元素")

print('嵌套列表')

alist = ['a', 'b', 'c', 'd', 'e']
blist = [1, 2, 3, 4, 5]

clist = [alist, blist]

print('alist = ', alist)
print('blist = ', blist)
print('clist = ', clist)
print('')
print('Python列表函数&方法')
print('1	list.append(obj) 在列表末尾添加新的对象')
print('2	list.count(obj) 统计某个元素在列表中出现的次数')
print('3	list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）')
print('4	list.index(obj) 从列表中找出某个值第一个匹配项的索引位置')
print('5	list.insert(index, obj) 将对象插入列表')
print('6	list.pop(obj=list[-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值')
print('7	list.remove(obj) 移除列表中某个值的第一个匹配项')
print('8	list.reverse() 反向列表中元素')
print('9	list.sort([func]) 对原列表进行排序')
print('10	list.clear() 清空列表')
print('11	list.copy() 复制列表')
print('')

listTest = ['Google', 'Bing', 'Baidu', 'Google', 2017, True, 1000.20]
listTest.append('Sogou')

extend = ['360', 'zhihu']
listTest.extend(extend)
listTest.insert(4, 'douban')
listTest.remove('douban')
listTest.reverse()
listTest1 = listTest.copy()


print('listTest = ', listTest)
print('listTest 元素个数 ', len(listTest))
print("listTest.append('Sogou') ", listTest)
print("listTest.count('Google') ", listTest.count('Google'))
print("list.extend(seq) ", listTest)
print("list.index(obj)  ", listTest.index('Baidu'))
print("list.insert(index, obj) ", listTest)
print("list.pop(obj=list[-1]) ", listTest.pop())
print("list.remove(obj) ", listTest)
print("list.reverse() ", listTest)
print("list.copy() ", listTest1)
listTest1.clear()
print("list.clear() ", listTest1)
