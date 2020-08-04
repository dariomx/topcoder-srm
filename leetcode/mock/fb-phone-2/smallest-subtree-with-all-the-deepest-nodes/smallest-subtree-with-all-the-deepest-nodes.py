class Solution:
    def findMaxDepth(self, node, depth):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return depth
        else:
            return max(self.findMaxDepth(node.left, depth + 1),
                       self.findMaxDepth(node.right, depth + 1))

    def countDeepest(self, node, depth, maxDepth, cache):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            cnt = int(depth == maxDepth)
        else:
            cnt = self.countDeepest(node.left, depth + 1, maxDepth, cache) + \
                  self.countDeepest(node.right, depth + 1, maxDepth, cache)
        cache[node] = cnt, depth
        return cnt

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        maxDepth = self.findMaxDepth(root, 0)
        cache = dict()
        self.countDeepest(root, 0, maxDepth, cache)
        maxCnt = cache[root][0]
        ans = root
        ansDepth = 0
        for node, (cnt, depth) in cache.items():
            print((node.val, cnt, depth, ans.val, ansDepth))
            if cnt == maxCnt and depth > ansDepth:
                ans = node
                ansDepth = depth
        return ans