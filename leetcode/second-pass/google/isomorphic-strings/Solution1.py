class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t = dict()
        t2s = dict()
        for (cs, ct) in zip(s, t):
            if cs in s2t:
                if s2t[cs] != ct:
                    return False
            elif ct in t2s:
                if t2s[ct] != cs:
                    return False
            else:
                s2t[cs] = ct
                t2s[ct] = cs
        return True

