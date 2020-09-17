class Solution:
    def removeVowels(self, S: str) -> str:
        ans = ''
        for c in S:
            if c in "aeiou":
                continue
            ans += c
        return ans
