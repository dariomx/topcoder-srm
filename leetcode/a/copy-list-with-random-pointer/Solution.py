# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        new_nodes = dict()
        old = head
        while old:
            new = RandomListNode(old.label)
            new_nodes[old] = new
            old = old.next
        for old, new in new_nodes.iteritems():
            new.next = new_nodes.get(old.next, None)
            new.random = new_nodes.get(old.random, None)
        return new_nodes.get(head, None)
