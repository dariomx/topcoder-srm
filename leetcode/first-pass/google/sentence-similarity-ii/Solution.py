"""
The description of the exercise gives us already a lot of hits, as they
describe the properties of the being-similar relation for words:

1. Reflexive
2. Symmetric
3. Transitive

Thus, the relation is pretty much an equivalence relation; though that may
not help us much for the exercise (or it might be, as the relation brings a
natural partition to the strings set; but we did not use that here).

The approach is simple: build a graph from the pairs, using a searchable
collection of children for each node (string); a set was good enough. Then
validate each property of the relation as an alternative for having similar
words.

The first two properties are directly validated from the words themselves,
or the children sets of the graph; and for the transitivity property we just
validate for reachability in the graph (using DFS, though BFS would serve too).

Last but not least, we just use the hint and validate upfront if the lenghts
of the words are same or not. In all functions indeed, we try to leave as
soon as possible when similarity is not achieved.

"""

from collections import defaultdict
from itertools import izip


class Solution(object):
    def create_graph(self, pairs):
        graph = defaultdict(lambda: set())
        for x, y in pairs:
            graph[x].add(y)
            graph[y].add(x)
        return graph

    def are_reachable(self, graph, x, y):
        stack = [x]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node == y:
                return True
            for child in graph[node]:
                stack.append(child)
        return False

    def are_similar(self, w1, w2, graph):
        if w1 == w2:  # reflexivity
            return True
        elif w1 in graph[w2] or w2 in graph[w1]:  # symmetry
            return True
        elif self.are_reachable(graph, w1, w2):  # transitivity
            return True
        else:
            return False

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        graph = self.create_graph(pairs)
        for w1, w2 in izip(words1, words2):
            if not self.are_similar(w1, w2, graph):
                return False
        return True
