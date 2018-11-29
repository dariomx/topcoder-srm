from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck):
        return reduce(gcd, set(Counter(deck).values())) >= 2

