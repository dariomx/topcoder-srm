# tried with min-heap but sorting seems faster
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1, 2*n, 2))