from collections import defaultdict


class Solution(object):
    def addOne(self, arr, k):
        rem = 1
        for i in xrange(len(arr)):
            tmp = arr[i] + rem
            arr[i] = tmp % k
            rem = tmp / k

    def isValid(self, arr):
        cnt = 0
        cnt = defaultdict(lambda: 0)
        for i in xrange(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                cnt[arr[i]] += 1
            if cnt[arr[i]] > 1:
                return False
        return True

    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0 or k == 0:
            return 0
        cnt = 0
        arr = [0] * n
        for _ in xrange(0, k ** n):
            if self.isValid(arr):
                cnt += 1
            else:
                print(list(reversed(arr)))
            self.addOne(arr, k)
        return cnt


print(Solution().numWays(5, 2))
