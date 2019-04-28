class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def dfs(node, path):
            if node == n - 1:
                ans.append(list(path))
            else:
                for child in graph[node]:
                    path.append(child)
                    dfs(child, path)
                    path.pop()

        dfs(0, [0])
        return ans
