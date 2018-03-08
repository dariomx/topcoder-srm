"""
Python3 solution that beats them all ... churro!

I initially thought that this would be done by using an stable sorting
algorithm, but altering the values of cells such that zeros were always
bigger than anybody else. But I do not really recall any of those algorithms,
at least not those with O(1) space; most famous seems merge sort but the
implementations I found were scary.

Then I decided to go with expensive O(n^2) approach: going from left to
right, the non-zero item at position i-th needs to be swapped with the first
zero position of the cells already passed. This scheme times out in Python3,
but if we optimize a bit by remembering the last used position, it seems to
work fine (actually beats all existing solutions ... probably cause there are
not many submissions in this language ;-)

Suspiciously it looks a bit similar to the optimal solution on editorial, mm,
except that they lack a nested loop. But I suspect in practice that loop does a
few iterations perhaps?

"""

class Solution:
    def moveZeroes(self, nums):
        start = 0
        for i in range(len(nums)):
            x = nums[i]
            if x != 0:
                for j in range(start, i):
                    if nums[j] == 0:
                        nums[j], nums[i] = nums[i], nums[j]
                        start = j
                        break


