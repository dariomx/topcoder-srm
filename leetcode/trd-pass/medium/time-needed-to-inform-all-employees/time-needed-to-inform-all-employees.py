class Solution:
    def buildGraph(self, manager):
        graph = defaultdict(list)
        for i, x in enumerate(manager):
            graph[x].append(i)
        return graph

    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        def rec(emp):
            return informTime[emp] + max((rec(sub) for sub in graph[emp]),
                                         default=0)

        graph = self.buildGraph(manager)
        return rec(headID)

