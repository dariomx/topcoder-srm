from collections import deque

class Solution(object):
    def levelOrder(self, root):
        ans = []
        queue = deque()
        if root:
            queue.append((root, 1))
        while queue:
            node, lev = queue.popleft()
            if lev > len(ans):
                ans.append([])
            ans[-1].append(node.val)
            for chd in node.children:
                queue.append((chd, lev+1))
        return ans