"""
An O(n) time solution in Python. Key idea is that a single pass is good
enough; which I realized by comparing this problem with that of finding
sub-arrays which add up to a given target, assuming that all numbers are
positive. The best technique I recall from that related problem, is to
use a sliding window. Same thing happened here.

We keep track of the start/end indexes of our sliding window, which represent
the current substring to explore. In order to detect duplication, we keep
track of the last index seen for each character. If the current character
was seen before start index, that means it lies out of our window and we do not
care; we can proceed to compute the window's length and update our maximum
accordingly. But if last index lies within our current window, we need to
shift our start index to one position after it.

It may look dramatic to discard all characters occurring prior last seen
index, given that the only offending one was current character. But since the
substring needs to be a contiguous section, a guy in the middle can actually
spoil big areas. In this case, the whole left portion of the current window
(left to the last seen occurrence of character).

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        last_idx = dict()
        max_len = 0
        for end in xrange(len(s)):
            c = s[end]
            c_idx, last_idx[c] = last_idx.get(c, -1), end
            if c_idx < start:
                max_len = max(max_len, end - start + 1)
            else:
                start = c_idx + 1
        return max_len
