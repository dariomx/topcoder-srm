class Solution:
    def intersect(self, l: 'Node', r: 'Node') -> 'Node':
        if l.isLeaf == 1 and r.isLeaf == 1:
            val_or = (l.val == 1) or (r.val == 1)
            ans = Node(val_or, 1, None, None, None, None)
        elif (l.isLeaf == 0 and r.isLeaf == 1 and r.val == 1) or \
                (l.isLeaf == 1 and r.isLeaf == 0 and l.val == 1):
            ans = Node(1, 1, None, None, None, None)
        elif l.isLeaf == 0 and r.isLeaf == 1:
            ans = Node(0, 0,
                       self.intersect(l.topLeft, r),
                       self.intersect(l.topRight, r),
                       self.intersect(l.bottomLeft, r),
                       self.intersect(l.bottomRight, r))
        elif l.isLeaf == 1 and r.isLeaf == 0:
            ans = Node(0, 0,
                       self.intersect(l, r.topLeft),
                       self.intersect(l, r.topRight),
                       self.intersect(l, r.bottomLeft),
                       self.intersect(l, r.bottomRight))
        elif l.isLeaf == 0 and r.isLeaf == 0:
            ans = Node(0, 0,
                       self.intersect(l.topLeft, r.topLeft),
                       self.intersect(l.topRight, r.topRight),
                       self.intersect(l.bottomLeft, r.bottomLeft),
                       self.intersect(l.bottomRight, r.bottomRight))
        if ans.isLeaf == 0 and \
                ans.topLeft.isLeaf == 1 and ans.topRight.isLeaf == 1 and \
                ans.bottomLeft.isLeaf == 1 and ans.bottomRight.isLeaf == 1 and \
                ans.topLeft.val == ans.topRight.val and \
                ans.topRight.val == ans.bottomLeft.val and \
                ans.bottomLeft.val == ans.bottomRight.val:
            ans = Node(1, ans.topLeft.val, None, None, None, None)
        return ans
