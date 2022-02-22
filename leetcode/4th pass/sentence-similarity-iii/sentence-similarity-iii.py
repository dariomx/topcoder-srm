class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        n, m = len(s1), len(s2)
        if n < m:
            s1, s2 = s2, s1
            n, m = m, n
            
        @cache
        def rec(i, j, prev_eq, gaps):
            if gaps > 1:
                return False
            elif i == n:
                return j == m
            elif j == m:
                return i == n or gaps == 0
            elif prev_eq:
                if s1[i] == s2[j]:
                    return rec(i+1, j+1, True, gaps) or rec(i+1, j, False, gaps+1)
                else:
                    return rec(i+1, j, False, gaps+1)
            else:
                if s1[i] == s2[j]:
                    return rec(i+1, j+1, True, gaps) or rec(i+1, j, False, gaps)
                else:
                    return rec(i+1, j, False, gaps)
            
        return rec(0, 0, True, 0)
