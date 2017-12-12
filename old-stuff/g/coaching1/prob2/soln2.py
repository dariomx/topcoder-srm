from random import random, randint
from math import log

class Node:
    def __init__(self, value, maxLevel=None, next=None, dist=None):
        assert (value is not None)
        self.value = value
        if maxLevel:
            level = self._getRandomLevel(maxLevel)
            self.next = [None] * level
            self.dist = [0] * level
        else:
            self.next = next
            self.dist = dist

    def _getRandomLevel(self, maxLevel):
        level = 1
        while random() < 0.5 and level < maxLevel:
            level += 1
        return level

    def getLevel(self):
        return len(self.next)

    def __str__(self):
        return "(%s, %s, %s)" % (self.value, self.next, self.dist)

class NegInfinity:
    def __cmp__(self, other):
        return -1

    def __str__(self):
        return "-inf"

class PosInfinity:
    def __cmp__(self, other):
        return 1

    def __str__(self):
        return "+inf"

NIL = Node(PosInfinity(), 0)

class IndexedSkipList:
    def __init__(self, maxSize):
        self.maxLevel = int(log(maxSize, 2))
        self.head = Node(NegInfinity(),
                         next=[NIL] * self.maxLevel,
                         dist=[1] * self.maxLevel)
        self.size = 0
        self.path = [None] * self.maxLevel
        self.levelDist = [0] * self.maxLevel

    def _search(self, value):
        node = self.head
        for i in xrange(self.maxLevel-1, -1, -1):
            levelDist = 0
            while node.next[i].value < value:
                levelDist += node.dist[i]
                node = node.next[i]
            self.path[i] = node
            self.levelDist[i] = levelDist
        node = node.next[0]
        return node if node.value == value else None

    def insert(self, value):
        if self._search(value):
            return
        newNode = Node(value, maxLevel=self.maxLevel)
        currDist = 0
        for i in xrange(newNode.getLevel()):
            prev = self.path[i]
            newNode.next[i] = prev.next[i]
            prev.next[i] = newNode
            newNode.dist[i] = prev.dist[i] - currDist
            prev.dist[i] = currDist + 1
            currDist += self.levelDist[i]
        for i in xrange(newNode.getLevel(), self.maxLevel):
            self.path[i].dist[i] += 1
        self.size += 1

    def delete(self, value):
        node = self._search(value)
        if not node:
            return
        for i in xrange(node.getLevel()):
            prev = self.path[i]
            prev.dist[i] += prev.next[i].dist[i] - 1
            prev.next[i] = prev.next[i].next[i]
        for i in xrange(node.getLevel(), self.maxLevel):
            self.path[i].dist[i] -= 1
        self.size -= 1

    def __getitem__(self, k):
        assert (0 <= k < self.size)
        k += 1
        pos = 0
        node = self.head
        for i in xrange(self.maxLevel-1, -1, -1):
            while pos + node.dist[i] <= k:
                pos += node.dist[i]
                node = node.next[i]
        return node.value

    def __len__(self):
        return self.size

    def __str__(self):
        s = ""
        for i in xrange(self.maxLevel-1, -1, -1):
            node = self.head
            s += "\n"
            while node != NIL:
                s += "(%s->%d)[%d], " % \
                     (str(node.value), node.dist[i], node.getLevel())
                node = node.next[i]
        return s

class RandomSet:
    def __init__(self, maxSize=1000000):
        self.skipList = IndexedSkipList(maxSize)

    def insert(self, value):
        self.skipList.insert(value)

    def delete(self, value):
        self.skipList.delete(value)

    def getRandomElem(self):
        if len(self.skipList) > 0:
            k = randint(0, len(self.skipList)-1)
            return self.skipList[k]
        else:
            return None

    def __str__(self):
        return str(self.skipList)

    def __len__(self):
        return len(self.skipList)

# test
n = 10
m = 100
rnds = RandomSet(n)
for _ in xrange(m):
    op = randint(0, 2)
    x = randint(0, n-1)
    print("op = %d, x = %d" % (op,x))
    print("before %d: %s" % (len(rnds), str(rnds)))
    if op == 0:
        rnds.insert(x)
    elif op == 1:
        rnds.delete(x)
    else:
        print(rnds.getRandomElem())
    print("after %d: %s" % (len(rnds), str(rnds)))
