"""
Python3 solution with O(k) space and O(n) time.

We are tempted to do a first pass to compute list size, but all we need are the
sizes of the parts. To calculate those we initialize an array of k sizes, and
iterate over the nodes. For each iteration i-th, we increase the size with
index i%k (which means we give preference to those on the left).

Once we have computed the part sizes, we just iterate over the k parts and for
each one move forward the node pointer as many times as needed; so we find
the head of the next sub-list. On those transitions we clean the next pointer of
the previous node.

Note: after looking at editorial solution, I realized that one could avoid
the O(k) space by realizing that n%k will be spread evenly (1 element) among
the first n%k parts.
"""

class Solution:
    def splitListToParts(self, root, k):
        node = root
        i = 0
        sizes = [0] * k
        while node:
            sizes[i % k] += 1
            i += 1
            node = node.next
        parts = [root]
        node = root
        prev = None
        for j in range(k - 1):
            for _ in range(sizes[j]):
                prev = node
                node = node.next
            if prev:
                prev.next = None
            parts.append(node)
        return parts


