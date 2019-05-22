class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lt_head = ListNode(None)
        lt_tail = lt_head
        ge_head = ListNode(None)
        ge_tail = ge_head
        node = head
        while node:
            if node.val < x:
                lt_tail.next = node
                lt_tail = node
            else:
                ge_tail.next = node
                ge_tail = node
            tmp = node.next
            node.next = None
            node = tmp
        lt_tail.next = ge_head.next
        return lt_head.next
