class Solution:
    def makeGood(self, s: str) -> str:
        rm = len(s)
        while rm > 0:
            rm = 0
            newS = ''
            n = len(s)
            i = 0
            while i < n:
                if i < n - 1 and \
                    s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    i += 2
                    rm += 1
                else:
                    newS += s[i]
                    i += 1
            s = newS
            newS = ''
        return s