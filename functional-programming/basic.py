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
L3 = ('单元素tuple',)  # 单元素在声明时 追加 \,即可
L4 = ('a', 'b', ['A', 'B'])  # 若 tuple 中存在元素为list list为可变
D1 = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}  # dict 数据类型 类似于 java hash map, key value结构 ，数据无序
# 插入
L1.append('Paul')  # 尾部追加
L1.insert(0, 'Paul')  # 索引处添加 原元素索引值自动向后顺延
# 修改
L1[0] = 'Lyn'  # 索引处直接赋值即可将原值替换

# 删除
L1.pop()  # 尾部删除
L1.pop(2)  # 索引值处删除,后续元素索引值自动向前移动

# 获取 & 迭代
print L1[0]
print L1[-1]
print D1['Adam']
print D1.get('Adam')