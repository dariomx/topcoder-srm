from collections import defaultdict, Counter

class Solution:
    def isMatch(self, s, p):
        new_p = ""
        for i in range(len(p)):
            if not (p[i] == '*' and new_p and new_p[-1] == '*'):
                new_p += p[i]
        p = new_p
        m = len(p)
        n = len(s)
        slots = dict()
        cnt = 0
        for i in range(m-1, -1, -1):
            if p[i] == '*':
                slots[i] = cnt
            else:
                cnt += 1
        if n < cnt:
            return False
        cache = dict()
        def rec(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            ret = False
            if i==n and j==m:
                ret = True
            elif (i==n and j<m):
                if j == m-1 and p[j] == '*':
                    ret = True
                else:
                    ret = False
            elif (i<n and j==m):
                ret = False
            elif s[i] == p[j] or p[j] == '?':
                ret = rec(i+1, j+1)
            elif p[j] == '*':
                ret = False
                for k in range(i, n-slots[j]+1):
                    if rec(k, j+1):
                       ret = True
                       break
            cache[ret] = ret
            return ret
        return rec(0, 0)