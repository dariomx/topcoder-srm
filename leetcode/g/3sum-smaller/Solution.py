from collections import defaultdict


class BST:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx
        self.left = None
        self.right = None


class Solution(object):
    def createBST(self, A, start, end):
        if start > end:
            return None
        else:
            mid = (start + end) / 2
            node = BST(A[mid], mid)
            node.left = self.createBST(A, start, mid - 1)
            node.right = self.createBST(A, mid + 1, end)
            return node

    def getBST(self, A):
        return self.createBST(A, 0, len(A) - 1)

    def findMax(self, root):
        node = root
        while node.right:
            node = node.right
        return node

    def findMaxLT(self, node, x):
        if node.val == x:
            if node.left:
                return self.findMax(node.left)
            else:
                return None
        elif node.val < x:
            if node.right:
                if node.right.val < x:
                    return self.findMaxLT(node.right, x)
                else:
                    return node
            else:
                return node
        else:
            if node.left:
                return self.findMaxLT(node.left, x)
            else:
                return None

    def getSum2(self, A):
        n = len(A)
        sum2 = defaultdict(list)
        for i in xrange(n):
            for j in xrange(i + 1, n):
                sum2[A[i] + A[j]].append((i, j))
        return sum2

    def threeSumSmaller(self, A, target):
        counted = set()
        A.sort()
        sum2 = self.getSum2(A)
        bst = self.getBST(A)
        for s2 in sum2:
            maxLT = self.findMaxLT(bst, target - s2)
            if maxLT is not None:
                for k in xrange(maxLT.idx + 1):
                    for (i, j) in sum2[s2]:
                        if k not in (i, j):
                            counted.add(tuple(sorted([i, j, k])))
        print(counted)
        return len(counted)


print(
Solution().threeSumSmaller([3, 2, -2, 6, 2, -2, 6, -2, -4, 2, 3, 0, 4, 4, 1],
                           3))
