#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
import math
import time


# python把函数作为参数
def add(x, y, f):
    return f(x) + f(y)


print add(25, 9, math.sqrt)


# python中map()函数
def format_name(s):
    return s[0].upper() + s[1:].lower()


print map(format_name, ['admin', 'LISA', 'barT'])


# python中reduce()函数
def prod(x, y):
    return x * y;


print reduce(prod, [2, 4, 5, 7], 10)


# python中filter()函数
def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


print filter(is_sqr, range(1, 101))


# python中sorted()函数 自定义排序函数
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


# python 中返回函数
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y

        return reduce(f, lst, 1)

    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print f()


# python 中闭包 特点：返回的函数 依赖了主函数的变量
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g()

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()

# python 中匿名函数
# lambda x: x * x 实际上就是：
#
# def f(x):
#     return x * x
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# # python 装饰器  相当于java spring aop , 源于函数代理
# def performance(f):
#     def fn(*args, **kwargs):
#         t1 = time.time()
#         r = f(*args, **kwargs)
#         t2 = time.time()
#
#         print 'call %s() in %fs' % (f.__name__, (t2 - t1))
#         return r
#
#     return fn
#
#
# @performance
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
#
# print factorial

# # python 中编写带参数 decorator
# def performance(unit):
#     def perf_decorator(f):
#         def wrapper(*args, **kwargs):
#             t1 = time.time()
#             r = f(*args, **kwargs)
#             t2 = time.time()
#             t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
#             print 'call %s() in %f %s' % (f.__name__, t, unit)
#             return r
#
#         return wrapper
#
#     return perf_decorator
#
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x, y: x * y, range(1, n + 1))
#
#
# print factorial(10)


# python中完善decorator 要让调用者看不出一个函数经过了@decorator的“改造”
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial.__name__

# python中偏函数（给缺省值赋值） 、柯里化
sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

# python 封装 抽象 类似 java class、package  __init__.py
# 导入模块 import  from ... import


# 动态导入，也就是通过顺语句式的导入
try:
    import json
except ImportError:
    import simplejson as json
print json.dumps({'python': 2.7})


# 旧版本 python 使用高版本 python 功能
# 要在Python 2.7中引入3.x的除法规则，导入__future__的division：
#
# >>> from __future__ import division
# >>> print 10 / 3
# 3.3333333333333335


# 安装第三方模块
# - easy_install
# - pip install

# 安装特定版本呢？ 卸载呢？