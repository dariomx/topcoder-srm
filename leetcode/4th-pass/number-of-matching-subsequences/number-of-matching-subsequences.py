class Solution:
    @cache
    def is_subseq(self, w: str, s: str) -> True:
        i, j = 0, 0
        while i < len(w) and j < len(s):
            if w[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(w)
            
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return sum(self.is_subseq(w, s) for w in words)
