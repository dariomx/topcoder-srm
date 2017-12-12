from collections import defaultdict


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balance = defaultdict(lambda: 0)
        for x, y, z in transactions:
            balance[x] += z
            balance[y] -= z
        pos, neg = [], []
        for k, b in balance.iteritems():
            if b > 0:
                pos.append(b)
            elif b < 0:
                neg.append(-b)
        pos.sort()
        neg.sort()
        opers = 0
        while neg:
            negBal = neg.pop()
            posBal = pos.pop()
            rem = negBal - posBal
            if rem > 0:
                neg.append(rem)
            elif rem < 0:
                pos.append(-rem)
            opers += 1
        return opers


# trans = [[0,1,10],[2,0,5]]
# trans = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
trans = [[1, 8, 1], [1, 13, 21], [2, 8, 10], [3, 9, 20], [4, 10, 61],
         [5, 11, 61], [6, 12, 59], [7, 13, 60]]
print(Solution().minTransfers(trans))
