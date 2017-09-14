# coding=utf-8
class ListNode(object):
    def __init__(self, s):
        self.val = s
        self.next = None
def f(a,b):
    # 先得到a，b的长度, p为a的指针， q为b的指针
    i = 0
    j = 0
    p = a
    q = b 
    while p:
        i += 1
        p = p.next
    while q:
        j += 1
        q = q.next
    # 长的先运行|a - b|，直到两个一样长
    p = a
    q = b
    k = abs(i - j)
    if i > j:
        while k > 0:
            p = p.next
            k -= 1
    elif i < j:
        while k > 0:
            q = q.next
            k -= 1
    # p，q到交点的距离相同
    while p != q:
        p = p.next
        q = q.next
    # 检测p, q不为None
    if p:
        return p
    else:
        return False

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
d.next = c

print f(a, d).val

            