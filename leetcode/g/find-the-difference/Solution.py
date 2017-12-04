from collections import defaultdict


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_cnt = defaultdict(lambda: 0)
        for c in s:
            s_cnt[c] += 1
        for c in t:
            if c in s_cnt:
                s_cnt[c] -= 1
                if s_cnt[c] == 0:
                    del s_cnt[c]
            else:
                return c
