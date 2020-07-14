from collections import Counter
from sortedcontainers import SortedKeyList


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        cnt = SortedKeyList(Counter(s).items(), key=lambda t: (-t[1], t[0]))
        last = defaultdict(lambda: -k)
        ans = ''
        while len(cnt) > 0:
            upd = []
            for _ in range(min(k, len(cnt))):
                sym, num = cnt.pop(0)
                if len(ans) - last[sym] < k:
                    return ''
                last[sym] = len(ans)
                ans += sym
                if num > 1:
                    upd.append((sym, num - 1))
            cnt.update(upd)
        return ans
