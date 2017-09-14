# coding=utf-8
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法

# 第一种
def memo(f):
    cache = {}
    def wrap(args):
        if args not in cache:
            cache[args] = f(args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i <= 2:
        return i
    return fib(i - 1) + fib(i - 2)

print fib(100)

# 第二种 太慢了
# f = lambda n: n if n <= 2 else f(n - 1) + f(n - 2)
# print f(4)

# 第三种
def f(i):
    a, b = 0, 1
    while i > 0:
        a, b = b, a + b
        i -= 1
    return b

print f(100)

def f(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b

print f(100)

