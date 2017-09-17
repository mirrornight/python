# coding=utf-8

# python魔术方法(magic method)
# 创建类的对象 __new__(cls)        :返回一个类的初始对象
# 初始化对象   __init__(self)      :
# 回收对象     __del__             :python的回收机制来调用的
#              __dict__            :如果实例调用，显示实例的属性。
#                                       如果是类调用，显示类的属性和方法。
# 查看对象属性 __dir__             :
#
#
# 比较运算(例二)
#              __eq__(self, other) :判断是否相等
#              __cmp__(self, other):比较
#              __it__(self, other) :小于
#              __gt__(self, other) :大于
# 数字运算
#              __add__(self, other):加
#              __sub__(self, other):减
#              __mul__(self, other):乘
#              __div__(self, other):除
# 逻辑运算  
#              __or__(self, other) :或
#              __and__(self, other):于
#
#
# 转换为字符串(类的展现)(例三)
#              把对象转换为字符串
#              __str__             :显示给用户看的(print)
#                                       >>>p = Person()
#                                       >>>print p
#              __repr__            :把对象转换为开发人员看的字符串(交互式环境下)
#                                       >>>p = Person()
#                                       >>>p
#              __unicode__         :
#
# eval函数将字符串当成有效Python表达式来求值，并返回计算结果
#                                   x = 1
#                                   eval('x+1')
#                                   eval('x==1')
# 与之对应的repr函数，它能够将Python的变量和表达式转换为字符串表示
#                                   repr(x==1)
#                                   repr(x+1)
#
#
# 设置对象属性(例四)
#              __setattr__         :当试图对象的item时将会被调用
#              __getattr__         :只有在对象属性不存在时调用
#              __getattribute__    :通过实例访问属性，都会经过__getattribute__函数，
#                                       而当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。 
#              __delattr__         :删除对象某个属性

# 例一
# class Person(object):
    # class_attribute = 'hello world'
    # def __new__(cls, *args, **kwargs):
        # print 'call __new__ method'
        # print args
        # return super(Person, cls).__new__(cls, *args, **kwargs)

    # def __init__(self, name, age):
        # print 'call __init__ method'
        # self.name = name 
        # self.age = age
    # def method(self):
        # pass

# if __name__ == '__main__':
    # p1 = Person('mirror', 13)
    # print p1.__dict__
    # print Person.__dict__
       
 
# 例二
# class Person(object):
    # def __init__(self, name, age):
        # self.name = name
        # if isinstance(age, int):
            # self.age = age
        # else:
            # raise Exception('age must be int')

    # def __eq__(self, other):
        # if isinstance(other, Person):
            # if self.age == self.age:
                # return True
            # else:
                # return False
        # else:
            # raise Exception('The type of object must be Person')

    # def __add__(self, other):
        # if isinstance(other, Person):
            # return self.age + other.age
        # else:
            # raise Exception('the type of object must be person')

# if __name__ == '__main__':
    # p1 = Person('mirror', 13)
    # p2 = Person('night', 13)
    # print p1.__eq__(p2)
    # print p1.__add__(p2)
    # print p1 + p2
    # print p1 == p2


#例三
# class Person(object):
    # def __init__(self, name, age):
        # self.name = name
        # if isinstance(age, int):
            # self.age = age
        # else:
            # raise Exception('age must be int')
    
    # def __str__(self):
        # return '%s is %s years old' % (self.name, self.age)

    # def __dir__(self):
        # return self.__dict__.keys()
    # __repr__ = __str__

# if __name__ == '__main__':
    # p = Person('hello', 13)
    # print p
    # print dir(p)


# 例四
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getattribute__(self, name):
        # return getattr(self, name)
        # return self.__dict__[name]
        # 上面这两种会引起无限递归
        print name
        return super(Person, self).__getattribute__(name)

    def __getattr__(self, item):
        print 'call_getattr'

    def __setattr__(self, name, value):
        # setattr(self, name, value)
        # 上面这一种会引起无限递归
        print 'call setattr'
        self.__dict__[name] = value
        
if __name__ == '__main__':
    # 创建时调用__dict__，和__setattr__
    p = Person('hello', 13)
    print 
    # 相当于p.__getattribute__(name)
    print p.name
    print p.weight
        
    
    






























