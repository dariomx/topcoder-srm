class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        aseq = dict()
        start, end = 0, 1
        aseq[start] = end
        step = A[end] - A[start]
        end += 1
        while end < n:
            if A[end] - A[end-1] == step:
                aseq[start] = end
                end += 1
            elif end < n-1:
                start = end
                end += 1
                aseq[start] = end
                step = A[end] - A[start]
                end += 1
            else:
                break
        ans = 0
        for start, end in aseq.items():
            size = end - start + 1
            if size >= 3:
                ans += (size-2) * (size-1) // 2
        return ans