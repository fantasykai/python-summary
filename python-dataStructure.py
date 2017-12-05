#!/usr/local/bin/python3.6

print("列表")
print("Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能")
print("list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。")
print("list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。")
print("list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。")
print("list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。")
print("list.pop([i])	从列表的指定位置删除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被删除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）")
print("list.clear()	移除列表中的所有项，等于del a[:]。")
print("list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。")
print("list.count(x)	返回 x 在列表中出现的次数。")
print("list.sort()	对列表中的元素进行排序。")
print("list.reverse()	倒排列表中的元素。")
print("list.copy()	返回列表的浅复制，等于a[:]。")
print("")

print("将列表当做堆栈使用")
print("列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来")

stack = [1, 2, 3, 4, 5]
stack.append(6)
stack.append(7)

print("stack : ", stack)

stack.pop()
stack.pop()
stack.pop()

print("stack : ", stack)

print()
print("将列表当作队列使用")

print("也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。")

from collections import deque

queue = deque(["Google", "Bing", "Baidu"])

queue.append("Sogou")
queue.append("360")
queue.popleft()

print("queue : ", queue)

print()

print("列表推导式")

print("列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。")


vec = [2, 4, 6]

vec1 = [3 * x for x in vec]

print('vec1: ', vec1)

vec2 = [[x, x**2] for x in vec]


print("vec2: ", vec2)
