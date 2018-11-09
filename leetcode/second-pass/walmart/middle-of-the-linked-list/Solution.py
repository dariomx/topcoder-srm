class Solution:
    def middleNode(self, head):
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        node = head
        for i in range(n//2):
            node = node.next
        return node