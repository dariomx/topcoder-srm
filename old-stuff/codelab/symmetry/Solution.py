from collections import deque

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(str):
    str2node = lambda s: None if s=="-1" else TreeNode(int(s))
    toks = str.split()
    n = int(toks[0])
    heap = [None] + map(str2node, toks[1:])
    for i in xrange(1, n+1):
        if heap[i] is None:
            continue
        if 2*i <= n:
            heap[i].left = heap[2*i]
        if 2*i + 1 <= n:
            heap[i].right = heap[2*i + 1]
    return heap[1]

def eqNode(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is not None and n2 is not None and n1.val == n2.val:
        return True
    return False

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, root):
        level = [root]
        while level:
            print(map(lambda n: -1 if n is None else n.val, level))
            n = len(level)
            for i in xrange(n/2):
                if not eqNode(level[i], level[n-1-i]):
                    print("%d != %d" % (i,n-1-i))
                    return 0
            newLevel = []
            for n in level:
                print(-1 if n is None else n.val)
                if n is not None:
                    newLevel.append(n.left)
                    newLevel.append(n.right)
            level = newLevel
        return 1

str = "67 0 4 4 10 6 6 10 16 3 14 9 9 14 3 16 13 -1 7 11 -1 -1 -1 15 15 -1 -1 -1 11 7 -1 13 -1 12 -1 1 -1 -1 -1 -1 -1 -1 -1 -1 1 -1 12 -1 8 -1 5 2 2 5 -1 8 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"
print(Solution().isSymmetric(buildTree(str)))
