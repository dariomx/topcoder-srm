"""
Python with linear time

Compute the unique paths of both nodes using binary search, which gives us
O(log(n)); then traverse such paths from left to right (they will begin at
root), while they match. The last matching node will be the lowest common
ancestor. This last matching process is the one taking O(n), so an optimization
should try to avoid it.
"""

from collections import deque


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def bin_search(root, end):
            path = deque()
            stack = [root]
            while stack:
                node = stack.pop()
                path.append(node)
                if node is None:
                    return None
                elif node == end:
                    return path
                elif end.val < node.val:
                    stack.append(node.left)
                else:
                    stack.append(node.right)
            return None

        path1 = bin_search(root, p)
        path2 = bin_search(root, q)
        lowest = None
        while path1 and path2 and path1[0] == path2[0]:
            lowest = path1.popleft()
            path2.popleft()
        return lowest
