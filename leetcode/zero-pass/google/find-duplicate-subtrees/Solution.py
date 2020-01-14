"""
Python solution using recursive tree encoding

Uses strings to encode each subtree; pretty much an string version of
the nested tuples one would have for in-order representation:

   enc(root) = (enc(root.left), root,val, enc(root.right))

But when mapping the above into a flat string, we use some string markers
to distinguish whether you were on left, or right. The None case also deserves
its own special marker.

As we progress (recursively) and computed all the nodes encodings, we
just keep track of the # of occurrences and root for each encoding.
At the end we just iterate over that dictionary and filter duplicates.

Each node is processed once, so this should be kind of O(n), not sure though.
"""

from collections import defaultdict


class Solution:
    def encode(self, root, cnt, roots):
        enc = 'N'
        if root:
            enc = 'L' + self.encode(root.left, cnt, roots) + \
                  str(root.val) + \
                  'R' + self.encode(root.right, cnt, roots)
            cnt[enc] += 1
            roots[enc] = root
        return enc

    def findDuplicateSubtrees(self, root):
        cnt = defaultdict(lambda: 0)
        roots = dict()
        self.encode(root, cnt, roots)
        dups = []
        for (enc, k) in cnt.items():
            if k > 1:
                dups.append(roots[enc])
        return dups
