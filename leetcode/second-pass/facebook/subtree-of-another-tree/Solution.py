class Solution:
    def isSubtree(self, s, t):
        def eq(r1, r2):
            if r1 is None and r2 is None:
                return True
            elif r1 and r2 and r1.val == r2.val:
                return eq(r1.left, r2.left) and eq(r1.right, r2.right)
            else:
                return False

        def search(r):
            ret = eq(r, t)
            if not ret and r is not None:
                ret = search(r.left) or search(r.right)
            return ret

        return search(s)
