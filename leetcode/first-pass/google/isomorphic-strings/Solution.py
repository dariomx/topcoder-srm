class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s2t = dict()
        for (cs, ct) in zip(s, t):
            if cs in s2t:
                if s2t[cs] != ct:
                    return False
            else:
                s2t[cs] = ct
        return len(set(s2t.values())) == len(s2t.keys())

