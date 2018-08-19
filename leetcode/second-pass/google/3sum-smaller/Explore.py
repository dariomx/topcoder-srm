# failed attempt to make it O(n^2)

from math import factorial as fact

class Solution:
    def binSearch(self, nums, iStart, iEnd, base, target):
        start = iStart
        end = iEnd
        while start <= end:
            mid = (start + end) // 2
            if mid - 1 >= iStart:
                cur = nums[mid] + base
                prev = nums[mid - 1] + base
                if prev < target and cur >= target:
                    return mid - 1
                elif prev < target and cur < target:
                    start = mid + 1
                else:
                    end = mid - 1
            elif end - start + 1 == 2 and \
                                            nums[start] + nums[
                                        end] + 2 * base < target:
                return end
            else:
                break
        if mid == iEnd:
            return iEnd
        else:
            return -1

    def comb(self, n, m):
        if n >= m:
            return fact(n) // (fact(n-m) * fact(m))
        else:
            return 0

    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            k = self.binSearch(nums, i + 1, n - 1, nums[i], target)
            if k < 0:
                continue
            while k+1 < n and nums[k+1] == 0:
                k += 1
            print((i, k))
            j = k-1
            while j > i and nums[i] + nums[j] + nums[k] >= target:
                j -= 1
            if k == i:
                continue
            print((i, j, k))
            ans += (j - i) * (k - j) + self.comb(j-i+1, 3)
        return ans

#nums = [-2, 1, 1]
#nums = [-2,0,1,3]
#print(Solution().binSearch(nums, 1, len(nums) - 1, -2, 1))
#nums = [-2, 0, 1, 3]
nums = [-1, -1, 0, 1]
#nums = [-1, -1, -1, 1]

print(Solution().threeSumSmaller(nums, -1))
