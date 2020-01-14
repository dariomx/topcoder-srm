"""
Python3 recursive solution with prefix sums

This one had a history with me. I initially tried 6 months ago, and could not
come up with something interesting (my best solution the timed out). But
recently I came across this recursive solution, combined with a prefix sum
technique.

The main idea is that we pay attention to the biggest, and second biggest
heights on the array. Between those walls, we can compute the water capacity
as follows:

1. Compute the surrounding rectangular area (using minimum height from
extremes). This area contains both water and concrete spots.

2. Discount the sum of the interior heights, as that space will be filled with
concrete.

For the 2nd part is that we used the prefix technique (inspired by
another problem). The idea is to compute the prefix sum for all indexes (a
prefix sum for i-th position is the sum(height[:i+1]), and then to use them
for obtaining the sum of any arbitrary sub-array of heights in constant time.

The last piece is recursion: once we have done the computation for the
greatest and second greatest heights, we call recursively to get the water
from the left and right sub-arrays (including the edges of the section we
just computed, because they still have chances to pair with others). Finally,
we just add up the three quantities and return final result.

I think that worst cases may still be O(n^2), because of the computation
of the greatest and second greatest elements given a sub-array. But on average
this smells like O(n*log(n)); because the sizes of sub-arrays may tend to
rapidly decrease, as we go deeper in recursion.
"""

class Solution(object):
    def trap(self, height):
        n = len(height)
        psum = dict()
        if n > 0:
            psum[0] = height[0]
        for i in range(1, n):
            psum[i] = psum[i - 1] + height[i]
        range_sum = lambda i, j: psum[j] - psum[i] + height[i]

        def next_pair(i, j):
            if j - i <= 1:
                return None
            if height[i] < height[i + 1]:
                max1 = i + 1
                max2 = i
            else:
                max1 = i
                max2 = i + 1
            for k in range(i + 2, j + 1):
                if height[k] > height[max1]:
                    max2 = max1
                    max1 = k
                elif height[k] > height[max2]:
                    max2 = k
            return tuple(sorted((max1, max2)))

        def rec(start, end):
            p = next_pair(start, end)
            if p is None:
                return 0
            i, j = p
            base = j - i - 1
            water = 0
            if base > 0:
                min_h = min(height[i], height[j])
                area = base * min_h
                water = area - range_sum(i + 1, j - 1)
            water += rec(start, i) + rec(j, end)
            return water

        return rec(0, n - 1)
