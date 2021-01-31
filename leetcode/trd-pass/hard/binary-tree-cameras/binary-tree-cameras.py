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
            elif uncov(pa) and l:
                left = cnt(n.left, UNCOV, l)
                if left < inf:
                    pa = COV
                return left + cnt(n.right, pa, r)
            elif uncov(pa) and r:
                right = cnt(n.right, UNCOV, r)
                if right < inf:
                    pa = COV
                return cnt(n.left, pa, l) + right
            else:
                return cnt(n.left, pa, l) + cnt(n.right, pa, r)

        @cache
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
            else:
                return min(children(n, False, False, COV),
                           children(n, False, True, COV),
                           children(n, True, False, COV),
                           children(n, True, True, COV))

        return min(cnt(root, COV, False), cnt(root, COV, True))
