class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        evenS = sum(x for x in A if x % 2 == 0)
        ans = []
        for x, i in queries:
            if A[i] % 2 == 0:
                evenS -= A[i]
            A[i] += x
            if A[i] % 2 == 0:
                evenS += A[i]
            ans.append(evenS)
        return ans