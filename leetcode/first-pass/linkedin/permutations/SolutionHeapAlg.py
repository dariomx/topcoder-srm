class Solution(object):
    def permute(self, nums):
        ans = []

        def heap_perm(n, A):
            if n <= 1:
                ans.append(list(A))
            else:
                for i in range(n - 1):
                    heap_perm(n - 1, A)
                    j = i if (n % 2 == 0) else 0
                    A[j], A[n - 1] = A[n - 1], A[j]
                heap_perm(n - 1, A)

        heap_perm(len(nums), nums)
        return ans


