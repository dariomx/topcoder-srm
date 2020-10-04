"""
I really discarded divide and conquer for this problem, until I gave up and
saw the phorum solutions. Then decided to spice its iterative flavor with:

a) O(1) count-char-in-range query structure (so we avoid counting every
substring).
b) Sentinels in loops (to avoid last special step)
c) max-heap instead of stack to abort when we can not improve further
   current answer (sorting key will be sub-string size)

So here it is ... I have failed in life but at least I did this.
"""


class CountRange:
    def __init__(self, s):
        n = len(s)
        cnt = [[0] * (n + 1) for _ in range(26)]
        for x in set(s):
            ix = ord(x) - ord('a')
            for j, y in enumerate(s):
                cnt[ix][j] = cnt[ix][j - 1] + int(x == y)
        self.cnt = cnt
        self.s = s

    def query(self, x, i, j):
        if i > j:
            return 0
        else:
            ix = ord(x) - ord('a')
            return self.cnt[ix][j] - self.cnt[ix][i] + int(x == self.s[i])


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = CountRange(s)
        heap = [(-len(s), 0, len(s) - 1)]
        ans = 0
        while heap and -heap[0][0] > ans:
            _, start, end = heappop(heap)
            i, bad = start, 0
            for j in range(start, end + 2):
                if (j > end or cnt.query(s[j], start, end) < k):
                    if i <= j - 1 and cnt.query(s[j - 1], start, end) >= k:
                        heappush(heap, (i - j, i, j - 1))
                    bad += int(j <= end)
                    i = j + 1
            if bad == 0:
                ans = max(ans, end - start + 1)
        return ans

