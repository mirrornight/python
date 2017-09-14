class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def SwapPairs(head):
    if head != None and head.next != None:
        next_node = head.next
        head.next = SwapPairs(next_node.next)
        next_node.next = head
        return next_node
    return head