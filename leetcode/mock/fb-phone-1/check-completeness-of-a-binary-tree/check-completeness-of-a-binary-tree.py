from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque()
        if root:
            queue.append((root, 0))
        prevLev, cnt, sawNone = -1, 0, False
        while queue:
            node, lev = queue.popleft()
            if node and lev != prevLev:
                if prevLev >= 0 and cnt != 2 ** prevLev:
                    return False
                prevLev = lev
                cnt = 0
            if node is None:
                sawNone = True
                continue
            elif sawNone:
                return False
            else:
                cnt += 1
                for child in (node.left, node.right):
                    queue.append((child, lev + 1))
        return True


