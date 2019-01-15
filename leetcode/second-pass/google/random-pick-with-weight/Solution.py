from random import random
from bisect import bisect_left

class Solution:
    def __init__(self, w):
        S = sum(w)
        w[0] /= S
        for i in range(1, len(w)):
            w[i] = w[i]/S + w[i-1]
        self.w = w

    def pickIndex(self):
        return bisect_left(self.w, random())
