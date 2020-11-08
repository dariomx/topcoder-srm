from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        def rec(A):
            if len(A) == 1:
                return A
            ans = [0] * len(A)
            m = len(A) // 2
            n = m + len(A) % 2
            for i in range(n):
                ans[2*i] = A[i]
            B = rec(A[n:])
            if n > m:
                B = B[-1:] + B[:-1]
            for i in range(m):
                ans[2*i + 1] = B[i]
            return ans
        deck.sort()
        return rec(deck)

# main
deck = [17,13,11,2,3,5,7]
# deck = [1,2,3,4,5]
print(Solution().deckRevealedIncreasing(deck))
