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
