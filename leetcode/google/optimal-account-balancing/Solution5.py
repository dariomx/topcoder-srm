from collections import defaultdict
from itertools import permutations
from sys import maxint


class Solution(object):
    def removeEq(self, pos, neg):
        pos.sort(reverse=True)
        neg.sort(reverse=True)
        newPos = []
        newNeg = []
        cnt = 0
        while pos and neg:
            if pos[-1] == neg[-1]:
                pos.pop()
                neg.pop()
                cnt += 1
            elif pos[-1] < neg[-1]:
                newPos.append(pos.pop())
            else:
                newNeg.append(neg.pop())
        newPos += pos
        newNeg += neg
        return newNeg, newPos, cnt

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
        pos, neg, cntEq = self.removeEq(pos, neg)
        minOpers = maxint
        for pp in permutations(pos):
            for np in permutations(neg):
                minOpers = min(minOpers, self.countOpers(pp, np, minOpers))
        return cntEq + minOpers


# trans = [[0,1,10],[2,0,5]]
# trans = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
trans = [[1, 8, 1], [1, 13, 21], [2, 8, 10], [3, 9, 20], [4, 10, 61],
         [5, 11, 61], [6, 12, 59], [7, 13, 60]]
trans = [[0, 1, 2], [1, 2, 1], [1, 3, 1]]
print(Solution().minTransfers(trans))
