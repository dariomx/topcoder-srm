class Solution:
    def findQuad(self, arr, S):
        n = len(arr)
        sum2 = dict()
        for i in xrange(n):
            for j in xrange(i):
                sum2[S - (arr[i] + arr[j])] = [i, j]
        for i in xrange(n):
            for j in xrange(i):
                pair = sum2.get(arr[i] + arr[j], None)
                if pair is not None and i not in pair and j not in pair:
                    return sorted(map(arr.__getitem__, pair + [i, j]))
        return None

print(Solution().findQuad([1,2,3,4], 10))

