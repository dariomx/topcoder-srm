class Solution:
    def pathSum(self, root, sum):
        started = set()
        ans = 0

        def rec(node, psum):
            if not node:
                return
            nonlocal ans
            psum += node.val
            if psum == sum:
                ans += 1
            if node not in started:
                started.add(node)
                rec(node, 0)
            rec(node.left, psum)
            rec(node.right, psum)

        started.add(root)
        rec(root, 0)
        return ans
