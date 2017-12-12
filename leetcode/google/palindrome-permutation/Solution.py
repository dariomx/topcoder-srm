from collections import defaultdict


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = defaultdict(lambda: 0)
        for c in s:
            cnt[c] += 1
        odd = 0
        for k in cnt.itervalues():
            if k % 2 == 1:
                odd += 1
        return odd in (0, 1)
