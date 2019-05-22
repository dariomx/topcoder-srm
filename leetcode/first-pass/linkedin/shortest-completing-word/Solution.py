from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        ans = None
        licensePlate = licensePlate.lower()
        for w in words:
            cnt = Counter(w)
            cand = True
            for c in licensePlate:
                if not c.isalpha():
                    continue
                if cnt[c] == 0:
                    cand = False
                    break
                else:
                    cnt[c] -= 1
            if cand and (not ans or len(w) < len(ans)):
                ans = w
        return ans

