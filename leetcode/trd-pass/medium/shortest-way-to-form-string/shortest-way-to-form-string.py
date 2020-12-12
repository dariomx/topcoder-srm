class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        n, m = len(source), len(target)
        i, j = 0, 0
        ans = 1
        chars_src = set(source)
        while j < m:
            if target[j] not in chars_src:
                break
            elif source[i] == target[j]:
                j += 1
                if j == m:
                    return ans
            if i < n - 1:
                i += 1
            else:
                ans += 1
                i = 0
        return -1
