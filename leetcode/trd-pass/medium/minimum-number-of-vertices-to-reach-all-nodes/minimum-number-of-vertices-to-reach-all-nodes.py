class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[
        int]:
        roots = [True] * n
        for _, v in edges:
            roots[v] = False
        return [i for i in range(n) if roots[i]]
