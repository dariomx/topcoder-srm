class Solution:
    def depthSum(self, nestedList):
        def rec(x, depth=0):
            if type(x) is NestedInteger and x.isInteger():
                return x.getInteger() * depth
            else:
                xs = x if type(x) is list else x.getList()
                return sum(map(lambda y: rec(y, depth + 1), xs))

        return rec(nestedList)
