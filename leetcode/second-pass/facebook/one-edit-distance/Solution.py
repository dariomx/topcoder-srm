class Solution:
    def isOneEditDistance(self, s, t):
        if len(s) < len(t):
            s, t = t, s
        j = 0
        edit = 0
        for i in range(len(s)):
            if j == len(t) or s[i] != t[j]:
                if edit == 0:
                    edit = 1
                    j += 1 - (len(s) - len(t))
                else:
                    return False
            else:
                j += 1
        return (edit==1)