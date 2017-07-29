from itertools import permutations
from collections import defaultdict
from sys import maxint
from datetime import datetime

class Solution(object):
    def countOpers(self, posPerm, negPerm, minOpers):
        posStack = list(posPerm)
        negStack = list(negPerm)
        cnt = 0
        while posStack:
            posBal = posStack.pop()
            negBal = negStack.pop()
            rem = negBal - posBal
            if rem > 0:
                negStack.append(rem)
            elif rem < 0:
                posStack.append(-rem)
            cnt += 1
            if cnt >= minOpers:
                return cnt
        return cnt

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
        for b in balance.itervalues():
            if b > 0:
                pos.append(b)
            elif b < 0:
                neg.append(-b)
        minOpers = maxint
        start = datetime.now()
        for pp in permutations(pos):
            for np in permutations(neg):
                minOpers = min(minOpers, self.countOpers(pp, np, minOpers))
        end = datetime.now()
        print(end - start)
        return minOpers

trans = [[0,1,10],[2,0,5]]
#trans = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
#trans = [[1,8,1],[1,13,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,12,59],[7,13,60]]
print(Solution().minTransfers(trans))