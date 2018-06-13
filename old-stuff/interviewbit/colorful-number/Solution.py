class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = list(map(int, str(A)))
        n = len(A)
        prod = [1] * n
        prod[0] = A[0]
        for i in range(1, n):
            prod[i] = prod[i - 1] * A[i]
        sub_prod = lambda i, j: prod[j] / prod[i] * A[i]
        diff_prod = set()
        for i in range(n):
            for j in range(i, n):
                p = sub_prod(i, j)
                if diff_prod and p in diff_prod:
                    return 0
                diff_prod.add(p)
        return 1
