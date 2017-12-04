"""
To prevent max memory errors that I got with recursive + caching solution, 
this approach tries to minimize the time entries are in temporary storage. 
For this, we initialize the base cases (1 and 2 len palindromes) and store 
their (start, end) indices in a queue.

Then we iterate until queue is empty: for each iteration we pop one pair of 
indices (i,j) and check whether they can be extended to become a larger 
palindrome. If they can, we add the extended range (i-1, j+1) to the queue; 
otherwise, it means that is the maximum palindrome we can get from that 
option, hence we need to check if it defeats our current champion.

This way, the entries (which are just pair of indices anyway), live on the 
queue long enough to be evaluated; but not beyond (meaning, we do not attempt 
to accumulate all possible candidates at same time).
"""

from collections import deque


class Solution(object):
    def longestPalindrome(self, s):
        queue = deque()
        n = len(s)
        for i in xrange(n):
            queue.append((i, i))
        for i in xrange(n - 1):
            if s[i] == s[i + 1]:
                queue.append((i, i + 1))
        max_len = 0
        pal_idx = None
        while queue:
            i, j = queue.popleft()
            if i > 0 and j < n - 1 and s[i - 1] == s[j + 1]:
                queue.append((i - 1, j + 1))
            elif (j - i + 1) > max_len:
                max_len = (j - i + 1)
                pal_idx = (i, j)
        i, j = pal_idx
        return s[i:j + 1]
