class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cntS = Counter(s)
        cntT = Counter(t)
        return sum(max(0, k - cntT.get(x, 0)) for x, k in cntS.items())

