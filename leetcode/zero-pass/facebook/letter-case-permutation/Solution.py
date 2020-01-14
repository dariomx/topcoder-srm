class Solution:
    def letterCasePermutation(self, S):
        perm = []
        n = len(S)

        def rec(i, s):
            if i == n:
                perm.append(s)
            else:
                if S[i].isalpha():
                    rec(i + 1, s + S[i].upper())
                    rec(i + 1, s + S[i].lower())
                else:
                    rec(i + 1, s + S[i])

        rec(0, '')
        return perm
