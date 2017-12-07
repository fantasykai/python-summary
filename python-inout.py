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

print()
print("在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用")
print()

table = {'Google': 1, 'Bing': 2, 'Baidu': 3}
for name, num in table.items():
    print('{0:10} ==> {1:10d}'.format(name, num))


print()
print("如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情")
print("最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值")


table = {'Google': 1, 'Bing': 2, 'Baidu': 3}
print(
    'Google: {0[Google]:d}; Bing: {0[Bing]:d}; Baidu: {0[Baidu]:d}'.format(table))

print("也可以通过在 table 变量前使用 '**' 来实现相同的功能")
table = {'Google': 1, 'Bing': 2, 'Baidu': 3}
print('Google: {Google:d}; Bing: {Bing:d}; Baidu: {Baidu:d}'.format(**table))

print()
print("旧式字符串格式化")
print("% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串.")
print('常量 PI 的值近似为：%5.3f。' % math.pi)

print("因为 str.format() 比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format().")
print("")
print("读取键盘输入")
print("Python提供了 input() 置函数从标准输入读入一行文本，默认的标准输入是键盘")
print("input 可以接收一个Python表达式作为输入，并将运算结果返回")
print()
str = input(" 请输入您的姓名 ：")
print(" 您输入的是： ", str)
print()
print("读和写文件")
print("open() 将会返回一个 file 对象，基本语法格式如下")
print(" open(filename, mode)")
print("filename：filename 变量是一个包含了你要访问的文件名称的字符串值")
print("mode：mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)")


f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "w")
f.write(" python读取文件不错，方便啊, open 文件 \n 先来个写入测试看看~~\n")
f.close()

print()

print("第一个参数为要打开的文件名")
print("第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。")
print()
print("文件对象的方法")
print("本节中剩下的例子假设已经创建了一个称为 f 的文件对象。")
print("f.read()")
print("为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回")
print("size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回")
print()

f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "r")
str = f.read()
print(str)

f.close()


print("f.readline()")
print("f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。")
print()
f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "r")
str = f.readline()
print(str)
f.close()

print()

print("f.readlines()")

print("f.readlines() 将返回该文件中包含的所有行")
print("如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。")

f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "r")
str = f.readlines()
print(str)

f.close()


print("")
print("另一种方式是迭代一个文件对象然后读取每行:")

f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "r")

for line in f:
    print(line, end='')

f.close()

print()
print("这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。")
print("f.write()")
print("f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。")

print()

f = open("/Users/makai/workspace/github/fantasykai/python-summary/test.txt", "w")
num = f.write(" python读取文件不错，方便啊, open 文件 \n 先来个写入测试看看~~\n")

print(num)

f.close()

print()

print("如果要写入一些不是字符串的东西, 那么将需要先进行转换:")
f = open("/Users/makai/workspace/github/fantasykai/python-summary/test1.txt", "w")


f.close()

print()

print("f.tell()")
print("f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。")
print("f.seek()")
print("如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。")
print("from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，")
print("seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符")
print("seek(x,1) ： 表示从当前位置往后移动x个字符")
print("seek(-x,2)：表示从文件的结尾往前移动x个字符")
print("from_what 值为默认为0，即文件开头")

f = open("/Users/makai/workspace/github/fantasykai/python-summary/test2.txt", "rb+")
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)
f.read(1)

f.close()
