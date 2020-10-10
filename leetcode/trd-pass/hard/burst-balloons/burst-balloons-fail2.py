from typing import List

from math import inf


class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def score(self):
        return self.prev.val * self.val * self.next.val


class DList:
    def __init__(self, hsent, tsent, values=[]):
        self.hsent = hsent
        self.tsent = tsent
        self.head = None
        self.tail = None
        for val in values:
            self.add(val)

    def add(self, val):
        node = DNode(val)
        if self.head is None:
            node.prev = self.hsent
            self.head = node
            node.next = self.tsent
            self.tail = node
        else:
            node.prev = self.tail
            node.next = self.tsent
            self.tail.next = node
            self.tail = node
        return node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node == self.head:
            if node.next == self.tsent:
                self.head = None
            else:
                self.head = node.next
                self.head.prev = self.tsent
        if node == self.tail:
            if node.prev == self.hsent:
                self.tail = None
            else:
                self.tail = node.prev
                self.tail.next = self.tsent

    def backupNode(self, node):
        return node, self.head, self.tail

    def restoreNode(self, backup):
        node, head, tail = backup
        node.prev.next = node
        node.next.prev = node
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head is None

    def toList(self):
        lst = []
        node = self.head
        while node and node != self.tsent:
            lst.append(node.val)
            node = node.next
        return lst


class Solution:
    def search(self, dl, score):
        print(dl.toList())
        if dl.isEmpty():
            self.ans = max(self.ans, score)
        else:
            node = dl.head
            while node != dl.tsent:
                backup = dl.backupNode(node)
                dl.remove(node)
                self.search(dl, score + node.score())
                dl.restoreNode(backup)
                node = node.next

    def maxCoins(self, nums: List[int]) -> int:
        dl = DList(DNode(1), DNode(1), nums)
        self.ans = -inf
        self.search(dl, 0)
        return self.ans

# main
nums = [35,16,83,87,84,59,48,41,20,54]
print(Solution().maxCoins(nums))
