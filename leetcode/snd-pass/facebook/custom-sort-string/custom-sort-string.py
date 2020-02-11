class Solution:
    def customSortString(self, S: str, T: str) -> str:
        order = dict(((c, i) for (i, c) in enumerate(S)))
        return ''.join(sorted(T, key=lambda c: order.get(c, -1)))
