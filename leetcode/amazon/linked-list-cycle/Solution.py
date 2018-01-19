"""
Python solution with O(n) time and O(1) space

I confess having heard about this problem before, but with a different skin (the
setting I knew involved robots running on a ring). The solution is to have a
couple of pointers, moving forward at different speeds (second pointer moving
two places at a time).

With different speed rates, if there is a cycle, it will happen that the second
pointer passes the first one.
"""

class Solution(object):
    def hasCycle(self, head):
        node1 = head
        node2 = head
        if node2:
            node2 = node2.next
        while node1 and node2:
            node1 = node1.next
            node2 = node2.next
            if node2 and node2 == node1:
                return True
            if node2:
                node2 = node2.next
                if node2 and node2 == node1:
                    return True
        return False