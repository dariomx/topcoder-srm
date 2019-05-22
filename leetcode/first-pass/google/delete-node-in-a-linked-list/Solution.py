# fail, a simpler O(1) soln is possible; one doest not
# need to shift entire list; just a few nodes.

class Solution:
    def deleteNode(self, node):
        prev = node
        curr = node.next
        while True:
            prev.val = curr.val
            if curr.next is None:
                prev.next = None
                break
            else:
                prev = curr
                curr = curr.next

