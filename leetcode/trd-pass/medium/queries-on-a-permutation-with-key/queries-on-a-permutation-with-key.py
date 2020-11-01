# lame, others used fenwick tree

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        n = len(queries)
        perm = deque(range(1, m + 1))
        ans = []
        for x in queries:
            j = perm.index(x)
            ans.append(j)
            del perm[j]
            perm.appendleft(x)
        return ans
