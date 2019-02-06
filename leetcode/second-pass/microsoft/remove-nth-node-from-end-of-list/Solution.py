class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        node = head
        for _ in range(n-1):
            node = node.next
        prev_n = None
        while node.next:
            node = node.next
            prev_n = prev_n.next if prev_n else head
        if prev_n:
            prev_n.next = prev_n.next.next
        else:
            head = head.next
        return head