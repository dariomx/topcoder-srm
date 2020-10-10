class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def score(self):
        return self.prev.val * self.val * self.next.val

    def __lt__(self, other):
        return self.score() < other.score()


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

    def getMaxHeap(self):
        heap = []
        node = self.head
        while node != self.tsent:
            heap.append(node)
            node = node.next
        heapify(heap)
        return heap


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dl = DList(DNode(1), DNode(1), nums)
        heap = dl.getMaxHeap()
        ans = 0
        while heap:
            node = heappop(heap)
            ans += node.score()
            dl.remove(node)
        return ans
