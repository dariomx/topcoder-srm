class Set:
    def __init__(self):
        self.parent = self
        self.rank = 0


class Forest:
    def __init__(self):
        self.num_roots = 0

    def make_set(self):
        self.num_roots += 1
        return Set()

    def find(self, x):
        if x != x.parent:
            x.parent = self.find(x.parent)
        return x.parent

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        elif root_x.rank < root_y.rank:
            root_x.parent = root_y
        elif root_x.rank > root_y.rank:
            root_y.parent = root_x
        else:
            root_y.parent = root_x
            root_x.rank += 1
        self.num_roots -= 1


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        sets = dict()
        forest = Forest()
        num_islands = []
        for (x, y) in positions:
            sets[(x, y)] = forest.make_set()
            for (i, j) in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= i < m and 0 <= j < n and (i, j) in sets:
                    set_xy = forest.find(sets[(x, y)])
                    set_ij = forest.find(sets[(i, j)])
                    forest.union(set_xy, set_ij)
            num_islands.append(forest.num_roots)
        return num_islands

