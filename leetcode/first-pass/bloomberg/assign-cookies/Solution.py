class Solution:
    def findContentChildren(self, g, s):
        ans = 0
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans