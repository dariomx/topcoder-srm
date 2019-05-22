from collections import deque


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)
        if r != 0:
            return False
        nums.sort(reverse=True)
        buck = [0] * k
        n = len(nums)

        def rec(i):
            if i == n:
                for x in buck:
                    if x != q:
                        return False
                return True
            else:
                x = nums[i]
                for j in range(k):
                    if x + buck[j] > q:
                        continue
                    buck[j] += x
                    if rec(i + 1):
                        return True
                    buck[j] -= x
                return False

        return rec(0)
