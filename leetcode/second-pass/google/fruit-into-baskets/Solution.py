from collections import defaultdict

class Solution:
    def totalFruit(self, tree):
        if not tree:
            return 0
        start = 0
        ftypes = defaultdict(lambda: 0)
        ftypes[tree[start]] = 1
        ans = 1
        for end in range(1, len(tree)):
            ftypes[tree[end]] += 1
            while len(ftypes) > 2:
                k = tree[start]
                ftypes[k] -= 1
                if ftypes[k] == 0:
                    del ftypes[k]
                start += 1
            ans = max(ans, end - start + 1)
        return ans