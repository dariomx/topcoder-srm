class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        rec = [0] * n
        rec[n-1] = 1
        cnt = dict()
        cnt[n-1] = 1
        max_len = 1
        max_cnt = 1
        for i in range(n-2, -1, -1):
            rec[i] = 1
            cnt[i] = 1
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    diff = (1 + rec[j]) - rec[i]
                    if diff == 0:
                        cnt[i] += cnt[j]
                    elif diff > 0:
                        cnt[i] = cnt[j]
                        rec[i] = 1 + rec[j]
            if rec[i] > max_len:
                max_len = rec[i]
                max_cnt = cnt[i]
            elif rec[i] == max_len:
                max_cnt += cnt[i]
        return max_cnt
