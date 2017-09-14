# coding=utf-8
def f1(a, b):
    s = list(a)
    t = list(b)
    s.sort()
    t.sort()
    if s == t:
        return True
    else:
        return False

# 有时候要判断一个数是否在一个序列里面，这时就会用到in运算符来判断成员资格
def f2(a, b):
    s = {}
    for i in a:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1
    for i in b:
        if i not in s:
            return False
        else:
            s[i] -= 1
            if s[i] == 0:
                s.pop(i)
    return s == {}

a = 'abcd'
b = 'dcab'
print f1(a, b)
print f2(a, b)