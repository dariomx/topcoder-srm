import sys
from itertools import izip

class MinHeap:
    def __init__(self, maxsize):
        self.arr = [None] * maxsize
        self.size = 0

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def search(self, x):
        for i in xrange(self.size):
            if self.arr[i][1] == x:
                return i
        return -1

    def decreaseKey(self, x, k):
        i = self.search(x)
        assert 0 <= i < self.size and k == sys.maxint or k < self.arr[i][0]
        self.arr[i][0] = k
        p = self.parent(i)
        while i > 0 and self.arr[p][0] > self.arr[i][0]:
            self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p
            p = self.parent(i)

    def insert(self, x, k):
        self.size += 1
        if self.size > len(self.arr):
            self.arr.append(None)
        i = self.size - 1
        self.arr[i] = [sys.maxint, x]
        self.decreaseKey(x, k)

    def _heapify(self, root):
        i = root
        while True:
            l = self.left(i)
            r = self.right(i)
            if l < self.size and self.arr[l][0] < self.arr[i][0]:
                mini = l
            else:
                mini = i
            if r < self.size and self.arr[r][0] < self.arr[mini][0]:
                mini = r
            if mini != i:
                self.arr[i], self.arr[mini] = self.arr[mini], self.arr[i]
                i = mini
            else:
                break

    # extractMax is auxiliary of delete
    def extractMin(self):
        minx = self.arr[0][1]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1
        self._heapify(0)
        return minx

    def __contains__(self, x):
        return self.search(x) >= 0

    def __len__(self):
        return self.size

class Solution(object):
    def getBuildings(self, grid):
        bs = []
        n, m = len(grid), len(grid[0])
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    bs.append((i,j))
        return bs

    def getNeighbors(self, x, y, grid, heap=None):
        n, m = len(grid), len(grid[0])
        for i,j in [(x-1,y), (x+1,y), (x,y+1), (x,y-1)]:
            goodIndexes = 0 <= i < n and 0 <= j < m
            heapCond = not heap or (i,j) in heap
            if goodIndexes and grid[i][j] != 2 and heapCond:
                yield i, j

    def solveSingleBuilding(self, b, grid):
        for x,y in self.getNeighbors(b[0], b[1], grid):
            if grid[x][y] == 0:
                return 1
        return -1

    def getPath(self, start, end, prev):
        path = []
        node = end
        while node != start:
            path.append(prev[node])
            node = prev[node]
        path.pop()
        return reversed(path)

    def getPathSet(self, start, end, grid):
        pathSet = set()
        prev = dict()
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            x, y = node
            visited.add(node)
            if node == end:
                pathSet |= set(self.getPath(start, end, prev))
            elif node == start or grid[x][y] == 0:
                for n in self.getNeighbors(x, y, grid):
                    stack.append(n)
                    if n not in prev:
                        prev[n] = node
        return pathSet

    def getTotalPathSet(self, bs, grid):
        totalPath = self.getPathSet(bs[0], bs[1], grid)
        for i in xrange(2, len(bs)):
            totalPath &= self.getPathSet(bs[i-1], bs[i], grid)
        return totalPath

    def getTotalDistFrom(self, start, grid):
        dist = dict()
        n, m = len(grid), len(grid[0])
        heap = MinHeap(n * m)
        for i in xrange(n):
            for j in xrange(m):
                if (i,j) != start:
                    dist[(i,j)] = sys.maxint
                    heap.insert((i,j), dist[(i,j)])
        dist[start] = 0
        heap.insert(start, dist[start])
        visited = set()
        while len(heap) > 0:
            x, y = heap.extractMin()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if grid[x][y] == 0:
                for n in self.getNeighbors(x, y, grid, heap):
                    if dist[(x,y)] + 1 < dist[n]:
                        dist[n] = dist[(x,y)] + 1
                        heap.decreaseKey(n, dist[n])
        totalDist = 0
        for (x,y) in dist:
            if grid[x][y] == 1:
                totalDist += dist[(x,y)]
        return totalDist

    def shortestDistance(self, grid):
        bs = self.getBuildings(grid)
        if len(bs) == 1:
            return self.solveSingleBuilding(bs[0], grid)
        else:
            cands = self.getTotalPathSet(bs, grid)
            if not cands:
                return -1
            else:
                minDist = sys.maxint
                for c in cands:
                    minDist = min(minDist, self.getTotalDistFrom(c, grid))
                return minDist

grid = [
    [1, 0, 2, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]
]
print(Solution().shortestDistance(grid))
