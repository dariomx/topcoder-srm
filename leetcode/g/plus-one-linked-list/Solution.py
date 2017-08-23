# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rev_list(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev, head

    def add_one(self, head, tail):
        node = head
        rem = 1
        while node:
            tmp = node.val + rem
            node.val = tmp % 10
            rem = tmp / 10
            node = node.next
        if rem > 0:
            tail.next = ListNode(rem)

    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head, tail = self.rev_list(head)
        self.add_one(head, tail)
        return self.rev_list(head)[0]

