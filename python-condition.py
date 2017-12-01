#!/usr/local/bin/python3.6

print("Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块")

print("1、每个条件后面要使用冒号（:），表示接下来是满足条件后要执行的语句块。")
print("2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。")
print("3、在Python中没有switch – case语句")
print("")

print("在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。")

age = int(input("请输入狗狗的年龄： "))

print("")

if age < 0:
	print("呵呵哒，前世就不知道了")
elif age == 1:
    print("相当于 14 岁的人类")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄： ", human)        	

input(" enter 退出")    