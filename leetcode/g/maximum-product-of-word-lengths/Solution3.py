class Solution(object):
    def encode(self, word):
        enc = 0
        for c in word:
            enc |= 1 << (ord(c) - ord('a'))
        return enc

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = dict()
        for w in words:
            codes[w] = self.encode(w)
        n = len(words)
        max_prod = 0
        for i in xrange(n):
            for j in xrange(i, n):
                if (codes[words[i]] & codes[words[j]]) == 0:
                    max_prod = max(max_prod, \
                                   len(words[i]) * len(words[j]))
        return max_prod
