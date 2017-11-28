#!/usr/local/bin/python3.6

print('Python算术运算符')
print('+	加 - 两个对象相加')
print('-	减 - 得到负数或是一个数减去另一个数')
print('*	乘 - 两个数相乘或是返回一个被重复若干次的字符串')
print('/	除 - x 除以 y')
print('%	取模 - 返回除法的余数')
print('**	幂 - 返回x的y次幂')
print('//	取整除 - 返回商的整数部分')
print('')

a = 21
b = 10
c = 0

c = a + b
print('a + b c = ', c)

c = a - b
print('a - b c = ', c)

c = a * b
print('a * b c = ', c)

c = a / b
print('a / b c = ', c)

c = a % b
print('a % b c = ', c)


# 修改a, b, c

a = 2
b = 3
c = a ** b
print('a ** b c = ', c)

a = 10
b = 5
c = a // b
print('a // b c = ', c)


print('Python比较运算符')

print()
print('==	等于 - 比较对象是否相等')
print('!=	不等于 - 比较两个对象是否不相等')
print('>	大于 - 返回x是否大于y')
print('<	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。注意，这些变量名的大写。	')
print('>=	大于等于 - 返回x是否大于等于y。')
print('<=	小于等于 - 返回x是否小于等于y。')


print('')
print('Python赋值运算符')
print('=	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c')
print('+=	加法赋值运算符	c += a 等效于 c = c + a')
print('-=	减法赋值运算符	c -= a 等效于 c = c - a')
print('*=	乘法赋值运算符	c *= a 等效于 c = c * a')
print('/=	除法赋值运算符	c /= a 等效于 c = c / a')
print('%=	取模赋值运算符	c %= a 等效于 c = c % a')
print('**=	幂赋值运算符	c **= a 等效于 c = c ** a')
print('//=	取整除赋值运算符	c //= a 等效于 c = c // a')

a = 21
b = 10
c = 0

print('a = ', a)
print('b = ', b)
print('c = ', c)

c = a + b
print(' c = a + b : ', c)

c += a
print(' c += a : ', c)

c *= a
print(' c += a : ', c)

c /= a
print(' c /= a : ', c)

c = 2
c %= a
print(' c = 2 c %= a : ', c)

c **= a
print(' c **= a : ', c)

c //= a
print(' c //= a : ', c)

print('')
print('Python位运算符')

print('按位运算符是把数字看作二进制来进行计算的')

print('&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b) 输出结果 12 ，二进制解释： 0000 1100')
print('|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b) 输出结果 61 ，二进制解释： 0011 1101')
print('^	按位异或运算符：当两对应的二进位相异时，结果为1	(a ^ b) 输出结果 49 ，二进制解释： 0011 0001')
print('~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1	(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。')
print('<<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。	a << 2 输出结果 240 ，二进制解释： 1111 0000')
print('>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果 15 ，二进制解释： 0000 1111')
print('')

a = 60   # 60 = 0011 1100
b = 13   # 13 = 0000 1101
c = 0
print('a = ', a)
print('b = ', b)
print('c = ', c)

c = a & b     # 12 = 0000 1100
print('a & b  = ', c)


c = a | b     # 61 = 0011 1101
print('a | b = ', c)

c = a ^ b     # 49 = 0011 0001
print('a ^ b = ', c)

c = ~a       # -61 = 1100 0011
print('~a = ', c)

c = a << 2    # 240 = 1111 0000
print('a << 2 = ', c)

c = a >> 2    # 15 = 0000 1111
print('a >> 2 = ', c)

print()
print('Python逻辑运算符')


print('and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。')
print('or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。')
print('not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False')

a = 10
b = 20

print('a = ', a)
print('b = ', b)


if (a and b):
    print('a and b | a 和 b 都为 True')
else:
    print('a and b | a 和 b 有一个不为 true')


if (a or b):
    print('a or b | a 和 b 都为 True 或其中1个为True')
else:
    print('a or b | a 和 b 都不为True')

a = 0
print('a = ', a)
if (a and b):
    print('a and b |  a 和 b 都为 True')
else:
    print('a and b | a 和 b 有一个不为 true')


if (a or b):
    print('a or b | a 和 b 都为 True 或其中1个为True')
else:
    print('a or b | a 和 b 都不为True')

if not(a and b):
    print('not(a and b) | a 和 b 都为 False 或其中1个为False')
else:
    print('not(a and b) | a 和 b 都为True')


print()

print('Python成员运算符')
print('in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。')
print('not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。')

a = 10
b = 20
list = [1, 2, 3, 4, 5]
print('a = ', a)
print('b = ', b)
print('list = ', list)


if (a in list):
    print('a in list |  a 在 list 中')
else:
    print('a in list | a 不在 list 中')

if (b not in list):
	print('b not in list |  b 不在 list 中')
else: 
	print('b not in list |  b 在 list 中')


print(' Python身份运算符 ')	

print('is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False')
print('is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。')


print(' id() 函数用于获取对象内存地址。')



