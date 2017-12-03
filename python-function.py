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
