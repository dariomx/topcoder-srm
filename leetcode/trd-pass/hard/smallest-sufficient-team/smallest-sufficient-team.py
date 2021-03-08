class Solution:
    def encodePerson(self, person: list[str], idx: dict[str, int]) -> int:
        enc = 0
        for skill in person:
            i = idx[skill]
            enc |= 1 << i
        return enc

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        idx = {s:i for (i, s) in enumerate(req_skills)}
        n = len(people)
        pskill = {p:self.encodePerson(people[p], idx) for p in range(n)}
        people = set(range(n))
        start, end = 0, (1 << len(req_skills)) - 1
        queue = deque([(start, set())])
        visited = {start}
        while queue:
            node, team = queue.popleft()
            if node == end:
                return team
            for p in people - team:
                child = node | pskill[p]
                if child in visited:
                    continue
                visited.add(child)
                queue.append((child, team | {p}))




