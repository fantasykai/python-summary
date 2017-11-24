#!/usr/local/bin/python3.6

# python 保留字
import keyword
import sys


print("python's keyword", keyword.kwlist)

## input("\n\n 按 回车 键退出。 ")

print("命令行参数为： ")

for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
print('')


print('python 数据类型')
print('数字类型：int, float, decimal.Decimal, fractions.Fraction, complex')
print('字符串类型：str, bytes')
print('元组：tuple')
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

print(counter)
print(miles)
print(octal)
print(name)
print('将十进制数转化为十六进制、八进制、二进制表示的“字符串', change)
print('无穷大, 无穷小, 非数', nums)
