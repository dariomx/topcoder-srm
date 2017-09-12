class PatternChar:
    def __init__(self, c):
        self.c = c
        self.has_star = False


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

    def compilePath(self, pat):
        cpath = []
        for c in pat:
            if c == '*':
                cpath[-1].has_star = True
            else:
                cpath.append(PatternChar(c))
        return cpath

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        p = self.compilePath(self.normalizePat(p))
        m = len(p)

        def isMatchRec(i, j):
            ret = False
            if i == n and j == m:
                ret = True
            elif (i == n and j < m) or (i < n and j == m):
                None
            elif p[j].has_star:
                for k in xrange(i, n + 1):
                    if isMatchRec(k, j + 1):
                        ret = True
                        break
            elif p[j].c == '.' or s[i] == p[j].c:
                ret = isMatchRec(i + 1, j + 1)
            return ret

        return isMatchRec(0, 0)
