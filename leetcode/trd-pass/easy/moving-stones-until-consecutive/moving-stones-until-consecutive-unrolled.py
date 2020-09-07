class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted((a, b, c))
        ba, cb = b - a, c - b
        if ba == 1 and cb == 1:
            return 0, 0
        elif ba == 1 and cb > 1:
            return 1, cb - 1
        elif cb == 1 and ba > 1:
            return 1, ba - 1
        elif ba == 2 and cb > 1:
            return 1, cb
        elif cb == 2 and ba > 1:
            return 1, ba
        else:
            return 2, ba + cb - 2
