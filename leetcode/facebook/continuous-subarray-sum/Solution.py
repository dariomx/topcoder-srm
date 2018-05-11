class Solution:
    def checkSubarraySum(self, nums, k):
        m = len(nums)
        k = abs(k)
        s = sum(nums)
        if k == 0:
            return (s == 0 and m >= 2)
        if s == 0 and m >= 2:
            return True
        if s < k:
            for i in range(m - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        n = sum(nums) // k
        while n > 0:
            i, j = 0, 0
            s = nums[0]
            nk = n * k
            while True:
                if s < nk:
                    if j < m - 1:
                        j += 1
                        s += nums[j]
                    else:
                        break
                elif s > nk:
                    if i < j:
                        s -= nums[i]
                        i += 1
                    else:
                        break
                else:
                    if j - i + 1 >= 2:
                        return True
                    elif j < m - 1:
                        j += 1
                        s += nums[j]
                    else:
                        break
            n -= 1
        return False

