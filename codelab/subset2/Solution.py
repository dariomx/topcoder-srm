class Node:
    def __init__(self, final):
        self.child = dict()
        self.final = final

    def _add(self, arr, i):
        if i == len(arr):
            wasFinal = self.final
            self.final = True
            return wasFinal
        else:
            if arr[i] in self.child:
                return self.child[arr[i]]._add(arr, i+1)
            else:
                node = Node(i == len(arr)-1)
                node._add(arr, i+1)
                self.child[arr[i]] = node
                return False

    def add(self, arr):
        return self._add(arr, 0)

class Solution:
    def powerset(self, arr, i, used):
        if i >= len(arr):
            return [[]]
        else:
            without = self.powerset(arr, i+1, used)
            subsets = []
            for s in without:
                ss = sorted([arr[i]] + s)
                found = used.add(ss)
                if not found:
                    subsets.append(ss)
            subsets += without
            return subsets

    def subsetsWithDup(self, arr):
        arr = sorted(arr)
        return sorted(self.powerset(arr, 0, Node(False)))

#print(Solution().subsetsWithDup([1,2,2]))
print(Solution().subsetsWithDup([ 6, 6, 3, 3, 6, 5 ]))
