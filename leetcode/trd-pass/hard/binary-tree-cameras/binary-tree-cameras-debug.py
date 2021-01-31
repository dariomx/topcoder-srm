from math import inf

from drawtree import deserialize, drawtree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        UNCOV = 0
        COV = 1
        CAM = 2
        uncov = lambda x: x == UNCOV
        cov = lambda x: x == COV
        cam = lambda x: x == CAM

        def valid(pa, granpa):
            return (uncov(pa) and uncov(granpa)) or \
                   (uncov(pa) and cov(granpa)) or \
                   (cov(pa) and cam(granpa)) or \
                   (cam(pa) and cov(granpa))

        def children(n, pa, granpa):
            return cnt(n.left, pa, granpa) + cnt(n.right, pa, granpa)

        def cnt(n, pa, granpa):
            if not valid(pa, granpa):
                raise ValueError('cant be')
            elif n is None:
                if uncov(pa) and cov(granpa):
                    return inf
                else:
                    return 0
            elif uncov(pa) and uncov(granpa):
                return inf
            elif uncov(pa) and cov(granpa):
                return 1 + children(n, CAM, COV)
            elif cov(pa) and cam(granpa):
                return min(1 + children(n, CAM, COV),
                           children(n, UNCOV, COV))
            elif cam(pa) and cov(granpa):
                return children(n, COV, CAM)

        return cnt(root, COV, CAM)

# main
root = deserialize('[0,0,0,null,0,0,null,null,0]')
drawtree(root)
print(Solution().minCameraCover(root))
