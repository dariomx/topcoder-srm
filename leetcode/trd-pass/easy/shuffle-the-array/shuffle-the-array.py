class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] |= nums[i+n] << 16
        j = -1
        for i in reversed(range(n)):
            nums[j] = nums[i] >> 16
            nums[j-1] = nums[i] & 0x0000ffff
            j -= 2
        return nums