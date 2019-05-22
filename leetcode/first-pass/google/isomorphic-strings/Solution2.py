class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t = [None] * 256
        t2s = [None] * 256
        for (cs, ct) in zip(s, t):
            cs, ct = ord(cs), ord(ct)
            if s2t[cs]:
                if s2t[cs] != ct:
                    return False
            elif t2s[ct]:
                if t2s[ct] != cs:
                    return False
            else:
                s2t[cs] = ct
                t2s[ct] = cs
        return True

