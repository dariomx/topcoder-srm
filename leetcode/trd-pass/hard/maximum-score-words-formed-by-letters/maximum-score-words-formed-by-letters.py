class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def getScore(i):
            return sum(score[ord(c) - ord('a')] * k for c, k in wcnt[i].items())
        def valid(wc):
            return all(cnt.get(c, 0) >= k for (c, k) in wc.items())
        def discount(wc):
            for c, k in wc.items():
                cnt[c] -= k
        def count(wc):
            for c, k in wc.items():
                cnt[c] += k
        def rec(i, totScore):
            nonlocal ans
            if i == n:
                ans = max(ans, totScore)
            else:
                wc = wcnt[i]
                if valid(wc):
                    discount(wc)
                    rec(i+1, totScore + wscore[i])
                    count(wc)
                rec(i+1, totScore)
        n = len(words)
        cnt = Counter(letters)
        wcnt = [Counter(w) for w in words]
        wscore = [getScore(i) for i in range(n)]
        ans = -inf
        rec(0, 0)
        return ans

