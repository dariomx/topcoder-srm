class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        sentinel = ListNode(None)
        sentinel.next = head
        prev_n = sentinel
        node = sentinel
        for _ in range(n):
            node = node.next
        while node.next:
            node = node.next
            prev_n = prev_n.next
        prev_n.next = prev_n.next.next
        return sentinel.next