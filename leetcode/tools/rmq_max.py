"""
Based on first method of

https://en.wikipedia.org/wiki/Range_minimum_query

(just adjusted to be max instead of min).

Which come from first two paragraphs of section 2.3 in below article:

https://www3.cs.stonybrook.edu/~bender/pub/JALG05-daglca.pdf

though the article seems to have a typo on the recurrence relation
that the Wikipedia author, thankfully, fixed.

Given definition of (inclusive slicing, to avoid confusion):

dp[i, j] = min(A[i : i + 2^j - 1])

Original article wrote:
dp[i, j] = min(dp[i, j-1], dp[i+2^(j-1)-1, j-1])

which in terms of array means:
min(A[i : i + 2^j - 1]) = min(A[i : i + 2^(j-1) - 1],
                              A[i + 2^(j-1) - 1 : i + 2^(j-1) - 1 + 2^(j-1) - 1])
                        = min(A[i : i + 2^(j-1) - 1],
                              A[i + 2^(j-1) - 1 : i + 2^j - 2])

You can see that the right sub-interval is shifted one place to the left,
overlapping with the left sub-interval and missing to cover last position.

Wikipedia author wrote instead:
dp[i, j] = min(dp[i, j-1], dp[i+2^(j-1), j-1])

which in terms of array means:
min(A[i : i + 2^j - 1]) = min(A[i : i + 2^(j-1) - 1],
                              A[i + 2^(j-1) : i + 2^(j-1) + 2^(j-1) - 1])
                        = min(A[i : i + 2^(j-1) - 1],
                              A[i + 2^(j-1) : i + 2^j - 1])

which kinda makes more sense now; the last two sub-arrays really partition
the original now:

A[i : i + 2^j - 1] = A[i : i + 2^(j-1) - 1] +  A[i + 2^(j-1) : i + 2^j - 1]

though we are kinda overwriting original idea about 'overlapping' ranges, mmm,
not sure if this fine.

Anyway, we map indexes internally to keep original convention of starting at 1,
and we also bring convention of preferring left-most maximum; just to make it
easier to unit test with index (which returns left-most occurrence).
"""

class RMQ:
    def __init__(self, nums):
        n = len(nums)
        k = self._log2(n)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = i
        for j in range(1, k+1):
            for i in range(1, n+1):
                p2i = i + (1 << (j - 1))
                if not (1 <= p2i <= n):
                    dp[i][j] = dp[i][j-1]
                elif nums[dp[i][j-1]-1] >= nums[dp[p2i][j-1]-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[p2i][j-1]
        self.nums = nums
        self.rmq = dp

    def _log2(self, n):
        return n.bit_length() - 1

    def find_max(self, i, j):
        i += 1
        j += 1
        k = self._log2(j - i + 1)
        max_ix_left = self.rmq[i][k]
        p2i = j - (1 << k) + 1
        if not (1 <= p2i <= len(self.nums)):
            return max_ix_left - 1
        max_ix_right = self.rmq[p2i][k]
        max_ix_left -= 1
        max_ix_right -= 1
        if self.nums[max_ix_left] >= self.nums[max_ix_right]:
            return max_ix_left
        else:
            return max_ix_right
