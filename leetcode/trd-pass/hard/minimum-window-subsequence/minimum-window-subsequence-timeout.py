class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n, m = len(S), len(T)
        last = [inf] * (n+1)
        @cache
        def rec(i, j):
            if j < 0:
                return 0
            elif i < 0 and j >= 0:
                return inf
            else:
                size = rec(i-1, j) + int(j < m-1)
                if S[i] == T[j]:
                    size = min(size, rec(i-1, j-1) + 1)
                    if j == m - 1 and size < inf:
                        last[size] = min(last[size], i)
                return size
        size = rec(n-1, m-1)
        if size < inf:
            end = last[size]
            return S[(end - size + 1):(end+1)]
        else:
            return ''