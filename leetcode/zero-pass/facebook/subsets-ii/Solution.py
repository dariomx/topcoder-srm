class Solution(object):
    def subsetsWithDup(self, nums):
        n = len(nums)
        def rec(i):
            ans = []
            if i == n:
                ans.append([])
            else:
                x = nums[i]
                for ss in rec(i+1):
                    ans.append(ss)
                    ans.append([x] + ss)
            return ans
        norm = lambda ss: tuple(sorted(ss))
        return list(set(map(norm, rec(0))))