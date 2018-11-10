from math import inf


class Solution:
    def shortestDistance(self, words, word1, word2):
        last1, last2 = inf, inf
        n = len(words)
        ans = inf
        for i in range(n):
            w = words[i]
            if w == word1:
                ans = min(ans, abs(i - last2))
                last1 = i
            elif w == word2:
                ans = min(ans, abs(i - last1))
                last2 = i
        return ans


