class Solution:
    def findCircleNum(self, M):
        def neighbors(i):
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    yield j

        def dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in to_visit:
                    continue
                to_visit.remove(node)
                for nei in neighbors(node):
                    stack.append(nei)

        # main
        ans = 0
        to_visit = set(range(len(M)))
        while to_visit:
            for start in to_visit:
                dfs(start)
                ans += 1
                break
        return ans
