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
        self.maxLevel = max(1, int(log(maxSize, 2)))
        self.head = Node(NegInfinity(),
                         next=[NIL] * self.maxLevel,
                         dist=[1] * self.maxLevel)
        self.size = 0
        self.path = [None] * self.maxLevel
        self.levelDist = [0] * self.maxLevel

    def _search(self, value):
        pos = 0
        node = self.head
        for i in xrange(self.maxLevel-1, -1, -1):
            levelDist = 0
            while node.next[i].value < value:
                levelDist += node.dist[i]
                pos += node.dist[i]
                node = node.next[i]
            self.path[i] = node
            self.levelDist[i] = levelDist
        node = node.next[0]
        return (node,pos) if node.value == value else (None,pos)

    def insertAndGetPos(self, value):
        node, pos = self._search(value)
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
        return pos

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


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        list = IndexedSkipList(n)
        cnt = [0] * n
        for i in xrange(n-1, -1, -1):
            cnt[i] = list.insertAndGetPos(nums[i])
        return cnt

lst = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
print(Solution().countSmaller(lst) == [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0])