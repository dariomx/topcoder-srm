class Solution:
    def size(self, hd):
        cnt = 0
        node = hd
        while node:
            cnt += 1
            node = node.next
        return cnt

    def prepend(self, prev, x):
        node = ListNode(x)
        node.next = prev
        return node

    def revCarry(self, hd, base=10):
        rem = 0
        node = hd
        prev = None
        while node:
            node.val += rem
            rem = node.val // base
            node.val %= base
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        if rem > 0:
            prev = self.prepend(prev, rem)
        return prev

    def addTwoNumbers(self, l1, l2):
        n1 = self.size(l1)
        n2 = self.size(l2)
        if n1 < n2:
            n1, n2 = n2, n1
            l1, l2 = l2, l1
        prev = None
        node1 = l1
        node2 = l2
        for _ in range(n1 - n2):
            prev = self.prepend(prev, node1.val)
            node1 = node1.next
        for _ in range(n2):
            prev = self.prepend(prev, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
        return self.revCarry(prev)

