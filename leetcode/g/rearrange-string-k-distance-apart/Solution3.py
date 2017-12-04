from collections import defaultdict


class Solution(object):
    def search_perm(self, perm, k, chars, cache):
        canon = perm
        if canon in cache:
            return None
        win = perm[-k:]
        win_set = set(win)
        if len(win) != len(win_set):
            cache.add(canon)
            return None
        if chars:
            if len(win) == k:
                win_set.remove(win[0])
            for c in set(chars.keys()) - win_set:
                chars[c] -= 1
                if chars[c] == 0:
                    del chars[c]
                soln = self.search_perm(perm + c, k, chars, cache)
                if soln is not None:
                    return soln
                chars[c] += 1
            cache.add(canon)
            return None
        else:
            return perm

    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        chars = defaultdict(lambda: 0)
        for c in s:
            chars[c] += 1
        soln = self.search_perm('', k, chars, set())
        return '' if soln is None else soln
