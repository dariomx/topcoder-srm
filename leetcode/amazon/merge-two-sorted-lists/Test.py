from Solution import Solution
from sys import stdout as out

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printList(head):
    node = head
    while node:
        out.write(str(node.val))
        out.write(",")
        node = node.next
    out.write("\n")

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

printList(Solution().mergeTwoLists(l1,l2))
