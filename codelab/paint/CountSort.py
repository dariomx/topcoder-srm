from sys import maxsize
from random import shuffle, randint

def countSort(A):
    n = len(A)
    B = [-1] * n
    C = dict()
    minA, maxA = maxsize, -1
    for i in xrange(n):
        C[A[i]] = C.get(A[i], 0) + 1
        minA = min(minA, A[i])
        maxA = max(maxA, A[i])
    prev = None
    for x in xrange(minA, maxA+1):
        if x in C:
            C[x] += C.get(prev, 0)
            prev = x
    for i in xrange(n-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B

n = 100
A = [randint(0,n) for _ in xrange(n)]
#A = range(n)
#shuffle(A)
print(A)
print(countSort(A))