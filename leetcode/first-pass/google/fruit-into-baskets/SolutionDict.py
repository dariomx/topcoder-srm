from collections import OrderedDict


class Solution(object):
    def totalFruit(self, tree):
        k = 2
        n = len(tree)
        last = OrderedDict()
        ans = 0
        cnt = 0
        for i in range(n):
            fruit = tree[i]
            # Simulate an insert cause OrderedDict does not support upd
            if fruit in last:
                del last[fruit]
            last[fruit] = i
            cnt += 1
            if len(last) > k:
                cnt = i - last.popitem(last=False)[1]
            ans = max(ans, cnt)
        return ans

