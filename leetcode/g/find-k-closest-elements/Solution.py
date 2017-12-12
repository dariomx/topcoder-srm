"""
The main idea is to locate a center first; and then iteratively grow this
center to become the expected sub-array.

This center is the closest element in the array to x. This can be found
efficiently with binary search, given that the array is already sorted.

Once we have a center, we initialize a couple of indexes i and j, to be equal
to this center; so far we can think we have computed one element of the answer.

Then, for the remaining k-1 elements, we explore the left and right edges; that
is, the elements at arr[i-1] and arr[j+1]. According to the rules, we pick the
closest one to x; if there is a tie we pick the smallest. If we reach the
scenario of hitting left or right edges of array, then we simply add next
element from the opposite direction.

Time complexity: O(log(n) + k), where log(n) is the cost of finding the closest
element, and O(k) is the cost of growing our center to a sub-array of size k.
"""

from bisect import bisect_left


class Solution(object):
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        i = bisect_left(arr, x)
        if i - 1 >= 0 and arr[i] != x:
            i -= 1
        j = i
        for _ in xrange(k - 1):
            if i - 1 >= 0 and j + 1 < n:
                diff = abs(x - arr[i - 1]) - abs(x - arr[j + 1])
                if diff < 0:
                    i -= 1
                elif diff == 0:
                    if arr[i - 1] < arr[j + 1]:
                        i -= 1
                    else:
                        j += 1
                else:
                    j += 1
            elif i - 1 >= 0:
                i -= 1
            elif j + 1 < n:
                j += 1
        return arr[i:j + 1]
