#!/usr/local/bin/python3.6


print("你可以定义一个由自己想要功能的函数，以下是简单的规则 ")

print("函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。")
print("任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。")
print("函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。")
print("函数内容以冒号起始，并且缩进")
print("return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。")
print("Python 定义函数使用 def 关键字，一般格式如下")


def area(width, heigt):
    return width * heigt


def print_welcome(name):
    print("Hello ", name)


print_welcome("kai.fantasy")

w = 4
h = 5

print("width = ", w, "heigt = ", h, " area = ", area(w, h))

print("函数调用")

print("定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。")

print("这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。")

print("参数传递")

print("可更改(mutable)与不可更改(immutable)对象")

print("在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象")
print("不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。")
print(
    "可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。")

print("python 函数的参数传递：")

print("不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。")

print("可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响")
print("python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。")


def changeInt(a):
    a = 10


b = 2

changeInt(b)

print(b)

print("实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它")

print("传可变对象实例")

print("可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了")


def chageme(mylist):
    mylist.append([1, 2, 3, 4, 5])
    print("函数内 mylist 的值 ： ", mylist)
    return


# 调用函数
mylist = [10, 20, 30, 40, 50]
print("调用函数前 mylist的值： ", mylist)
chageme(mylist)

print("调用函数后 mylist的值: ", mylist)

print("参数")
print("以下是调用函数时可使用的正式参数类型")

print("必需参数")
print("关键字参数")
print("默认参数")
print("不定长参数")
print("")
print("必须参数")
print("必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样")
print("关键字参数")

print("关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值")
print("使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值")


def printInfo(name, age):
    print("name : ", name)
    print("age : ", age)
    return


printInfo(age=28, name='kai.fantasy')

print("默认参数")

print("调用函数时，如果没有传递参数，则会使用默认参数")

print("默认参数不在最后，会报错")

def printInfo(name, age=30):
    print("name : ", name)
    print("age : ", age)
    return


printInfo(name='zhangsan')


print("不定长参数 ")
print("能处理比当初声明时更多的参数。这些参数叫做不定长参数")


'''
def functionname([formal_args, ] * var_args_tuple):
    "函数_文档字符串"
    function_suite
    return [expression]`
'''


def printInfo(arg1, *vartuple):
    print("输出： ")
    print("arg1 = ", arg1)
    for var in vartuple:
        print("var ", vartuple)

    return


print(10)
print(20, 30, 40, 50)

print("匿名函数")
print("python 使用 lambda 来创建匿名函数")
print("所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数")

print("lambda 只是一个表达式，函数体比 def 简单很多")
print("lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去")
print("lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。")
print("虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。")

print("语法")

print("lambda 函数的语法只包含一个语句")

print(" lambda [arg1 [,arg2,.....argn]]:expression ")
print("lambda 匿名函数也是可以使用"关键字参数"进行参数传递, 同样地，lambda 匿名函数也可以设定默认值")


def sum(arg1, arg2): return arg1 + arg2
## sum = lambda arg1, arg2: arg1 + arg2;


print("相加后的值 ： ", sum(10, 20))

print("return语句 ")
print(
    "return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值")


def sum(arg1, arg2):
    total = arg1 + arg2
    print("total : ", total)
    return total


total1 = sum(30, 20)
print("total1 : ", total1)


print("变量作用域: ")
print("Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的")
print("变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是")
print("L （Local） 局部作用域")
print("E （Enclosing） 闭包函数外的函数中")
print("G （Global） 全局作用域")
print("B （Built-in） 内建作用域")
print()
print("以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。")


x = int(2.9)  # 内建作用域

g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        o_count = 2  # 局部作用域


print("Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这这些语句内定义的变量，外部也可以访问")

print("全局变量和局部变量")
print("定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。")
print("局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中")
print("")
total = 0  # 这是一个全局变量
# 可写函数说明


def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)


print()

print("global 和 nonlocal关键字")
print("当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了")

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()


print()

print("如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了")


def outer():
    num = 10

    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)


outer()
