class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, K, T, L):
        n, L = L[0], L[1:]
        #
        def numPaint(cap):
            numP = 1
            timeP = 0
            for i in xrange(n):
                timeB = L[i] * T
                if timeP + timeB > cap:
                    timeP = timeB
                    numP += 1
                else:
                    timeP += timeB
            return numP
        #
        if n < K:
            return -1
        start = max(L) * T
        end = sum(L) * T
        while start < end:
            mid = (start + end) / 2
            numP = numPaint(mid)
            if numP <= K:
                end = mid
            else:
                start = mid + 1
        return start % 10000003

K, T, L = 1, 10, [1,1]
print(Solution().paint(K, T, L))