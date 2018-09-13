from collections import Counter

class Solution:
    def containsDuplicate(self, nums):
        return len(Counter(nums)) < len(nums)