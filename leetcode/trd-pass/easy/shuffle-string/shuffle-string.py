# this is the trivial one using O(n) space, but saw other in phorum used cyclic sort? let me see

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ans = [None] * n
        for i, j in enumerate(indices):
            ans[j] = s[i]
        return ''.join(ans)