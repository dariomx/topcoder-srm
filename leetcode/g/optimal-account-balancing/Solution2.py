from itertools import permutations
from collections import defaultdict
from sys import maxint
from datetime import datetime

class Solution(object):
    def countOpers(self, posPerm, negPerm, cache):
        if len(posPerm) == 0:
            return 0
        else:
            key = posPerm, negPerm
            if key in cache:
                return cache[key]
            else:
                posBal = posPerm[-1]
                negBal = negPerm[-1]
                posPerm = posPerm[:-1]
                negPerm = negPerm[:-1]
                rem = negBal - posBal
                if rem > 0:
                    negPerm = negPerm + (rem,)
                elif rem < 0:
                    posPerm = posPerm + (-rem,)
                cnt = 1 + self.countOpers(posPerm, negPerm, cache)
                cache[key] = cnt
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
        cache = dict()
        start = datetime.now()
        for pp in permutations(pos):
            for np in permutations(neg):
                minOpers = min(minOpers, self.countOpers(pp, np, cache))
        end  = datetime.now()
        print(end - start)
        return minOpers

trans = [[0,1,10],[2,0,5]]
trans = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
trans = [[1,8,1],[1,13,21],[2,8,10],[3,9,20],[4,10,61],[5,11,61],[6,12,59],[7,13,60]]
print(Solution().minTransfers(trans))