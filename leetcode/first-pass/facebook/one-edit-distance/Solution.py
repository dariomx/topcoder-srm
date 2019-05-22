class Solution:
    def isOneEditDistance(self, s, t):
        if len(s) < len(t):
            s, t = t, s
        n, m = len(s), len(t)
        def rec(i, j, edit):
            if i == n and j == m:
                ret = (edit==1)
            elif edit > 1:
                ret = False
            else:
                ret = False
                if i < n and j < m:
                    ret = ret or rec(i+1, j+1, edit + int(s[i] != t[j]))
                if i < n:
                    ret = ret or rec(i+1, j, edit+1)
                if j < m:
                    ret = ret or rec(i, j+1, edit+1)
            return ret
        return rec(0, 0, 0)
