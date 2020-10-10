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
        self.key = []
        self.keyIx = dict()
        for val in values:
            node = self.add(val)
            self.keyIx[node] = len(self.key)
            self.key.append(node.val)

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
        self.key[self.keyIx[node]] = None

    def backupNode(self, node):
        return node, self.head, self.tail

    def restoreNode(self, backup):
        node, head, tail = backup
        node.prev.next = node
        node.next.prev = node
        self.head = head
        self.tail = tail
        self.key[self.keyIx[node]] = node.val

    def isEmpty(self):
        return self.head is None

    def toList(self):
        lst = []
        node = self.head
        while node and node != self.tsent:
            lst.append(node.val)
            node = node.next
        return lst

    def getKey(self):
        return tuple(self.key)


class Solution:
    def search(self, dl, score):
        key = (dl.getKey(), score)
        if key in self.cache:
            return self.cache[key]
        if dl.isEmpty():
            ret = score
        else:
            node = dl.head
            ret = -inf
            while node != dl.tsent:
                backup = dl.backupNode(node)
                dl.remove(node)
                ret = max(ret, self.search(dl, score + node.score()))
                dl.restoreNode(backup)
                node = node.next
        self.cache[key] = ret
        return ret

    def maxCoins(self, nums: List[int]) -> int:
        dl = DList(DNode(1), DNode(1), nums)
        self.cache = dict()
        return self.search(dl, 0)
