# coding=utf-8
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9)))))))))

def f(q):
    # 先将链表中的元素取出，按顺序放入list中
    stack = []
    while q:
        next_node = q.next
        q.next = None
        stack.append(q)
        q = next_node
    index = len(stack) - 1
    # 再将链表重新连接（重后往前的顺序）
    while index > 0:
        stack[index].next = stack[index - 1]
        index -= 1
    return stack[-1]

print f(link).next.next.next.next.next.next.next.next.data
    