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


