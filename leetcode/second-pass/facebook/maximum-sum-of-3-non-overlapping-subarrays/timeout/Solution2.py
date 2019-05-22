class Solution:
    def calcPrefixSum(self, nums, n):
        pfxSum = [0] * n
        pfxSum[0] = nums[0]
        for i in range(1, n):
            pfxSum[i] = pfxSum[i - 1] + nums[i]
        return pfxSum

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        pfxSum = self.calcPrefixSum(nums, n)
        subSum = lambda i, j: pfxSum[j] - pfxSum[i] + nums[i]
        maxSum = dict()
        maxIdx = dict()

        def rec(i, p):
            if (i, p) in maxSum:
                return maxSum[(i, p)], maxIdx[(i, p)]
            sum = 0
            idx = []
            if n - i < p * k:
                sum = None
            elif p == 0:
                idx = []
            else:
                for j in range(i, n):
                    sum_j, idx_j = rec(j + k, p - 1)
                    if sum_j is None:
                        break
                    sum_j += subSum(j, j + k - 1)
                    if sum_j > sum:
                        sum = sum_j
                        idx = [j] + idx_j
                if sum == 0:
                    sum = None
            maxSum[(i, p)] = sum
            maxIdx[(i, p)] = idx
            return sum, idx

        # main
        sum, idx = rec(0, 3)
        return idx
