#!/usr/local/bin/python3.6

# python 保留字
import keyword
import sys


print("python's keyword", keyword.kwlist)

# input("\n\n 按 回车 键退出。 ")

print("命令行参数为： ")

for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
print('')


print('python 数据类型')
print('数字类型：int, float, decimal.Decimal, fractions.Fraction, complex')
print('字符串类型：str, bytes')
print('列表: list')
print('集合: set')
print('元组：tuple')
print('字典: dict')
print('冻结集合：frozenset')
print('布尔类型：True, False')
print('None')


print('----- 愉快的分割线 ---------')

counter = 100             # 整数
miles = 1000.0            # 浮点数
octal = 0o177, 0x9ff, 0X9FF, 0b101010  # 八进制
change = hex(10), oct(10), bin(10)
nums = float('inf'), float('-inf'), float('nan')
name = 'kai.fantasy'  # 字符串
a, b, c, d = 1, 100.234, True, 'kai'  # 多变量赋值还可以这样玩

print(counter)
print(miles)
print(octal)
print(name)
print('将十进制数转化为十六进制、八进制、二进制表示的“字符串', change)
print('无穷大, 无穷小, 非数', nums)
print(a, b, c)

print('---- 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。----')

print('## type() 函数可以用来查询变量所指向的对象类型')

print(type(a), type(b), type(c), type(d))

print('也可以用 isinstance 来判断')

print(isinstance(a, int)


print('isinstance 和 type d 区别')

print('type 不会认为子类是一种父类类型')
print('isinstance 会认为子类是一种父类类型')


print('在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。')
		