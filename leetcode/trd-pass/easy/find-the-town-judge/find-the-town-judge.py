from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        i_trust = defaultdict(lambda: 0)
        trust_me = defaultdict(lambda: 0)
        for x, y in trust:
            i_trust[x] += 1
            trust_me[y] += 1
        for x, k in trust_me.items():
            if k == N - 1 and i_trust[x] == 0:
                return x
        return -1