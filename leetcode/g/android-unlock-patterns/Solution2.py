class Solution(object):
    def __init__(self):
        self.keys = [[0] * 3 for _ in xrange(3)]
        self.coords = dict()
        for i in xrange(3):
            for j in xrange(3):
                key = i * 3 + j + 1
                self.keys[i][j] = key
                self.coords[key] = (i, j)
        self.bridges = dict()
        self.bridges[5] = [(1, 9), (3, 7), (2, 8), (4, 6)]
        self.bridges[2] = [(1, 3)]
        self.bridges[4] = [(1, 7)]
        self.bridges[6] = [(3, 9)]
        self.bridges[8] = [(7, 9)]

    def getNeighbors(self, key, visited):
        x, y = self.coords[key]
        extras = set(range(1, 10))
        extras.remove(key)
        for i in xrange(x - 1, x + 2):
            for j in xrange(y - 1, y + 2):
                if (i, j) != (x, y) and 0 <= i < 3 and 0 <= j < 3:
                    extras.remove(self.keys[i][j])
                    yield self.keys[i][j]
        for k in self.bridges:
            for (k1, k2) in self.bridges[k]:
                if key == k1:
                    extras.remove(k2)
                    if k in visited:
                        yield k2
                elif key == k2:
                    extras.remove(k1)
                    if k in visited:
                        yield k1
        for k in extras:
            yield k

    def prunePath(self, path):
        pathSet = set()
        prunedPath = []
        for k in path:
            if k not in pathSet:
                prunedPath.append(k)
                pathSet.add(k)
        return prunedPath

    def addPaths(self, start, m, n, paths):
        stack = [(start, [start])]
        while stack:
            key, path = stack.pop()
            prunedPath = self.prunePath(path)
            if m <= len(prunedPath) <= n:
                paths.append(prunedPath)
            if len(prunedPath) < n:
                for k in self.getNeighbors(key, set(path)):
                    stack.append((k, path + [k]))
                    # print(map(lambda s: ''.join(map(str, s)), sorted(paths)))

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = []
        for start in xrange(1, 10):
            self.addPaths(start, m, n, paths)
        return len(paths)


print(Solution().numberOfPatterns(3, 8))
