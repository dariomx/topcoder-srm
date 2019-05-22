from math import copysign

class Solution:
    def reverse(self, x):
        x = int(copysign(int(str(abs(x))[::-1]), x))
        if -(1<<31) <= x <= (1<<31)-1:
            return x
        else:
            return 0