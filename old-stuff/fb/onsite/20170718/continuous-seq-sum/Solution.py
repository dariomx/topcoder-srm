
from collections import deque

class Solution:
    def findSeq(self, arr, target):
        seq = deque()
        seqSum = 0
        for x in arr:
            seq.append(x)
            seqSum += x
            while seqSum > target:
                seqSum -= seq.popleft()
            if seqSum == target:
                return seq
        return None

soln = Solution()

arr = [23, 5, 4, 7, 2, 11]
print(soln.findSeq(arr, 20))

arr = [1, 3, 5, 23, 2]
print(soln.findSeq(arr, 8))
print(soln.findSeq(arr, 7))

arr = [1, 2, 3, 7, 5]
print(soln.findSeq(arr, 12))