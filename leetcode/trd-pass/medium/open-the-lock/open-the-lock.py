class Solution:
    def bfs(self, start, target, deadends):
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            node, dist = queue.popleft()
            if node in deadends:
                continue
            elif node == target:
                return dist
            for i, d in enumerate(node):
                for inc in (-1, +1):
                    child = node[:i] + str((int(d) + inc) % 10) + node[i + 1:]
                    if child not in visited:
                        queue.append((child, dist + 1))
                        visited.add(child)
        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        return self.bfs('0000', target, set(deadends))

