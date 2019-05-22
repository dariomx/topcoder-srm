class Solution:
    def size(self, hd):
        n = 0
        node = hd
        while node:
            n += 1
            node = node.next
        return n

    def split(self, hd, n):
        half = n // 2 + n % 2
        node = hd
        for _ in range(half - 1):
            node = node.next
        snd = node.next
        node.next = None
        return hd, snd

    def rev(self, hd):
        prev = None
        node = hd
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev

    def append(self, tail, node):
        node.next = None
        if tail:
            tail.next = node
        return node

    def reorderList(self, hd):
        n = self.size(hd)
        if n <= 2:
            return
        fst, snd = self.split(hd, n)
        snd = self.rev(snd)
        node = None
        while snd:
            tmp1 = fst.next
            tmp2 = snd.next
            node = self.append(node, fst)
            node = self.append(node, snd)
            fst = tmp1
            snd = tmp2
        if fst:
            self.append(node, fst)
