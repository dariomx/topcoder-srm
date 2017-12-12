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
        s_cnt = self.s2cnt(s[:k])
        prev_ok = (s_cnt == p_cnt)
        if prev_ok:
            idx.append(0)
        for i in xrange(k, n):
            left = s[i - k]
            right = s[i]
            s_cnt[left] -= 1
            if s_cnt[left] == 0:
                del s_cnt[left]
            s_cnt[right] += 1
            if prev_ok:
                prev_ok = (left == right)
            else:
                prev_ok = (s_cnt == p_cnt)
            if prev_ok:
                idx.append(i - k + 1)
        return idx
