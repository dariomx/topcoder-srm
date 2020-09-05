from math import inf


class Solution:
    def countStr(self, s, k):
        s_cnt = [0] * k
        for c in s:
            i = ord(c) - ord('a')
            s_cnt[i] += 1
        return s_cnt

    def commonChars(self, A: List[str], k=26) -> List[str]:
        in_all = [True] * k
        cnt = [inf] * k
        for s in A:
            s_cnt = self.countStr(s, k)
            for i in range(k):
                in_all[i] = in_all[i] and (s_cnt[i] > 0)
                cnt[i] = min(cnt[i], s_cnt[i])
        ans = []
        for i in range(k):
            if not in_all[i]:
                continue
            for _ in range(cnt[i]):
                ans.append(chr(ord('a') + i))
        return ans