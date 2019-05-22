class Solution:
    def matrixReshape(self, nums, r, c):
        n, m = len(nums), len(nums[0])
        if n * m == r * c:
            ans = [[]]
            for i in range(n):
                for j in range(m):
                    ans[-1].append(nums[i][j])
                    if len(ans[-1]) == c and len(ans) < r:
                        ans.append([])
            return ans
        else:
            return nums
