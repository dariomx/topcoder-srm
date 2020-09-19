class Solution:
    def countOdds(self, low: int, high: int) -> int:
        size = high - low + 1
        if size % 2 == 0:
            return size // 2
        else:
            return size // 2 + low % 2            