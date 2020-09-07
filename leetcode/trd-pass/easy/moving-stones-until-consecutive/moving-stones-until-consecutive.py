class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        ba, cb = b - a, c - b
        if ba == 1 and cb == 1:
            return 0, 0
        elif 1 <= min(ba, cb) <= 2:
            return 1, max(ba, cb) - 2 + min(ba, cb)
        else:
            return 2, ba + cb - 2




