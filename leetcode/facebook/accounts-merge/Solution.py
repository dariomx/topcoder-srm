from collections import defaultdict


class Solution:
    def build_graph(self, accounts):
        pairs = defaultdict(lambda: set())
        for i in range(len(accounts)):
            name = accounts[i][0]
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                pairs[(name, email)].add(i)
        graph = defaultdict(lambda: set())
        for ids in pairs.values():
            for id in ids:
                graph[id].update(ids)
        return graph

    def dfs_scc(self, graph, start):
        stack = [start]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for sib in graph[node]:
                stack.append(sib)
        return visited

    def accountsMerge(self, accounts):
        graph = self.build_graph(accounts)
        visited = set()
        merged_accs = []
        for i in range(len(accounts)):
            name = accounts[i][0]
            emails = set()
            if i not in visited:
                scc = self.dfs_scc(graph, i)
                visited.update(scc)
                for j in scc:
                    for k in range(1, len(accounts[j])):
                        emails.add(accounts[j][k])
                merged_accs.append([name] + sorted(emails))
        return merged_accs
