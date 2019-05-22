class Solution:
    def repeatedStringMatch(self, A, B):
        n = len(B)
        m = len(A)
        start = B.find(A)
        if start < 0 or m >= n:
            if A.find(B) >= 0:
                return 1
            elif (A + A).find(B) >= 0:
                return 2
            else:
                return -1
        cnt = 0
        if start > 0:
            cnt += 1
        j = 0
        for i in range(start, n):
            k = j % m
            if A[k] != B[i]:
                return -1
            if k == 0:
                cnt += 1
            j += 1
        return cnt