# Should have removed dups before sorting, like guys on phorum?

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict()
        prev = None
        for x in sorted(arr) + [None]:
            if x == prev:
                continue
            else:
                if prev is not None:
                    rank[prev] = len(rank) + 1
                prev = x
        return [rank[x] for x in arr]


