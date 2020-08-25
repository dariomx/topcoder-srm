class Solution:
    def confusingNumber(self, N: int) -> bool:
        rotDig = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        rotN = 0
        pow10 = 1
        for c in str(N):
            d = int(c)
            if d not in rotDig:
                return False
            rotN += pow10 * rotDig[d]
            pow10 *= 10
        return rotN != N
