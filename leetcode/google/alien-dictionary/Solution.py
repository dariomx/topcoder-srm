class Solution(object):
    def calc_alien_cmp(self, words):
        n = len(words)
        max_len = max(map(len, words))
        cmp = dict()
        for k in xrange(1, max_len + 1):
            for j in xrange(n - 1, 0, -1):
                w1 = words[j - 1]
                w2 = words[j]
                if len(w1) >= k and len(w2) >= k:
                    i = k - 1
                    cmp[(w1[i], w2[i])] = -1
                    cmp[(w2[i], w1[i])] = +1
        return lambda x, y: 0 if x == y else cmp[(x, y)]

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        alien_cmp = self.calc_alien_cmp(words)
        chars = set()
        for w in words:
            chars = chars.union(set(w))
        chars = list(chars)
        try:
            chars.sort(cmp=alien_cmp)
            return ''.join(chars)
        except:
            raise
            return ''


words = ["wrt", "wrf", "er", "ett", "rftt"]
print(Solution().alienOrder(words))
