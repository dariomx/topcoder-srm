class Solution:
    def depthSumInverse(self, nestedList):
        def maxDepth(lst):
            depth = 0
            for child in lst:
                if not child.isInteger():
                    depth = max(depth, maxDepth(child.getList()))
            depth += 1
            return depth

        def depthSum(lst, depth):
            nonlocal ans
            for child in lst:
                if child.isInteger():
                    ans += depth * child.getInteger()
                else:
                    depthSum(child.getList(), depth - 1)

        ans = 0
        depthSum(nestedList, maxDepth(nestedList))
        return ans
