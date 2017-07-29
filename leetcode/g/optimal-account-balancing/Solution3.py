from itertools import permutations
from collections import defaultdict
from sys import maxint
from datetime import datetime

class Solution(object):
    def getClosest(self, S, t):
        closest = None
        minDiff = maxint
        for k, x in S:
            diff = abs(t - x)
            if diff < minDiff:
                minDiff = diff
                closest = k, x
        return closest

    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        snd = lambda t: t[1]
        balance = defaultdict(lambda: 0)
        for x, y, z in transactions:
            balance[x] += z
            balance[y] -= z
        pos, neg = [], []
        for k, b in balance.iteritems():
            if b > 0:
                pos.append((k, b))
            elif b < 0:
                neg.append((k, -b))
        opers = 0
        while neg:
            kn, negBal = max(neg, key=snd)
            neg.remove((kn, negBal))
            kp, posBal = self.getClosest(pos, negBal)
            pos.remove((kp, posBal))
            rem = negBal - posBal
            if rem > 0:
                neg.append((kn, rem))
            elif rem < 0:
                pos.append((kp, -rem))
            opers += 1
        return opers

#trans = [[0,1,10],[2,0,5]]
#trans = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
trans = [[1,8,1],[1,13,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,12,59],[7,13,60]]
print(Solution().minTransfers(trans))