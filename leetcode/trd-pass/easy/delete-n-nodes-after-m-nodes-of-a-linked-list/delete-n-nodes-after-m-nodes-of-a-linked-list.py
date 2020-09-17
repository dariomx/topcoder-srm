class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        prev = None
        while node:
            for _ in range(m):
                if node is None:
                    break
                prev = node
                node = node.next
            for _ in range(n):
                if node is None:
                    break
                node = node.next
            prev.next = node
        return head