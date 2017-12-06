#!/usr/local/bin/python3.6

import math

print("Python3 输入和输出")

print("输出格式美化")
print("Python两种输出值的方式: 表达式语句和 print() 函数。")
print("第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。")
print("如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。")
print("如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。")
print("str()： 函数返回一个用户易读的表达形式。")
print("repr()： 产生一个解释器易读的表达形式。")
print("")
print("")
print("")

s = "Hello, World"
print("str(s) ", str(s))
print("repr(s)", repr(s))

print()

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

print()

for x in range(1, 11):
    print('{0:2d} {1:3d} {2: 4d}'.format(x, x * x, x * x * x))

print()
print("注意：在第一个例子中, 每列间的空格由 print() 添加。")
print("这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。")
print("还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。")
print("另一个方法 zfill(), 它会在数字的左边填充 0")
print()

var1 = '24'.zfill(5)

print("var1 : ", var1)

print("str.format() 的基本使用如下")
print('{}网址： "{}!"'.format('个人博客', 'fantasykai.cc'))
print("大括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。")
print("在括号中的数字用于指向传入对象在 format() 中的位置")
print('{0} 和 {1}'.format('Google', 'Bing'))
print('{1} 和 {0}'.format('Google', 'Bing'))
print("")
print("如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。")
print('{name}网址： {site}'.format(name='个人博客', site='fantasykai.cc'))
print("位置及关键字参数可以任意的结合:")
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Bing',
                                         other='Taobao'))


print()
print("'!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:")
print()
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print()
print("可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位")
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
