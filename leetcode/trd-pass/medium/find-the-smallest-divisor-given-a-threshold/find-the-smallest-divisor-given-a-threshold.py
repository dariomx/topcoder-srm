class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        start, end = 1, max(nums)
        while start <= end:
            middle = (start + end) // 2
            if sum(ceil(x/middle) for x in nums) <= threshold:
                if start == end:
                    break
                else:
                    end = middle
            else:
                start = middle + 1
        return middle