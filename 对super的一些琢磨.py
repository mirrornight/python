# coding=utf-8
# 理解创建实例的过程
# 和super的用法

# super不是一个函数！
# super(cls, inst):(这是一种大致实现，因为返回的是一个super类的对象)
    # mro = inst.__class__.mro()
    # mro[mro.index(cls) + 1]

class Root(object):
    def __init__(self):
        print 'this is root'

class B(Root):
    def __init__(self):
        print 'enter B'
        super(B, self).__init__()
        print 'leave B'

class C(Root):
    def __init__(self):
        print 'enter C'
        super(C, self).__init__()
        print 'leave C'

class D(B, C):
    pass


# # 创建实例d
# r = object.__new__(Root)
# print isinstance(r, Root)
# # 初始化d 第一种方法
# r.__init__()
# print isinstance(r, Root)
# # 初始化d 第二种方法
# Root.__init__(r)
# print isinstance(r, Root)


d = D()
# print d.__class__.mro()[0] == D

# print super(B, d)
# print super(B, d).__init__()
# print C.__init__(d)


class Root(object):
    def __init__(self):
        print 'this is root'

class B(Root):
    def __init__(self):
        print 'enter B'
        Root.__init__(self)
        print 'leave B'

class C(Root):
    def __init__(self):
        print 'enter C'
        Root.__init__(self)
        print 'leave C'

class D(B, C):
    pass

d = D()






