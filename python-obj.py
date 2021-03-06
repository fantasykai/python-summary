#!/usr/local/bin/python3.6

print("Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的")
print()
print("面向对象技术简介")
print("类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。")
print("类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。")
print("数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。")
print("方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。")
print("实例变量：定义在方法中的变量，只作用于当前实例的类。")
print("继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟 '是一个（is-a）'关系（例图，Dog是一个Animal）。")
print("实例化：创建一个类的实例，类的具体对象。")
print("方法：类中定义的函数。")
print("对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。")
print("和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。")
print("Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。")
print("对象可以包含任意数量和类型的数据。")
print()
print("类定义")
print("语法格式如下")
'''
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>


'''
print("类实例化后，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。")
print("类对象")
print("类对象支持两种操作：属性引用和实例化")
print("属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。")
print("类对象创建后，类命名空间中所有的命名都是有效属性名。")
print()


class MyClass(object):
    i = 12345

    def f(self):
        return "hello python"


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 的类属性 i 为： ", x.i)
print("MyClass 的类方法 f 为： ", x.f())
print()


class Complex(object):
    """docstring for ClassName"""

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x. i)

print()
print("self代表类的实例，而非类")

print("类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。")

print()


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()


print()
print("类的方法")

print("在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。")
print()


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = 0
        self.__weight = w

    def speak(self):
        print("%s 说： 我 %d 岁。" % (self.name, self.age))


p = people('kai.fantasy', 10, 30)
p.speak()


print()
print("继承")
print("Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。")
print("需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。")
print("BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:")
print("")


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()

print()
print("多继承")
print("Python同样有限的支持多继承形式")
'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

'''
print("需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。")

# 类定义


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()


print()
print("方法重写")
print("如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法，实例如下：")


class Parent:        # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法

print()
print("类属性与方法")
print("类的私有属性")
print("__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。")
print("类的方法")
print("在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，self 代表的是类的实例。")
print("self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。")
print("类的私有方法")
print("__private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。")
print("self.__private_methods。")
print("实例")
print("类的私有属性实例如下：")


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公有变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)## 报错，实例不能访问私有变量
#
print()
print("类的私有方法实例如下：")


class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):          # 私有方法
        print('这是私有方法')

    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('个人博客', 'fantasykai.cc')
x.who()
x.foo()
# x.__foo() 报错
