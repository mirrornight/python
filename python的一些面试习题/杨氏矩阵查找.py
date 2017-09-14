# coding=utf-8

# 返回数组m行n列的值
def get_value(l, m, n):
    return l[m - 1][n - 1]

def f(l, num):
    m = len(l)
    n = len(l[0])
    r = 1
    c = n
    while r <= m and c >= 1:
        if get_value(l, r, c) > num:
            c -= 1
        elif get_value(l, r, c) < num:
            r += 1
        elif:
            return True  
    return False
            
    
        