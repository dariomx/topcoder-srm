class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        ixs, ixe = [], []
        for i in range(len(start)):
            if start[i] != 'X':
                ixs.append(i)
            if end[i] != 'X':
                ixe.append(i)
        if len(ixs) != len(ixe):
            return False
        for i, j in zip(ixs, ixe):
            if start[i] != end[j]:
                return False
            if start[i] == 'R' and i > j:
                return False
            if start[i] == 'L' and i < j:
                return False
        return True