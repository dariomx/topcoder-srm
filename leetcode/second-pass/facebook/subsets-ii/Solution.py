class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        ans = set()

        def rec(i, ss):
            if i == n:
                ans.add(tuple(sorted(ss)))
            else:
                ss.append(nums[i])
                rec(i + 1, ss)
                ss.pop()
                rec(i + 1, ss)

        rec(0, [])
        return list(ans)

