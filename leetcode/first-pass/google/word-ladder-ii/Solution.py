"""
Did not really got it myself 100%. After having dealt with a quick
way of computing and caching the neighbors, I struggled in how to
extend BFS to compute all shortest paths and not just one.

Looked for a while for an academic source for the standard algorithm
for such problem: point-to-point all shorted paths for unweighted graph. But
no banana, last resource was to combine the following sources:

1) bitec answer for

https://stackoverflow.com/questions/14144071/finding-all-the-shortest-paths
-between-two-nodes-in-unweighted-undirected-graph

available here: https://ideone.com/2IUfcd

2) Miguel Oliveira answer for

https://www.quora.com/Can-I-get-all-the-shortest-paths-from-source-node-to
-destination-in-graph-using-bfs

"""

from collections import deque, defaultdict
from sys import maxsize as maxint


class Solution:
    def neighbors(self, word):
        if word in self.neicache:
            return self.neicache[word]
        nei = []
        for i in range(len(word)):
            prefix = word[:i]
            suffix = word[i + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                w = prefix + c + suffix
                if w != word and w in self.words:
                    nei.append(w)
        self.neicache[word] = nei
        return nei

    def bfs(self, beginWord):
        queue = deque([beginWord])
        parents = defaultdict(lambda: [])
        dist = defaultdict(lambda: maxint)
        dist[beginWord] = 0
        while queue:
            word = queue.popleft()
            if word == self.endWord:
                return parents
            for w in self.neighbors(word):
                if dist[word] + 1 < dist[w]:
                    dist[w] = dist[word] + 1
                    parents[w] = [word]
                    queue.append(w)
                elif dist[word] + 1 == dist[w]:
                    parents[w].append(word)
        return None

    def dfs(self, parents):
        paths = []
        stack = [(self.endWord, [self.endWord])]
        while stack:
            word, p = stack.pop()
            if word == self.beginWord:
                paths.append(p)
            else:
                for w in parents[word]:
                    stack.append((w, [w] + p))
        return paths

    def findLadders(self, beginWord, endWord, wordList):
        if len(beginWord) == 1:
            return [[beginWord, endWord]]
        self.beginWord = beginWord
        self.endWord = endWord
        self.words = set(wordList)
        self.neicache = dict()
        self.neicache[beginWord] = self.neighbors(beginWord)
        paths = []
        parents = self.bfs(beginWord)
        if parents:
            paths = self.dfs(parents)
        return paths