class Solution:
    def sortColors(self, nums):
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        i, j = 0, 1
        k = n
        while j < k:
            x, y = nums[i], nums[j]
            if x != 2 and y != 2:
                if x > y:
                    swap(i, j)
                j += 1
                if not (x == 1 and y == 1):
                    i += 1
            elif x == 2 and y in (0, 1):
                k -= 1
                swap(i, k)
            elif x in (0, 1) and y == 2:
                k -= 1
                swap(j, k)
            elif x == 2 and y == 2:
                k -= 1
                swap(i, k)
                k -= 1
                swap(j, k)
