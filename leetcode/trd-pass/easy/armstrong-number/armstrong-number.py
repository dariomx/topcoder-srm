class Solution:
    def isArmstrong(self, N: int) -> bool:
        N = str(N)
        k = len(N)
        return sum(d**k for d in map(int, N)) == int(N)
