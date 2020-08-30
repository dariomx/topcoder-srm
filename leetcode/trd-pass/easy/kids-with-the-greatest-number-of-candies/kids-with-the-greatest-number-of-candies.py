class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC = max(candies)
        return [x + extraCandies >= maxC for x in candies]
