from bisect import bisect_left


class Solution:
    def search_pivot(self, nums, start, end):
        while end - start + 1 >= 3:
            mid = (start + end) // 2
            print((start, end, mid))
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                mid_left = self.search_pivot(nums, start, mid)
                if mid_left is None:
                    return self.search_pivot(nums, mid, end)
                else:
                    return mid_left
            elif nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid] and nums[mid] < nums[mid + 1]:
                return mid - 1
        return None

    def search(self, nums, target):
        n = len(nums)
        if n < 3:
            i = n
            for j in range(n):
                if nums[j] == target:
                    i = j
                    break
        else:
            mid = self.search_pivot(nums, 0, n - 1)
            print(mid)
            if mid is None:
                i = bisect_left(nums, target)
            elif nums[0] <= target <= nums[mid]:
                i = bisect_left(nums, target, lo=0, hi=mid)
            else:
                i = bisect_left(nums, target, lo=mid + 1, hi=n - 1)
        return i if i != n and nums[i] == target else -1
