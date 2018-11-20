class Solution:
    def findMode(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        prev = None
        cnt = 0
        max_cnt = 0
        modes = []
        def check_cnt(x):
            nonlocal max_cnt, modes
            if cnt > max_cnt:
                max_cnt = cnt
                modes = [x]
            elif cnt == max_cnt:
                modes.append(x)
        for x in inorder(root):
            if prev is None or x == prev:
                cnt += 1
            else:
                check_cnt(prev)
                cnt = 1
            prev = x
        if prev is not None:
            check_cnt(prev)
        return modes
