class Solution:
    def reverse(self, head, k):
        prev = None
        node = head
        size = 0
        while node and size < k:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            size += 1
        return prev, head, size, node

    def reverseKGroup(self, head, k):
        prev = None
        rest = head
        fst_head = None
        size = k
        while size == k:
            head, tail, size, rest = self.reverse(rest, k)
            if size < k:
                head, tail, size, rest = self.reverse(head, k)
            if fst_head is None:
                fst_head = head
            if prev:
                prev.next = head
            prev = tail
        return fst_head
