from collections import defaultdict


class Solution(object):
    def anagramMappings(self, A, B):
        ixB = defaultdict(lambda: [])
        for i, b in enumerate(B):
            ixB[b].append(i)
        ans = []
        for a in A:
            ans.append(ixB[a].pop())
        return ans
