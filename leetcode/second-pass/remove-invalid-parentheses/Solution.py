from sys import maxsize as maxint


class Solution:
    def removeInvalidParentheses(self, s):
        n = len(s)
        min_dels = maxint
        min_sols = set()

        def rec(i, cnt, dels):
            nonlocal min_dels, min_sols
            if i == n:
                if cnt == 0:
                    sol = "".join([s[i] for i in range(n) if i not in dels])
                    # print((1, i, cnt, dels, sol, min_dels, min_sols))
                    if len(dels) == min_dels:
                        min_sols.add(sol)
                    elif len(dels) < min_dels:
                        min_dels = len(dels)
                        min_sols.clear()
                        min_sols.add(sol)
                        # print((2, i, cnt, dels, sol, min_dels, min_sols))

            elif s[i] in ('(', ')'):
                dels.add(i)
                rec(i + 1, cnt, dels)
                dels.remove(i)
                if s[i] == '(':
                    rec(i + 1, cnt + 1, dels)
                elif cnt > 0:
                    rec(i + 1, cnt - 1, dels)
            else:
                rec(i + 1, cnt, dels)

        rec(0, 0, set())
        return list(min_sols)
