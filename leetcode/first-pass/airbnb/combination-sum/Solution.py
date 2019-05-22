'''
Inspired by generic template to compute power set, where at
each element you have two branches (to include or not to include),
I adapted to this problem by having k ways of adding each element
to current combination. Problem is that it may be less expensive to
allow the recursion go horizontal, aiming that you have more variety
of options. In that other style, base case would had been tied to
current sum, not to current index.
'''

class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        def rec(i, s, comb):
            if i == len(candidates):
                if s == target:
                    ans.append(list(comb))
            elif s <= target:
                x = candidates[i]
                max_k = target//x
                for k in range(1, max_k + 1):
                    comb.append(x)
                    s += x
                    rec(i+1, s, comb)
                if max_k > 0:
                    del comb[-max_k:]
                    s -= x * max_k
                rec(i+1, s, comb)
        rec(0, 0, [])
        return ans