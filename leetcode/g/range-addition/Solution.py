class Solution(object):
    def getModifiedArray(self, n, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0] * n
        for a, b, k, in updates:
            arr[a] += k
            if b < n - 1:
                arr[b + 1] -= k
        acc = 0
        for i in xrange(n):
            acc += arr[i]
            arr[i] = acc
        return arr
