class Solution(object):
    def can_break(self, s, wdict, cache):
        if s in cache:
            return cache[s]
        else:
            can = False
            for i in xrange(len(s)):
                if s[:i + 1] in wdict and self.can_break(s[i + 1:], wdict, cache):
                    can = True
                    break
            cache[s] = can
            return can

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        cache = dict()
        cache[''] = True
        return self.can_break(s, wordDict, cache)