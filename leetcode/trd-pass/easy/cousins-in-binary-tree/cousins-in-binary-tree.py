# originally used dfs, but bfs makes more sense (saw it from editorial soln); with
# dfs we can potentially traverse the whole tree, and with bfs just up to the needed
# layer

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth = dict()
        parent = dict()
        queue = deque()
        if root:
            queue.append((root, 0, None))
        while queue:
            node, d, p = queue.popleft()
            if node.val in (x, y):
                depth[node.val] = d
                parent[node.val] = p
                if len(depth) == 2:
                    return depth[x] == depth[y] and parent[x] != parent[y]
            for child in (node.left, node.right):
                if child:
                    queue.append((child, d+1, node))
        return False