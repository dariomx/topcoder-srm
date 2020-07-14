# kinda cheated here, cause took the definition of series from https://oeis.org/A027868, cause i was having trouble seeing the whole pattern
class Solution:
    def trailingZeroes(self, n: int) -> int:
        def A027868(n):
            if n < 5:
                return 0
            else:
                return n//5 + A027868(n//5)
        return A027868(n)