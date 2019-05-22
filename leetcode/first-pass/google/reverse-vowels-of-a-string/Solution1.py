# based on discussion phorum

class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        start, end = 0, len(s) - 1
        s = list(s)
        while start < end:
            p, q = s[start] in vowels, s[end] in vowels
            if p and q:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            if not p:
                start += 1
            if not q:
                end -= 1
        return "".join(s)
