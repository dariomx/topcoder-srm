class Solution:
    def rev(self, head, size):
        prev = None
        node = head
        for _ in range(size):
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev, node

    def reverseBetween(self, head, m, n):
        prev_m = None
        node_m = head
        for _ in range(m - 1):
            prev_m = node_m
            node_m = node_m.next
        node_n, next_n = self.rev(node_m, n - m + 1)
        if prev_m:
            prev_m.next = node_n
        else:
            head = node_n
        node_m.next = next_n
        return head
