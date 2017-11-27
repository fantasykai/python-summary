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
