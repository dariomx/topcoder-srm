class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumd = 0
        for d in str(n):
            d = int(d)
            prod *= d
            sumd += d
        return prod - sumd