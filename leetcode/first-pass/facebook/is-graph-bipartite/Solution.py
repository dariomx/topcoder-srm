class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        conn = set()
        for i in range(n):
            if graph[i]:
                conn.add(i)
        nconn = len(conn)
        if nconn == 0:
            return True
        visited = set()
        left = set()
        right = set()
        while conn:
            start = conn.pop()
            stack = [(start, True)]
            while stack:
                node, is_left = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                if node in conn:
                    conn.remove(node)
                if is_left:
                    left.add(node)
                else:
                    right.add(node)
                for child in graph[node]:
                    stack.append((child, not is_left))
        if len(visited) != nconn:
            return False
        if left & right:
            return False
        for i in range(n):
            for j in graph[i]:
                if i in left and j in left:
                    return False
                if i in right and j in right:
                    return False
        return True
