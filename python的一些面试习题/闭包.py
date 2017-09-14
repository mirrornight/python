# coding=utf-8

# 函数对象的作用域与def所在的层级相同。比如下面代码，
# 我们在line_conf函数的隶属范围内定义的函数line，
# 就只能在line_conf的隶属范围内调用。
# def line_conf():
    # def line(x):
        # return 2 * x + 1
    # print line(5)

# line_conf()



# 闭包
# def line_conf():
    # def line(x):
        # return 2 * x + 1
    # return line

# my_line = line_conf()
# print my_line(5)


# 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)。
# 在Python中，所谓的闭包是一个包含有环境变量取值的函数对象。
def line_conf():
    b = 15
    def line(x):
        return 2 * x + b
    return line

b = 5
my_line = line_conf()
# __closure__里包含了一个元组(tuple)。这个元组中的每个元素是cell类型的对象。
# 我们看到第一个cell包含的就是整数15，也就是我们创建闭包时的环境变量b的取值。
print my_line.__closure__
print my_line.__closure__[0].cell_contents
print my_line(5)


