from collections import deque

class Solution:
    def levelOrderBottom(self, root):
        queue = deque()
        if root:
            queue.append((root, 0))
        prev_lev = None
        ans = deque()
        tmp = []
        while queue:
            node, lev = queue.popleft()
            if prev_lev is None:
                prev_lev = lev
            elif lev != prev_lev:
                ans.appendleft(tmp)
                tmp = []
                prev_lev = lev
            tmp.append(node.val)
            for child in (node.left, node.right):
                if child:
                    queue.append((child, lev+1))
        if tmp:
            ans.appendleft(tmp)
        return list(ans)