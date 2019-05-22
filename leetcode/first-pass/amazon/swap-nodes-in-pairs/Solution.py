class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = head
        node = head.next
        new_head = node
        while node:
            tmp = node.next
            node.next = prev
            if tmp and tmp.next:
                prev.next = tmp.next
            else:
                prev.next = tmp
            prev = tmp
            node = tmp
            if node:
                node = node.next
        return new_head