class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        head_odd = ListNode(None)
        last_odd = head_odd
        head_even = ListNode(None)
        last_even = head_even
        i = 1
        node = head
        while node:
            if i % 2 == 1:
                last_odd.next = node
                last_odd = node
            else:
                last_even.next = node
                last_even = node
            tmp = node.next
            node.next = None
            node = tmp
            i += 1
        last_odd.next = head_even.next
        return head_odd.next
