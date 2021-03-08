class Solution:
    def offsetIdx(self, i, size):
        return size - 1 - i

    def encodeIdx(self, i, size):
        return 1 << self.offsetIdx(i, size)

    def encodeSkills(self, skills: list[str], sidx: dict[str, int]) -> int:
        enc = 0
        for s in skills:
            i = sidx[s]
            enc |= self.encodeIdx(i, len(sidx))
        return enc

    def bitIterator(self, word, size):
        for i in range(size):
            offset = self.offsetIdx(i, size)
            if (word & (1 << offset)) >> offset == 1:
                yield i

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(people), len(req_skills)
        sidx = {s:i for (i, s) in enumerate(req_skills)}
        pskill = {p:self.encodeSkills(people[p], sidx) for p in range(n)}
        people = (1 << n) - 1
        queue = deque([(pskill[p], self.encodeIdx(p, n)) for p in range(n) if pskill[p] > 0])
        visited = {node for (node, _) in queue}
        start, end = 0, (1 << m) - 1
        while queue:
            node, team = queue.popleft()
            if node == end:
                return list(self.bitIterator(team, size=n))
            for p in self.bitIterator(people & ~team, size=n):
                child = node | pskill[p]
                if child in visited:
                    continue
                visited.add(child)
                queue.append((child, team | self.encodeIdx(p, n)))
