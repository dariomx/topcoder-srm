"""
Python3 solution with a single pass

We convert the number into an array of digits, and iterate through it. If the
digit in question is <= next one, we keep it as part of the answer. The
interesting thing happens when the condition is not met. For those cases,
we need to use digit-1 and append 9 for the rest of positions.

The trick is that we can not blindly set digit-1 at position i-th, we need to
check first if the condition of being monotone increasing will keep on holding
for previous position; if it does not, we need to go back into our already
computed result until we find a position i such that arr[i-1] <= arr[i]-1.
Once we found such position, we truncate our result so far and proceed to
append the 9's.

The time complexity is linear in terms of the number of digits (m),
but logarithmic in terms of the input N. This is because the number of digits
(in base10) of number N is roughly log_10(N), which in turn is O(log(N))
"""

class Solution:
    def monotoneIncreasingDigits(self, N):
        arr = [int(c) for c in str(N)]
        m = len(arr)
        mid = ''
        for i in range(m):
            if i == m - 1 or arr[i] <= arr[i + 1]:
                mid += str(arr[i])
            else:
                while not (i == 0 or arr[i - 1] <= arr[i] - 1):
                    i -= 1
                mid = mid[:i]
                mid += str(arr[i] - 1)
                mid += ''.rjust(m - i - 1, '9')
                break
        return int(mid)
