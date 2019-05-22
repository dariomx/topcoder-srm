class Solution:
    def subSum(self, nums, start, end):
        sum = 0
        for i in range(start, end + 1):
            sum += nums[i]
        return sum

    def calcLeftMax(self, nums, n, k):
        leftMax = [(0, None)] * n
        sum = self.subSum(nums, 0, k - 1)
        leftMax[k - 1] = sum, 0
        for i in range(k, n - 2 * k):
            sum += nums[i] - nums[i - k]
            if sum > leftMax[i - 1][0]:
                leftMax[i] = sum, i - k + 1
            else:
                leftMax[i] = leftMax[i - 1]
        return leftMax

    def calcRightMax(self, nums, n, k):
        rightMax = [(0, None)] * n
        sum = self.subSum(nums, n - k, n - 1)
        rightMax[n - k] = sum, n - k
        for i in range(n - k - 1, k - 1, -1):
            sum += nums[i] - nums[i + k]
            if sum > rightMax[i + 1][0]:
                rightMax[i] = sum, i
            else:
                rightMax[i] = rightMax[i + 1]
        return rightMax

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        leftMax = self.calcLeftMax(nums, n, k)
        rightMax = self.calcRightMax(nums, n, k)
        maxSum = 0
        maxIdx = []
        sum = self.subSum(nums, k, 2 * k - 1)
        for i in range(k, n - k):
            sum += nums[i + k - 1] - nums[i - 1]
            leftSum, leftIdx = leftMax[i - 1]
            rightSum, rightIdx = rightMax[i + k]
            totalSum = leftSum + sum + rightSum
            if totalSum > maxSum:
                maxSum = totalSum
                maxIdx = [leftIdx, i, rightIdx]
        return maxIdx
