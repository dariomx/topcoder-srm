from collections import defaultdict
from math import inf


class WordDistance:
    def __init__(self, words: 'List[str]'):
        self.index = defaultdict(lambda: [])
        for i in range(len(words)):
            self.index[words[i]].append(i)
        self.cache = dict()

    def shortest(self, word1: 'str', word2: 'str') -> 'int':
        if (word1, word2) in self.cache:
            return self.cache[(word1, word2)]
        l1, l2 = self.index[word1], self.index[word2]
        i1, i2 = 0, 0
        ans = inf
        while i1 < len(l1) or i2 < len(l2):
            if i1 < len(l1) and i2 < len(l2):
                last1, last2 = l1[i1], l2[i2]
                if last1 < last2:
                    i1 += 1
                else:
                    i2 += 1
            elif i1 < len(l1):
                last1 = l1[i1]
                i1 += 1
            else:
                last2 = l2[i2]
                i2 += 1
            ans = min(ans, abs(last1 - last2))
        self.cache[(word1, word2)] = ans
        self.cache[(word2, word1)] = ans
        return ans
