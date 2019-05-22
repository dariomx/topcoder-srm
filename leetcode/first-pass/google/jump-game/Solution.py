class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        def isReachable(i):
            for j in range(i-1, -1, -1):
                if nums[j] >= i-j:
                    return True
            return False
        for i in range(len(nums)-1):
            if nums[i] == 0 and not isReachable(i+1):
                return False
        return True
