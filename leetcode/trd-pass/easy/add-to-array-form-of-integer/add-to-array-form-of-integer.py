class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        rem = K
        i = len(A) - 1
        ans = []
        while rem > 0 or i >= 0:
            if i < 0:
                q, r = divmod(rem, 10)
            else:
                q, r = divmod(A[i] + rem, 10)
            ans.append(r)
            rem = q
            i -= 1
        return ans[::-1]