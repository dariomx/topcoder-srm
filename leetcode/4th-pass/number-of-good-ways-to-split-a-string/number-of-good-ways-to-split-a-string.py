class Solution:
    def numSplits(self, s: str) -> int:
        left_cnt = defaultdict(lambda: 0)
        right_cnt = Counter(s)
        ans = 0
        
        for x in s:
            left_cnt[x] += 1
            right_cnt[x] -= 1
            if right_cnt[x] == 0:
                del right_cnt[x]
            if len(left_cnt) == len(right_cnt):
                ans += 1
                
        return ans
