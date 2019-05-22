class Solution:
    def calPoints(self, ops):
        ans = 0
        prev = []
        for op in ops:
            if op == '+':
                p = prev[-2] + prev[-1]
            elif op == 'D':
                p = 2 * prev[-1]
            elif op == 'C':
                p = -prev.pop()
            else:
                p = int(op)
            if op != 'C':
                prev.append(p)
            ans += p
        return ans