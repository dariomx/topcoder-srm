# are types 2/3 needed?

from operator import add, sub, mul, truediv as div
from itertools import permutations as perm, product as prod

EPS = 1e-10


class Solution:
    def evalType1(self, nums, ops):
        a, b, c, d = nums
        f, g, h = ops
        return f(a, g(b, h(c, d)))

    def evalType2(self, nums, ops):
        a, b, c, d = nums
        f, g, h = ops
        return f(g(a, h(b, c)), d)

    def evalType3(self, nums, ops):
        a, b, c, d = nums
        f, g, h = ops
        return f(a, g(h(b, c), d))

    def evalType4(self, nums, ops):
        a, b, c, d = nums
        f, g, h = ops
        return g(f(a, b), h(c, d))

    def judgePoint24(self, nums: List[int]) -> bool:
        ops = [add, sub, mul, div]
        evals = [self.evalType1, self.evalType2, self.evalType3, self.evalType4]
        for p in perm(nums):
            for q in prod(ops, ops, ops):
                for ev in evals:
                    try:
                        if abs(ev(p, q) - 24) < EPS:
                            return True
                    except ZeroDivisionError:
                        None
                    except:
                        raise
        return False