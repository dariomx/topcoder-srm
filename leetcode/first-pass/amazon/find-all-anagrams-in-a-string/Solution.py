from collections import defaultdict


class Solution(object):
    def s2cnt(self, s):
        cnt = defaultdict(lambda: 0)
        for c in s:
            cnt[c] += 1
        return cnt

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        k = len(p)
        p_cnt = self.s2cnt(p)
        idx = []
        for i in xrange(n):
            if self.s2cnt(s[i:i + k]) == p_cnt:
                idx.append(i)
        return idx
