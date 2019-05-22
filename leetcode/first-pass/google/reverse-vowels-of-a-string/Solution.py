class Solution:
    def reverseVowels(self, s):
        is_vowel = lambda c: c.lower() in ('a','e','i','o', 'u')
        vs = [c for c in s if is_vowel(c)]
        ans = ""
        i = 0
        for c in s:
            if is_vowel(c):
                i += 1
                ans += vs[-i]
            else:
                ans += c
        return ans