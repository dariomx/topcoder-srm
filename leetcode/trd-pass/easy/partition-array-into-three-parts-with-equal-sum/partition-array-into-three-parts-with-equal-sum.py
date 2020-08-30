class Solution:
    def canTwoPartsEqualSum(self, A, S):
        psum = 0
        for i, x in enumerate(A):
            psum += x
            if 2 * psum == S and i < len(A) - 1:
                return True
        return False

    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        S = sum(A)
        psum = 0
        for i, x in enumerate(A):
            psum += x
            if 3 * psum == S and self.canTwoPartsEqualSum(A[i + 1:], S - psum):
                return True
        return False

