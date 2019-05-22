"""
Canonical merge algorithm in Python3 (compute_next + insert)

Not much to say here other than standard merge algorithm for two sorted lists
(though I confess tending to forget that is not needed to handle the
remainder list within single loop).

Perhaps the only special thing here is that I decided to make it a bit more
modular, by distinguishing the computation of the next node to insert vs the
insertion itself.

Time is O(n), with O(1) storage.
"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        node1 = l1
        node2 = l2
        prev = None
        l3 = None
        def insert(node):
            nonlocal prev, l3
            if not node:
                return
            if prev:
                prev.next = node
                prev = node
            else:
                prev = node
                l3 = prev
        def compute_next():
            nonlocal node1, node2
            if node1.val <= node2.val:
                next = node1
                node1 = node1.next
            else:
                next = node2
                node2 = node2.next
            return next
        # main
        while node1 and node2:
            insert(compute_next())
        insert(node1)
        insert(node2)
        return l3
