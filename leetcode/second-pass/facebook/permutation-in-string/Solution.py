from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        cnt2 = defaultdict(lambda: 0)
        start = 0
        for end in range(len(s2)):
            c = s2[end]
            if c in cnt1:
                cnt2[c] += 1
                win_size = end - start + 1
                if win_size > len(s1) or cnt2[c] > cnt1[c]:
                    cnt2[s2[start]] -= 1
                    start += 1
                    win_size -= 1
                if win_size == len(s1) and cnt1 == cnt2:
                    return True
            else:
                cnt2 = defaultdict(lambda: 0)
                start = end + 1
        return False
