"""
Python3 solution using constrained BFS

This problem can be seen as a graph problem: the nodes represent the words,
and the edges are created only for those words at distance = 1 (where
distance here is computed as the number of different positions between
the words).

As I see it, there are two parts of this problem:

a) Ensuring the paths we find are the shortest

b) Ensuring that we compute the adjacency list in less than O(n^2)

The first part can be done using BFS, as that guarantees shortest paths for
undirected graphs like this. But the second part was a bit hard to guess,
but finally realized that we can do the following:

1) Save all words in a set for O(1) existence queries

2) Pre-compute all possible characters among words per position (all have same
size, per problem description)

3) For a given word, iterate over its k positions
      For each position, iterate over its possible characters:
          Form a new word by replacing character at current position
          Test if word does exist, and it it does then we found an edge

The adjacency list was built in lazy-mode, just when we reached the word
behind the node.

I think worst-case complexity would be O(n * k * m), where

n = number of words
k = size of words
m = maximum number of chars observed among all words x positions

"""


from collections import deque
from sys import maxsize as maxint


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        words = set(wordList)
        k = len(beginWord)
        chars = [set() for _ in range(k)]
        for w in words:
            for i in range(k):
                chars[i].add(w[i])

        def neighbors(word):
            for j in range(k):
                for c in chars[j]:
                    w = word[:j] + c + word[j + 1:]
                    if w in words and w != word:
                        yield w

        def search_bfs(start):
            min_dist = maxint
            queue = deque([(start, 1)])
            visited = set([start])
            while queue:
                word, d = queue.popleft()
                if word == endWord:
                    min_dist = min(min_dist, d)
                elif d < min_dist:
                    for w in neighbors(word):
                        if w not in visited:
                            visited.add(w)
                            queue.append((w, d + 1))
            return min_dist

        min_dist = search_bfs(beginWord)
        return 0 if min_dist == maxint else min_dist
