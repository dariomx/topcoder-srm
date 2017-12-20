"""
The trick is to move the biggest list at a time, or both if they have same size.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodeA = headA
        sizeA = 0
        while nodeA:
            nodeA = nodeA.next
            sizeA += 1
        nodeB = headB
        sizeB = 0
        while nodeB:
            nodeB = nodeB.next
            sizeB += 1
        nodeA = headA
        nodeB = headB
        while nodeA and nodeB and nodeA != nodeB:
            if sizeA == sizeB:
                nodeA = nodeA.next
                sizeA -= 1
                nodeB = nodeB.next
                sizeB -= 1
            elif sizeA > sizeB:
                nodeA = nodeA.next
                sizeA -= 1
            else:
                nodeB = nodeB.next
                sizeB -= 1
        return None if nodeA != nodeB else nodeA