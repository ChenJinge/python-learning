#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 基本数据类型: 整数 浮点数 字符串 布尔值 空值
a = 10
b = 3.14
c = 'it is terrific !'
d = u'棒极了'
e = True
f = False
g = None

# print 注意()的区别
print 'it is terrific !'
print "it is terrific !"
print '棒极了'
print u'棒极了'

# 逻辑运算 and or not == > <
print 0xff == 255

# 变量命名规则 变量名必须是大小写英文、数字和下划线（_）的组合，且不能用数字开头


# 定义字符串 转义 换行
str = 'Bob said \"I\'m OK \"'
print str  # Bob said "I'm OK".

# Python中raw字符串与多行字符串
# 前缀 r ''' 解决多个需要转义字符的问题 只能单行
# 多行字符串 ''' xxx ''' 需要转义符
# r'''xxx''' 多行字符串 不需要转义符
print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''

# 正数和浮点数在运算中的要注意的 如果同时存在精确度要安装浮点数类型给出结果

# python 集合数据类型：list tuple dic set
# 主要操作：
# 声明一个变量
L1 = ['Michael', 100, True]  # list
L2 = ('Michael', 100, True)  # tuple 一旦创建 便不可再修改
T1 = ('单元素tuple',)  # 单元素在声明时 追加 \,即可
T2 = ('a', 'b', ['A', 'B'])  # 若 tuple 中存在元素为list list为可变
D1 = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}  # dict 数据类型 类似于 java hash map, key value结构 ，数据无序
S1 = set(['Adam', 'Lisa', 'Bart', 'Paul'])
# 插入
L1.append('Paul')  # 尾部追加
L1.insert(0, 'Paul')  # 索引处添加 原元素索引值自动向后顺延
# 修改
L1[0] = 'Lyn'  # 索引处直接赋值即可将原值替换

# 删除
L1.pop()  # 尾部删除
L1.pop(2)  # 索引值处删除,后续元素索引值自动向前移动
S1.remove('Adam')

# 获取
print L1[0]
print L1[-1]
print D1['Adam']
print D1.get('Adam')
D1['Adam'] = 72

for key in D1:
    print key + ':', D1[key]

print 'Adam' in S1

for name in S1:
    print name

S1.add('Adam')

# 迭代 Python中，迭代是通过 for ... in 来完成的 enumerate(L1)

for index, name in enumerate(L1):
    print index, '-', name

for v in D1.values():
    print v

for v in D1.itervalues():
    print v

for key, value in D1.items():
    print key, ':', value

for key, value in D1.iteritems():
    print key, ':', value

# 列表生成式
print [x * (x + 1) for x in range(1, 100, 2)]

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


# 列表生成式 复杂处理可借用函数
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


# 列表生成式 条件过滤
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]


print toUppers(['Hello', 'world', 101])

# 条件判断和循环
score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'

age = 28
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'

# for while 循环 break 可以跳出循环 continue 直接进入下次循环
sum = 0
x = 1
while x < 100:
    sum = sum + x
    x = x + 2
print sum

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y


# python 编写函数 def 函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# Python函数之返回多值 表面是多个值，其实是一个tuple

import math


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
print r


# Python之递归函数 fact(n)可以表示为 n * fact(n-1)


# Python之定义默认参数

# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# Python之定义可变参数
def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)


print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

# 柯里化 偏函数
