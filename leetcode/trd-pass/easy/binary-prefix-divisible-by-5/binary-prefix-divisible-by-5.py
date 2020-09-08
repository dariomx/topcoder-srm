# Horner's rule would had allowed to do a single pass, # fail
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        n = len(A)
        numA = sum(A[i] * (1 << n-1-i) for i in range(n))
        ans = [0] * n
        for i in reversed(range(n)):
            ans[i] = (numA % 5 == 0)
            numA -= A[i] * (1 << (n-1-i))
        return ans