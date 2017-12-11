"""
Python solution with overkill comparator

This solution did not reach the 90% block, cause the comparator was more
expensive than needed. As one can read on the editorial solution, this
greedy strategy only requires to sort by the second element. My (incorrect)
intuition was that in addition to the second element, I needed to also
consider the first in order to always make the best greedy choice on cases
with a tie. For example, assuming we started with (1,2) let us suppose we
have the following options left:

[2,4], [3,4], [6,7]

We could use either of the first two options as next slab, but whether we
pick [2,4] or [3,4] is irrelevant. Once we join with the chain, the only
thing that matters is the second position of tuple. Also, given we are
exploring whole sequence anyway, doing sub-sorting by the first position
seemed not really needed.

"""

class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda p: (p[1], p[0]))
        a, b = pairs[0]
        curr_len = 1
        for (c,d) in pairs[1:]:
            if b < c:
                curr_len += 1
                a, b = c, d
        return curr_len