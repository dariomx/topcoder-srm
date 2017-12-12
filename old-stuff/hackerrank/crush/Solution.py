#!/bin/python

import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = [0] * n
    for a0 in xrange(m):
        a, b, k = raw_input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        arr[a-1] += k
        if b < n:
            arr[b] -= k
    max_x = 0
    curr = 0
    for x in arr:
        curr += x
        max_x = max(max_x, curr)
    print(max_x)

