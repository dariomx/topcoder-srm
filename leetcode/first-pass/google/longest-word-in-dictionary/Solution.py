class Solution:
    def longestWord(self, words):
        seen = set()
        ans = ""
        for w in sorted(words):
            cand = True
            for i in range(len(w)-1):
                if w[:i+1] not in seen:
                    cand = False
                    break
            if cand and len(w) > len(ans):
                ans = w
            seen.add(w)
        return ans