from collections import defaultdict


class Solution(object):
    def get_facts_vars(self, equations, values):
        facts = dict()
        vars = set()
        for (a, b), k in zip(equations, values):
            facts[(a, b)] = k
            facts[(b, a)] = 1.0 / k
            facts[(a, a)] = 1
            facts[(b, b)] = 1
            vars.add(a)
            vars.add(b)
        return facts, vars

    def build_graph(self, equations):
        graph = defaultdict(lambda: [])
        for a, b in equations:
            graph[a].append(b)
            graph[b].append(a)
        return graph

    def search_dfs(self, facts, graph, x, y):
        stack = [(x, 1)]
        visited = set()
        while stack:
            node, prod = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            facts[(x, node)] = prod
            facts[(node, x)] = 1.0 / prod
            if node == y:
                return prod
            for c in graph[node]:
                if (node, c) in facts:
                    stack.append((c, prod * facts[(node, c)]))
        return -1

    def answer_query(self, facts, vars, graph, query):
        x, y = query
        if x not in vars or y not in vars:
            return -1
        elif (x, y) in facts:
            return facts[(x, y)]
        else:
            return self.search_dfs(facts, graph, x, y)

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        facts, vars = self.get_facts_vars(equations, values)
        graph = self.build_graph(equations)
        ans_query = lambda q: self.answer_query(facts, vars, graph, q)
        return map(ans_query, queries)
