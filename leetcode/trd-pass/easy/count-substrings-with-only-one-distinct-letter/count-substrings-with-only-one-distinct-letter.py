class Solution:
    def countLetters(self, S: str) -> int:
        ans = 0
        prev = None
        start = 0
        for end, c in chain(enumerate(S), [(len(S), None)]):
            if c != prev:
                size = end - start
                ans += size * (size + 1) // 2
                prev = c
                start = end
        return ans
