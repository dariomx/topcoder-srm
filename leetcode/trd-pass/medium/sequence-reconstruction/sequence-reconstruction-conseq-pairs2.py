"""
I originally wanted to do the topological sorting, but could not
figure out an efficient way to detect it was unique; read somewhere
that if you got a Hamiltonian path then is unique, but the algorithms
for checking that seemed expensive.

Then I came out with this alternate approach, which to be honest, I am
not sure if it will work for all cases (it does for the ones in this
leetcode problem though). Basically I am just computing a subset
of the less-than relationship that the sequences imply; the one
computed by the consecutive elements (think everybody does that
for the graph though; though when exploring topo-sort  or transitive
closure, I was putting every pair ... anyway).

With that subset relation, after checking it is consistent among
the subsequences and also against the order in org; then I just
check that all same sub-relation from org is a subset of the sub-relation
from sequences. But wait, I may just compare for equality.


"""
class Solution:
    def getRelation(self, seqs, refSeq):
        refSeq = {x: i for (i, x) in enumerate(refSeq)}
        rel = set()
        for seq in seqs:
            m = len(seq)
            for i in range(m):
                x = seq[i]
                if x not in refSeq:
                    return None
                if i == m - 1:
                    break
                y = seq[i + 1]
                if y not in refSeq:
                    return None
                if x == y or refSeq[x] > refSeq[y]:
                    return None
                else:
                    rel.add((x, y))
        return rel

    def checkOrder(self, org, ltRel):
        for i in range(len(org) - 1):
            if (org[i], org[i + 1]) not in ltRel:
                return False
        return True

    def sequenceReconstruction(self, org: List[int],
                               seqs: List[List[int]]) -> bool:
        ltRel = self.getRelation(seqs, org)
        if len(seqs) == 0 or ltRel is None:
            return False
        elif len(ltRel) == 0:
            return len(org) <= 1
        else:
            return self.checkOrder(org, ltRel)
