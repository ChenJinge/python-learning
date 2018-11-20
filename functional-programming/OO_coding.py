# -*- coding: utf-8 -*-


## OO coding
## 封装 继承 多态
## 命名规范

## 类 实例
class Person(object):
    pass


## python 实例添加属性
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))
print L2[0].name
print L2[1].name
print L2[2].name


## python 中初始化实例
## python中访问限制 类似 java中 private protected public
class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.__gender = gender
        self.birth = birth
        for k, v in kw.iteritems():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print xiaoming.__name
print xiaoming.job


## 类的属性与实例是一个 、实例的属性则x相互独立、当实例属性和类属性重名时，实例属性优先级高


## 虽然私有属性无法从外部访问，但是，从类的内部是可以访问的


## python中方法也是属性，和属性类似，方法也分实例方法和类方法  也分私有方法 和 公共方法么？


## 类的继承 复用已有的代码  父类 子类（派生类） super(object, self).__init__（）



