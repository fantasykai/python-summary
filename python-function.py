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
