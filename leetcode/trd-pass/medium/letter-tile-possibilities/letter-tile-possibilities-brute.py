from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        dp = [0] * (n+1)
        for s in range(1, n+1):
            dp[s] = len(set(permutations(tiles, s)))
        return sum(dp)

# main
tiles = "AAABBC"
print(Solution().numTilePossibilities(tiles))
