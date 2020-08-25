class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        idx = {k:i for (i, k) in enumerate(keyboard)}
        i = 0
        ans = 0
        for c in word:
            j = idx[c]
            ans += abs(i - j)
            i = j
        return ans