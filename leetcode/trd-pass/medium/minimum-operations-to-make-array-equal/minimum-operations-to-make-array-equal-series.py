class Solution:
    def minOperations(self, n: int) -> int:
        return sum(n - (2*i + 1) for i in range(floor((n-1)/2) + 1))
