"""
This is faster approach leveraging counting sort algorithm,
whose complexity is linear; O(n), where n = len(s)

It may not be evident that algorithm below is linear, given the
intrinsic nested loops (3 levels). But one way to look at that,
is that we are imposing a tree structure of 2 levels above the list.
On the first level we are grouping per frequency, and on the
second level we group by character. At the bottom level we have
a permutation of the list itself.

Therefore, regardless of how many levels the tree structure above has,
ultimately the dominating factor is the bottom level (recall
for example that leaves level in a full binary tree, has as much
data as the rest of the tree). The bottom level in our imaginary
tree has as many elements as the list (size n); hence the dominating
factor in the nested loops is n itself (adding the extra cost of the
above layers would make cost a multiple of n, leading to O(n)).

Note:
    The original count sort algorithm may assume a fixed range
    in the values, and iterate through that range. Here we are doing
    an small optimization, by iterating only over the observed sub-range
    in the list.

"""

from collections import defaultdict
from itertools import imap


class Solution(object):
    def frequencySort(self, s):
        hist = defaultdict(lambda: 0)
        for c in s:
            hist[c] += 1
        cnt = defaultdict(lambda: [])
        min_k, max_k = len(s), 0
        for c, k in hist.iteritems():
            cnt[k].append(c)
            min_k = min(min_k, k)
            max_k = max(max_k, k)
        sorted_s = ''
        for k in xrange(max_k, min_k - 1, -1):
            if k in cnt:
                sorted_s += ''.join(imap(lambda c: c * k, cnt[k]))
        return sorted_s
