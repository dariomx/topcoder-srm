class Solution:
    def revList(self, head, k, rev=False):
        prev = None
        node = head
        size = 0
        while node and size < k:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            size += 1
        if size < k and not rev:
            return self.revList(prev, k, True)
        else:
            return prev, head, size, node

    def reverseKGroup(self, head, k):
        if not head:
            return None
        node = head
        new_head = None
        prev_g_tail = None
        while True:
            g_head, g_tail, g_size, g_next = self.revList(node, k)
            if not new_head:
                new_head = g_head
            if prev_g_tail:
                prev_g_tail.next = g_head
            g_tail.next = g_next
            prev_g_tail = g_tail
            if not g_next or g_size < k:
                break
            node = g_next
        return new_head

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
k = 3

node = Solution().reverseKGroup(head, k)
while node:
    print(node.val)
    node = node.next

