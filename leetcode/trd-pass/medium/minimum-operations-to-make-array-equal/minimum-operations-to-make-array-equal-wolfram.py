# https://leetcode.com/problems/minimum-operations-to-make-array-equal/discuss/919800/Python3%3A-detailed-O(1)-solution-derivation-with-different-approach-(mass-conservation)
class Solution:
    def minOperations(self, n: int) -> int:
        t = floor((n-1) / 2)
        return -(t + 1) * (t - n + 1)