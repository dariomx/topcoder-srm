from sortedcontainers import SortedList


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        win = SortedList(nums[:k])
        half = k // 2

        def median():
            if k % 2 == 0:
                med = (win[half] + win[half - 1]) / 2
            else:
                med = win[half]
            return med

        ans = [median()]
        for i in range(k, len(nums)):
            win.discard(nums[i - k])
            win.add(nums[i])
            ans.append(median())
        return ans


