from random import randint

class Solution:
    def __init__(self, nums: List[int]):
        self.orig = list(nums)
        self.shuf = list(nums)

    def reset(self) -> List[int]:
        return self.orig

    def shuffle(self) -> List[int]:
        n = len(self.shuf)
        A = self.shuf
        for i in range(n):
            j = randint(0, n-1)
            A[i], A[j] = A[j], A[i]
        return A

