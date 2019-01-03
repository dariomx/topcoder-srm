class Solution:
    def totalFruit(self, tree):
        if not tree:
            return 0
        n = len(tree)
        start = 0
        cnt = [0] * n
        cnt[tree[start]] = 1
        nf = 1
        ans = 1
        for end in range(1, n):
            cnt[tree[end]] += 1
            if cnt[tree[end]] == 1:
                nf += 1
            while nf > 2:
                k = tree[start]
                cnt[k] -= 1
                if cnt[k] == 0:
                    nf -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans