from collections import Counter


class Solution:
    def uncommonFromSentences(self, A, B):
        cntA = Counter(A.split())
        cntB = Counter(B.split())
        A = cntA.keys()
        B = cntB.keys()
        ans = [x for x in A - B if cntA[x] == 1]
        ans += [x for x in B - A if cntB[x] == 1]
        return ans



