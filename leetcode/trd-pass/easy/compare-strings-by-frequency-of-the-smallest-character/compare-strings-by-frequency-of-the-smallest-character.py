from bisect import bisect_right


class Solution:
    def chr2idx(self, c):
        return ord(c) - ord('a')

    def freqSmallest(self, s):
        cnt = [0] * 26
        min_c = None
        for c in s:
            cnt[self.chr2idx(c)] += 1
            if min_c is None or c < min_c:
                min_c = c
        return cnt[self.chr2idx(min_c)]

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> \
    List[int]:
        fWords = [self.freqSmallest(w) for w in words]
        fWords.sort()
        n = len(words)
        ans = []
        for q in queries:
            idx = bisect_right(fWords, self.freqSmallest(q))
            ans.append(n - idx)
        return ans