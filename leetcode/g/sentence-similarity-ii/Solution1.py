"""
While the previous DFS approach works, it can potentially traverse long
sections of the graph without a real need. In order to improve further,
we can leverage the previously ignored properties of the similar relation: it
is an equivalence relation.

Equivalence relations bring a natural partition to the set, where in our
particular case each partition contains strings similar to each other. If we
model each partition as a disjoin-set, then we could optimize the
transitivity check: if two strings belong to same disjoint set, then they are
similar.

Knowing two strings belong to same disjoint-set, means retrieving the
representative for each one, and comparing those representatives. Retrieving
each representative, in a disjoint-set forests implementation, can be done in
O(log(n)). This should be better than the linear complexity from DFS.

The disjoint-set forest was taken from Cormen book.

NOTE: Despite theoretical advantages mentioned, this algorithm actually is
slower than the DFS one. Perhaps the paths to parent are too long (unbalanced
trees), or perhaps the path-compression is worth it only if you query more
times.

"""

from itertools import izip


class DisjointSet:
    def __init__(self, val):
        self.p = self
        self.rank = 0


def make_set(x):
    return DisjointSet(x)


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p


class Solution(object):
    def create_forest(self, pairs):
        forest = dict()
        for x, y in pairs:
            if x not in forest:
                forest[x] = make_set(x)
            if y not in forest:
                forest[y] = make_set(y)
            union(forest[x], forest[y])
        return forest

    def are_similar(self, w1, w2, forest):
        # reflexivity
        if w1 == w2:
            return True
        # they can't be similar if one is not in forest
        elif w1 not in forest or w2 not in forest:
            return False
            # symmetry & transitivity
        elif find_set(forest[w1]) == find_set(forest[w2]):
            return True
        else:
            return False

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        forest = self.create_forest(pairs)
        for w1, w2 in izip(words1, words2):
            if not self.are_similar(w1, w2, forest):
                return False
        return True
