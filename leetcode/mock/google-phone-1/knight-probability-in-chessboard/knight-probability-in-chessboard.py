class Solution:
    def __init__(self):
        self.moves = [(+1, +2), (+1, -2), (-1, +2), (-1, -2),
                      (+2, +1), (+2, -1), (-2, +1), (-2, -1)]
        self.cache = dict()
        self.leaf_prob = None

    def _search(self, N: int, K: int, r: int, c: int, moves: int) -> float:
        key = (r, c, moves)
        if key in self.cache:
            return self.cache[key]
        elif moves == K:
            return self.leaf_prob
        prob = 0
        for dr, dc in self.moves:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            prob += self._search(N, K, nr, nc, moves + 1)
        self.cache[key] = prob
        return prob

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        self.cache.clear()
        self.leaf_prob = (1 / 8.) ** K
        return self._search(N, K, r, c, 0)
