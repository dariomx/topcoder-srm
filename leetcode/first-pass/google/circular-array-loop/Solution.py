WHITE = 0
GRAY = 1
BLACK = 2

class Solution(object):
    def dfs(self, nums, child_dir):
        n = len(nums)
        color = [WHITE] * n
        sign = lambda i: +1 if nums[i] > 0 else -1

        def visit(node, parent=None):
            if sign(node) != child_dir:
                return
            elif color[node] == GRAY:
                if node == parent:
                    return
                else:
                    raise ValueError("cycle detected")
            elif color[node] == BLACK:
                return
            else:
                color[node] = GRAY
                child = (node + nums[node]) % n
                visit(child, node)
                color[node] = BLACK

        for node in range(n):
            if color[node] == WHITE:
                visit(node)

    def circularArrayLoop(self, nums):
        try:
            self.dfs(nums, +1)
            self.dfs(nums, -1)
            return False
        except ValueError:
            return True

