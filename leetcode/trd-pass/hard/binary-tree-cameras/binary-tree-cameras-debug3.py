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

        def children(n, l, r, pa):
            if n.left is None and n.right is not None:
                return cnt(n.right, pa, r)
            if n.left is not None and n.right is None:
                return cnt(n.left, pa, l)
            else:
                return cnt(n.left, pa, l) + cnt(n.right, pa, r)

        def cnt(n, pa, pcam):
            if n is None:
                if uncov(pa):
                    return inf
                else:
                    return 0
            elif pcam:
                return 1 + min(children(n, False, False, CAM),
                               children(n, False, True, CAM),
                               children(n, True, False, CAM),
                               children(n, True, True, CAM))
            elif uncov(pa):
                return inf
            elif cov(pa):
                return min(children(n, False, True, UNCOV),
                           children(n, True, False, UNCOV),
                           children(n, True, True, UNCOV))
            elif cam(pa):
                return children(n, False, False, COV)

        return min(cnt(root, COV, False), cnt(root, COV, True))

# main
root = deserialize('[0,0,0,null,0,0,null,null,0]')
# drawtree(root)
print(Solution().minCameraCover(root))
