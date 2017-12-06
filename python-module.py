#!/usr/local/bin/python3.6

import sys

print('命令行参数如下:')

for i in sys.argv:
    print(i)


print()
print("Python3.6 的路径为： ", sys.path)

print("1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。")
print("2、sys.argv 是一个包含命令行参数的列表。")
print("3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。")

print("import 语句")

print("想使用 Python 源文件，只需在另一个源文件里执行 import 语句")

print("import module1[, module2[,... moduleN]")

print("解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。")

print("搜索路径是一个解释器会先进行搜索的所有目录的列表。")

print("一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行")
print("当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢?")
print("这就涉及到Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块")
print("这看起来很像环境变量，事实上，也可以通过定义环境变量的方式来确定搜索路径。")
print("搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量")
print("sys.path 输出是一个列表，其中第一项是空串''，代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）")

print("")

print("from…import 语句")
print("Python的from语句让你从模块中导入一个指定的部分到当前命名空间中")
print("")
print("From…import* 语句")
print("把一个模块的所有内容全都导入到当前的命名空间也是可行的")

print("深入模块")

print("模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。")
print("每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。")
print("所以，模块的作者可以放心大胆的在模块内部使用这些全局变量，而不用担心把其他用户的全局变量搞花。")
print("从另一个方面，当你确实知道你在做什么的话，你也可以通过 modname.itemname 这样的表示法来访问模块内的函数。")
print("模块是可以导入其他模块的。在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，当然这只是一个惯例，而不是强制的。被导入的模块的名称将被放入当前操作的模块的符号表中。")
print("还有一种导入的方法，可以使用 import 直接把模块内（函数，变量的）名称导入到当前操作模块")
print("如： from fibo import fib, fib2")

print("__name__属性")
print("一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行")

if __name__ == '__main__':
    print("程序自身运行")

else:
    print("其他模块")


print("dir() 函数")
print("内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回")
print("")
print("dir(sys) ", dir(sys))
