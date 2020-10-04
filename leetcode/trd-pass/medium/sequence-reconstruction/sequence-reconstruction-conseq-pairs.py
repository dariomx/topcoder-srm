WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def getRelation(self, seqs, refRel, n):
        rel = set()
        for seq in seqs:
            m = len(seq)
            for i in range(m):
                x = seq[i]
                if not (1 <= x <= n):  # note sure about this
                    return None
                for j in range(i + 1, m):
                    y = seq[j]
                    if x == y or \
                            (y, x) in rel or \
                            (refRel and (x, y) not in refRel):
                        return None
                    rel.add((x, y))
        return rel

    def checkOrder(self, org, ltRel):
        for i in range(len(org) - 1):
            if (org[i], org[i + 1]) not in ltRel:
                return False
        return True

    def sequenceReconstruction(self, org: List[int],
                               seqs: List[List[int]]) -> bool:
        n = len(org)
        refRel = self.getRelation([org], None, n)
        ltRel = self.getRelation(seqs, refRel, n)
        if len(seqs) == 0 or ltRel is None:
            return False
        elif len(ltRel) == 0:
            return len(org) <= 1
        else:
            return self.checkOrder(org, ltRel)
