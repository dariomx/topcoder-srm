class Solution(object):
    def normalizePat(self, pat):
        normPat = ""
        cnt = 0
        for c in pat:
            if c == '*':
                cnt += 1
                if cnt == 1:
                    normPat = normPat + c
            else:
                normPat = normPat + c
                cnt = 0
        return normPat

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        p = self.normalizePat(p)
        m = len(p)

        def isMatchRec(i, j):
            ret = None
            if i == n and j == m:
                ret = True
            elif i == n and j < m:
                ret = False
            elif i < n and j == m:
                ret = False
            else:
                if p[j] not in ['.', '*']:
                    if s[i] == p[j]:
                        ret = isMatchRec(i + 1, j + 1)
                    else:
                        ret = False
                elif p[j] == '.':
                    ret = isMatchRec(i + 1, j + 1)
                else:
                    ret = False
                    for k in xrange(i, n + 1):
                        if isMatchRec(k, j + 1):
                            ret = True
                            break
            return ret

        return isMatchRec(0, 0)


print(Solution().isMatch("aa", "a*"))
