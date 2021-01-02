class Solution:
    def buildGraph(self, head):
        graph = defaultdict(list)
        node = head
        prev = None
        while node:
            if prev:
                graph[node.val].append(prev.val)
                graph[prev.val].append(node.val)
            prev = node
            node = node.next
        return graph

    def dfs(self, graph, start, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for child in graph[node]:
                stack.append(child)

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        graph = self.buildGraph(head)
        visited = graph.keys() - set(G)
        ans = 0
        for x in G:
            if x in visited:
                continue
            else:
                self.dfs(graph, x, visited)
                ans += 1
        return ans
