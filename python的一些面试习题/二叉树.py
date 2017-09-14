# coding=utf-8
# 遍历二叉树
class Node(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

# 广度遍历 提示：使用队列
def lookup(root):
    queue = [root]
    while queue:
        current = queue.pop(0)
        print current.data
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# 深度遍历(前序)
def deep_1(root):
    if not root:
        return 
    print root.data
    deep(root.left)
    deep(root.right)

# 中序遍历
def deep_2(root):
    if not root:
        return 
    deep(root.left)
    print root.data
    deep(root.right)

# 后序遍历
def deep_3(root):
    if not root:
        return 
    deep(root.left)
    deep(root.right)
    print root.data

# 求最大树深
def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# 判断两棵树是否相同
def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
    
if __name__ == '__main__':
    # lookup(tree)
    # deep(tree)
    print maxDepth(tree)


    

