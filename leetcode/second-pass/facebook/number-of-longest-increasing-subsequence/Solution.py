class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        max_size = 1
        max_cnt = 1
        size = [1] * n
        cnt = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    size_j = 1 + size[j]
                    if size_j > size[i]:
                        size[i] = size_j
                        cnt[i] = cnt[j]
                    elif size_j == size[i]:
                        cnt[i] += cnt[j]
            if size[i] > max_size:
                max_size = size[i]
                max_cnt = cnt[i]
            elif size[i] == max_size:
                max_cnt += cnt[i]
        return max_cnt
