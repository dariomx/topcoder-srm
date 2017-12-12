from collections import deque
from sys import stdin, stdout

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
                if len(seq) > 0:
                    seqSum -= arr[seq.popleft()]
                else:
                    break
        if seqSum == target:
            return seq
        else:
            return None

soln = Solution()
n = int(stdin.readline())
for _ in range(n):
    _, target = stdin.readline().split()
    target = int(target)
    arr = stdin.readline().split()
    arr = list(map(int, arr))
    seq = soln.findSeq(arr, target)
    if seq is None:
        print(-1)
    else:
        print("%d %d" % (seq[0]+1, seq[-1]+1))
