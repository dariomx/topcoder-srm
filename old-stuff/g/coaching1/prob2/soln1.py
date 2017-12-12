import sys
import random

class RandomSet:
    # standard index functions in a 0-based heap
    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    # self.size is logical size, physical size is len(self.arr)
    # note we also need to pass the key function (which extracts
    # the key from objects, used for == and < operators).
    def __init__(self, maxsize, key, minkey, biggerKey):
        self.arr = [None] * maxsize
        self.size = 0
        self.key = key
        self.minkey = minkey
        self.biggerKey = biggerKey
        random.seed()

    # increase key is internal usage (auxiliary for insert/delete)
    def _increaseKey(self, i, k):
        assert k > self.arr[i][0]
        self.arr[i][0] = k
        p = self.parent(i)
        while i > 0 and self.arr[p][0] < self.arr[i][0]:
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p
            p = self.parent(i)

    # as the key function could be kinda expensive, we trade space for
    # time by caching its result: saved in fst element of tuple, snd
    # is the actual object (in reality we use 2-lists cause tuples do
    # not support assignment). note that here is where we could need to
    # invoke the worst case O(n) of built-in list's append (when the
    # given maxsize on constructor was not good enough).
    #
    # also, since this a set-like structure, we ignore the insertion if
    # the element already exists (this is another O(log(n)) operation, but
    # overall insertion remains as O(log(n)) [assuming we dont resize]
    def insert(self, x):
        k = self.key(x)
        if self._binSearch(0, k) < 0:
            self.size += 1
            if self.size > len(self.arr):
                self.arr.append(None)
            i = self.size - 1
            self.arr[i] = [self.minkey, x]
            self._increaseKey(i, self.key(x))

    # (bin)search receives the key already, as is mostly an internal
    # auxiliary function for delete. root stands for the index
    # of the root (potentially a subtree), where we want to start
    # searching. it returns -1 if not found.
    def _binSearch(self, root, k):
        i = root
        while i < self.size:
            if self.arr[i][0] == k:
                return i
            elif self.arr[i] < k:
                i = self.right(i)
            else:
                i = self.left(i)
        return -1

    # heapify is auxiliary of extractMax, it ensures that max-heap property
    # self.arr[self.parent(i)] >= self.arr[i] for all i
    def _heapify(self, root):
        i = root
        while True:
            l = self.left(i)
            r = self.right(i)
            if l < self.size and self.arr[l] > self.arr[i]:
                maxi = l
            else:
                maxi = i
            if r < self.size and self.arr[r] > self.arr[maxi]:
                maxi = r
            if maxi != i:
                self.arr[i], self.arr[maxi] = self.arr[maxi], self.arr[i]
                i = maxi
            else:
                break

    # extractMax is auxiliary of delete
    def _extractMax(self):
        maxx = self.arr[0][1]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1
        self._heapify(0)
        return maxx

    # by increasing key to something bigger than root, we will basically
    # make our element x the new root (allowing to use extractMax)
    # even if in theory this is still O(log(n)), in practice this may
    # be the slowest operation: we are doing 3 things inside that take
    # each O(log(n))
    def delete(self, x):
        k = self.key(x)
        i = self._binSearch(0, k)
        if i >= 0:
            kmax = self.arr[0][0]
            self._increaseKey(i, self.biggerKey(kmax))
            self._extractMax()

    def getRandomElement(self):
        if self.size > 0:
            i = random.randint(0, self.size-1)
            return self.arr[i]
        else:
            return None

# test
from random import randint
n = 10
m = 100
rnds = RandomSet(n, lambda x: x, -sys.maxint, lambda x: x+1)
for _ in xrange(m):
    op = randint(0, 2)
    x = randint(0, n-1)
    print("op = %d, x = %d" % (op,x))
    print("before: %d, %s" % (rnds.size, str(rnds.arr)))
    if op == 0:
        rnds.insert(x)
    elif op == 1:
        rnds.delete(x)
    else:
        print(rnds.getRandomElement())
    print("after: %d, %s" % (rnds.size, str(rnds.arr)))


