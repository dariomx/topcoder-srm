class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        f0, f1 = 0, 1
        for _ in range(2, N + 1):
            tmp = f1
            f1 = f1 + f0
            f0 = tmp
        return f1
