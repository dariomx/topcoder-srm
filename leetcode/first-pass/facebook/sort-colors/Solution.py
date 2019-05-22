class Solution:
    def sortColors(self, nums):
        n = len(nums)
        zero_i = 0
        two_i = n - 1

        def ins(i):
            nonlocal zero_i, two_i
            if nums[i] == 0:
                nums[zero_i] = 0
                if zero_i != i:
                    nums[i] = 1
                zero_i += 1
            elif nums[i] == 2:
                while zero_i < two_i:
                    if two_i != i and nums[two_i] == 2:
                        two_i -= 1
                    else:
                        if nums[two_i] == 0:
                            ins(two_i)
                        break
                nums[two_i] = 2
                if i not in (two_i, zero_i - 1):
                    nums[i] = 1
                two_i -= 1

        for i in range(n):
            if zero_i == two_i or i > two_i:
                return
            ins(i)

