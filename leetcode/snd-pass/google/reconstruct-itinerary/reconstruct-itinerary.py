class Solution:
    def getCityDicts(self, tickets):
        cities = set()
        for src, dst in tickets:
            for c in (src, dst):
                cities.add(c)
        idx = {c: i for (i, c) in enumerate(sorted(cities))}
        name = {i: c for (c, i) in idx.items()}
        return idx, name

    def getAdjMatrix(self, tickets, cityIdx):
        n = len(cityIdx)
        adj = [[0] * n for _ in range(n)]
        size = 0
        for src, dst in tickets:
            i, j = cityIdx[src], cityIdx[dst]
            adj[i][j] += 1
            size += 1
        return adj, size

    def search(self, adj, path, size):
        if size == 0:
            self.ans = path
            raise ValueError()
        i = path[-1]
        for j in range(len(adj)):
            if adj[i][j] > 0:
                adj[i][j] -= 1
                self.search(adj, path + [j], size - 1)
                adj[i][j] += 1

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        cityIdx, cityName = self.getCityDicts(tickets)
        adj, size = self.getAdjMatrix(tickets, cityIdx)
        try:
            self.search(adj, [cityIdx['JFK']], size)
        except ValueError:
            return list(map(cityName.__getitem__, self.ans))
