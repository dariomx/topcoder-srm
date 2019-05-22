"""
Recursive Python3 solution with pruning

I recall having done a similar exercise, and really liked a counter technique
that a friend used. Typically, from school we learn that in order to check
balanced parentheses we gotta use an stack. But in this particular case,
a simple counter is good enough: every time you find an opening parenthesis
you increase the counter, and every time you see a closing one you decrease
it. When you finish going over the input stream, you can assume that if the
counter is zero, then the parentheses were balanced.

So, the recursion algorithm checks position i-th, and considers two branches
from there: what happens if we remove that position, and what happens if we
leave it. The base cases are the following:

1) When we finish exploring the string, we need to check if the parentheses
were balanced (cnt==0). If the formed solution at that point, has the same
number of removals as the ones observed so far; we just append to the answer.
But, if we find it has less removals; we need to discard whatever solutions
we have so far.

2) We do a couple of optimizations aiming pruning, which are the following:

2.1) When the counter is negative meaning that we have unbalanced case (more
closing parentheses than opening).

2.2) When the counter reflects more opening parentheses that remaining
characters on the string; this means we can not close them all, so it does
not make sense to continue with that branch.

Time complexity is O(n * log(m)), because for every single character we can
potentially add it to a set of size m; where m represents the maximum number
of solutions we could have at any moment. Space complexity would be O(m). I
guess that we could produce upper bounds for m, in terms of n; but gotta go
back to work now ;-?

"""

from sys import maxsize as maxint


class Solution(object):
    def removeInvalidParentheses(self, s):
        ans = set()
        ans_nrem = maxint
        n = len(s)

        def rec(i, cnt, soln):
            nonlocal ans_nrem
            nrem = n - len(soln)
            if i == n:
                if cnt == 0:
                    if nrem < ans_nrem:
                        ans.clear()
                        ans_nrem = nrem
                        ans.add(soln)
                    elif nrem == ans_nrem:
                        ans.add(soln)
            elif cnt < 0 or cnt > nrem:
                return
            else:
                c = s[i]
                new_cnt = cnt
                if c == '(':
                    new_cnt += 1
                elif c == ')':
                    new_cnt -= 1
                rec(i + 1, new_cnt, soln + c)
                if new_cnt != cnt:
                    rec(i + 1, cnt, soln)

        rec(0, 0, '')
        return list(ans)
