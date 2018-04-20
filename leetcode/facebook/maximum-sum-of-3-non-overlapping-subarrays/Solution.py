class Solution:
    def calcPrefixSum(self, nums, n):
        pfxSum = [0] * n
        pfxSum[0] = nums[0]
        for i in range(1, n):
            pfxSum[i] = pfxSum[i - 1] + nums[i]
        return pfxSum

    def calcLeftMax(self, n, k, subSum):
        leftMax = [(0, None)] * n
        leftMax[k - 1] = subSum(0, k - 1), 0
        for i in range(k, n - 2 * k):
            sum = subSum(i - k + 1, i)
            if sum > leftMax[i - 1][0]:
                leftMax[i] = sum, i - k + 1
            else:
                leftMax[i] = leftMax[i - 1]
        return leftMax

    def calcRightMax(self, n, k, subSum):
        rightMax = [(0, None)] * n
        rightMax[n - k] = subSum(n - k, n - 1), n - k
        for i in range(n - k - 1, k - 1, -1):
            sum = subSum(i, i + k - 1)
            if sum > rightMax[i + 1][0]:
                rightMax[i] = sum, i
            else:
                rightMax[i] = rightMax[i + 1]
        return rightMax

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        pfxSum = self.calcPrefixSum(nums, n)
        subSum = lambda i, j: pfxSum[j] - pfxSum[i] + nums[i]
        leftMax = self.calcLeftMax(n, k, subSum)
        rightMax = self.calcRightMax(n, k, subSum)
        maxSum = 0
        maxIdx = []
        for i in range(k, n - k):
            leftSum, leftIdx = leftMax[i - 1]
            rightSum, rightIdx = rightMax[i + k]
            sum = leftSum + subSum(i, i + k - 1) + rightSum
            if sum > maxSum:
                maxSum = sum
                maxIdx = [leftIdx, i, rightIdx]
        return maxIdx
