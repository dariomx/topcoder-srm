class Solution(object):
    def dfs_search(self, n, adj, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for i in xrange(n):
                if adj[node][i] == 1:
                    stack.append(i)
        return visited

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        adj = [[0 for _ in xrange(n)] for _ in xrange(n)]
        has_one = False
        for i in xrange(n):
            for j in xrange(n):
                x = nums[i]
                y = nums[j]
                if 1 in (x, y):
                    has_one = True
                elif x % y == 0 or y % x == 0:
                    adj[i][j] = 1
                    adj[j][i] = 1
        visited = set()
        max_island = set()
        for i in xrange(n):
            if nums[i] == 1 or i in visited:
                continue
            island = self.dfs_search(n, adj, i)
            if len(island) > len(max_island):
                max_island = island
            visited |= island
        ret = [nums[i] for i in max_island]
        if has_one:
            ret.append(1)
        return ret
