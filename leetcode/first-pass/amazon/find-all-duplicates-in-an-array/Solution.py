# putting aside items already in place, we can think of the
# rest of items as belonging to disjoint cycles; but if they
# contain duplicates, the cycle would get broken.
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(1, n+1):
            if nums[i-1] == i:
                continue
            j, nums[i-1] = nums[i-1], 0
            while j > 0:
                if j == nums[j-1]:
                    ans.append(j)
                    break
                else:
                    tmp = nums[j-1]
                    nums[j-1] = j
                    j = tmp
        return ans
