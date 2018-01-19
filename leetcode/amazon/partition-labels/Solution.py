"""
Python3 solution with O(n) time complexity

We could be inserting the characters seen so far on a set, and if we had a
way to know when we have seen the last occurrence of each one, we could
remove from such a set. This will allow to detect cases where all characters
up to current position, have been exhausted; and that is the moment to make a
partition.

There are two ways to detect if we have seen the last occurrence of a
character, and both require one extra pass to S: either keep track of last
index where each character was seen, or, count occurrences on first pass and
decrease them on a second pass. We opted for second option (so we can
leverage the Counter class in Python3).

The partition boundaries are tracked with a couple of indexes, start and end,
which are updated every time we find a new partition.
"""


from collections import Counter


class Solution:
    def partitionLabels(self, S):
        parts = []
        cnt = Counter(S)
        curr = set()
        start, end = 0, 0
        for i in range(len(S)):
            c = S[i]
            end = i
            curr.add(c)
            if cnt[c] == 1:
                curr.remove(c)
            else:
                cnt[c] -= 1
            if len(curr) == 0:
                parts.append(end - start + 1)
                start, end = i + 1, i + 1
        return parts
