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


print('isinstance 和 type 区别')
print('type 不会认为子类是一种父类类型')
print('isinstance 会认为子类是一种父类类型')


print('在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。')

bianliang = '''
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
4、在混合计算时，Python会把整型转换成为浮点数。
'''

print(bianliang)

print('========字符串==============')

str = 'kai.fantasy'

print('字符串', str)
print('第一个到倒数第二个所有的字符串 ', str[0:-1])
print('第一个字符 ', str[0])
print('第三个到第五个 ', str[2:5])
print('第第三到最后 ', str[2:])
print('两遍字符串 ', str * 2)
print('拼接字符串 ', str + 'TEST')


print('Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串')

print('kai.\nfantasy')
print(r'kai.\nfantasy')

# 反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行

print('Python 没有单独的字符类型，一个字符就是长度为1的字符串')

print(r'''Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误''')

print('1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。')
print('2、字符串可以用+运算符连接在一起，用*运算符重复。')
print('3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。')
print('4、Python中的字符串不能改变。')


print()


print('##### list ###########')


list = ['abcdef', 12345, 99.991, True, False]
tlinlist = [139, 'kai.fantasy']


print('list列表', list)
print('列表中第一个元素', list[0])
print('列表中第二个和第三个元素', list[1:3])
print('列表中第三个到最后', list[2:])
print('列表两遍', tlinlist * 2)
print('列表拼接', list + tlinlist)


lista = [1, 2, 3, 4, 5, 6, 7]

lista[0] = 9

lista[2:5] = [13, 14, 15]

print(lista)

print('1、List写在方括号之间，元素用逗号隔开。')
print('2、和字符串一样，list可以被索引和切片。')
print('3、List可以使用+操作符进行拼接。')
print('4、List中的元素是可以改变的。')

print()

print(' ========= Tuple（元组） =======')

tuple = ('abcde', 678, 90.23, True, False)
tinytuple = (133, 'kai.fantasy')

print('元组', tuple)
print('元组第一个元素', tuple[0])
print('元组第二个到第三个元素', tuple[1:3])
print('元组第三个元素到最后', tuple[2:])
print('元组两遍', tinytuple * 2)
print('元组数据拼接', tuple + tinytuple)
