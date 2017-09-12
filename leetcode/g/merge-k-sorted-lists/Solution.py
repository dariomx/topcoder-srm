# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def append(self, head, tail, node):
        if head == None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
        node.next = None
        return head, tail

    def merge(self, l1, l2):
        n1 = l1
        n2 = l2
        head, tail = None, None
        while n1 or n2:
            if n1 and n2 and n1.val == n2.val:
                t1 = n1.next
                t2 = n2.next
                head, tail = self.append(head, tail, n1)
                head, tail = self.append(head, tail, n2)
                n1 = t1
                n2 = t2
            elif (n1 and not n2) or (n1 and n2 and n1.val < n2.val):
                t1 = n1.next
                head, tail = self.append(head, tail, n1)
                n1 = t1
            else:
                t2 = n2.next
                head, tail = self.append(head, tail, n2)
                n2 = t2
        return head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists:
            return reduce(self.merge, lists)
        else:
            return []
