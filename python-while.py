#!/usr/local/bin/python3.6

print("Python中的循环语句有 for 和 while")

n = 100

sum = 0
counter = 1

while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d " % (n, sum))

print("while 循环使用 else 语句")
print("在 while … else 在条件语句为 false 时执行 else 的语句块：")

count = 0
while count < 5:
    print(count, " 小于 5")
    count += 1
else:
    print(count, "大于或等于 5")


print()

print("类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中")


print("Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串")

sites = ["Google", "Bing", "Baidu", "Sougo", "360", "Taobao", "fantasykai.cc"]

for site in sites:
    if site == "Taobao":
        print("淘宝!")
        break
    print("循环数据 ", site)
else:
    print("没有循环数据!")
print("完成循环!")

print()
print("range()函数")

for i in range(1, 20, 2):
    print(i)


print("结合range()和len()函数以遍历一个序列的索引")

sites1 = ["Google", "Bing", "Baidu", "Sougo", "360", "Taobao", "fantasykai.cc"]

for i in range(len(sites1)):
    print(i, sites1[i])


print()
print("break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行")
print("continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。")

print("Python pass是空语句，是为了保持程序结构的完整性。")



