class Solution:
    def removeElements(self, head, val):
        node = head
        prev = None
        while node:
            if node.val == val:
                if node.next:
                    node.val = node.next.val
                    node.next = node.next.next
                elif prev:
                    prev.next = None
                    break
                else:
                    head = None
                    break
            else:
                prev = node
                node = node.next
        return head

