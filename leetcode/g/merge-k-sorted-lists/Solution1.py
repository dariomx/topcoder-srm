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

    def get_tail(self, head):
        node = head
        while node and node.next:
            node = node.next
        return node

    def merge(self, l1, tail1, l2):
        n1 = l1
        n2 = l2
        head, tail = None, None
        if n1 and n2 and tail1.val <= l2.val:
            head = n1
            tail = tail1
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
        return head, tail

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists:
            lists.sort(key=lambda n: n.val if n else None)
            head, tail = lists[0], self.get_tail(lists[0])
            for lst in lists[1:]:
                head, tail = self.merge(head, tail, lst)
            return head
        else:
            return []
