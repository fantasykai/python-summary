#!/usr/local/bin/python3.6

var1 = 'Hello, Python'
var2 = 'kai.fantasy'

print('var1 = ', var1)
print('var2 = ', var2)

print('var1[0] ', var1[0])
print('var2[1:5]', var2[1:5])

print('更新 ', var1[:6] + var2)

print('')
print('Python转义字符')

print('\(在行尾时)	续行符')
print('\\	反斜杠符号')
print('\'	单引号')
print('\"	双引号')

print('\a	响铃')
print('\b	退格(Backspace)')
print('\e	转义')
print('\000	空')
print('\n	换行')
print('\v	纵向制表符')
print('\t	横向制表符')
print('\r	回车')
print('\f	换页')
print('\oyy	八进制数，yy代表的字符，例如：\o12代表换行')
print(r'\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行')
print('\other	其它的字符以普通格式输出')
print('')

print('Python字符串格式化')

print('Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。')


print('这个学生是 %s 他的学号 %d ~' % ('张三', 1003212))

print('python字符串格式化符号')

print('%c	 格式化字符及其ASCII码')
print('%s	 格式化字符串')
print('%d	 格式化整数')
print('%u	 格式化无符号整型')
print('%o	 格式化无符号八进制数')
print('%x	 格式化无符号十六进制数')
print('%X	 格式化无符号十六进制数（大写）')
print('%f	 格式化浮点数字，可指定小数点后的精度')
print('%e	 用科学计数法格式化浮点数')
print('%E	 作用同%e，用科学计数法格式化浮点数')
print('%g	 %f和%e的简写')
print('%G	 %f 和 %E 的简写')
print('%p	 用十六进制数格式化变量的地址')
print('')
print('格式化操作符辅助指令:')

print('*	定义宽度或者小数点精度')
print('-	用做左对齐')
print('+	在正数前面显示加号( + )')
print('<sp>	在正数前面显示空格')
print(r'#	在八进制数前面显示零 0 在十六进制前面显示 0x 或者 0X 取决于用的是 x 还是 X ')
print(r'0	显示的数字前面填充 0 而不是默认的空格')
print(r'%	 % %输出一个单一的 % ')
print('(var)	映射变量(字典参数)')
print('m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)')
print('')


print('三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。')
print('')
print('Python 的字符串内建函数')
print('')
print('')
