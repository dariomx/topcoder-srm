class Solution:
    def isMonotonic(self, A):
        n = len(A)
        if n < 2:
            return True
        else:
            get_sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
            cnt = [0, 0, 0]
            for i in range(1, n):
                sign = get_sign(A[i - 1] - A[i])
                cnt[sign] += 1
                if cnt[1] > 0 and cnt[-1] > 0:
                    return False
            return True
