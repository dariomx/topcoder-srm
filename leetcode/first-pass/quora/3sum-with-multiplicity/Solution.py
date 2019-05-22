MOD = 10**9 + 7

class Solution:
    def threeSumMulti(self, A, target):
        comb2 = lambda x: x*(x-1) // 2
        A.sort()
        n = len(A)
        ans = 0
        for i in range(n-2):
            j = i + 1
            k = n - 1
            s = A[i] + A[j] + A[k]
            while j < k:
                if s == target:
                    fact_j = fact_k = 1
                    while j+1 < k and A[j] == A[j+1]:
                        fact_j += 1
                        j += 1
                    while j < k-1 and A[k-1] == A[k]:
                        fact_k += 1
                        k -= 1
                    if j+1 == k and A[j] == A[k]:
                        ans += comb2(fact_j + fact_k)
                    else:
                        ans += fact_j * fact_k
                    ans %= MOD
                if s <= target:
                    s += A[j+1] - A[j]
                    j += 1
                else:
                    s += A[k-1] - A[k]
                    k -= 1
        return ans