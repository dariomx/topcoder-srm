
from collections import deque

class Solution:
    def findSeq(self, arr, target):
        n = len(arr)
        seq = deque()
        seqSum = 0
        i = -1
        while seqSum != target:
            if seqSum < target:
                if i < (n-1):
                    i += 1
                    seq.append(i)
                    seqSum += arr[i]
                else:
                    break
            else:
                seqSum -= arr[seq.popleft()]
        if seqSum == target:
            return seq
        else:
            return None

soln = Solution()
def seeAns(seq):
    if seq is None:
        print(-1)
    else:
        print(map(arr.__getitem__, seq))

arr = [23, 5, 4, 7, 2, 11]
seeAns(soln.findSeq(arr, 20))

arr = [1, 3, 5, 23, 2]
seeAns(soln.findSeq(arr, 8))
seeAns(soln.findSeq(arr, 7))

arr = [1, 2, 3, 7, 5]
seeAns(soln.findSeq(arr, 12))