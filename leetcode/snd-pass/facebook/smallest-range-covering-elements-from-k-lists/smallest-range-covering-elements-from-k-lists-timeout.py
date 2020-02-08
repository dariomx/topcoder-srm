from collections import defaultdict


class Solution:
    def isSmallerRange(self, r1, r2):
        a, b = r1
        c, d = r2
        return b - a < d - c or (a < c and b - a == d - c)

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        xis = sorted([(x, i) for i in range(k) for x in nums[i]])
        mem = defaultdict(lambda: [])
        for x, i in xis:
            mem[x].append(i)
        used, used_size = [0] * k, 0
        start, end = 0, -1
        ans = None

        def check_ans():
            nonlocal ans
            cur = xis[start][0], xis[end][0]
            if used_size == k and (
                    ans is None or self.isSmallerRange(cur, ans)):
                ans = cur

        total = 0
        for x, i in xis:
            for j in mem[x]:
                used[j] += 1
                if used[j] == 1:
                    used_size += 1
                total += 1
            end += 1
            check_ans()
            while used_size == k and total > k:
                for j in mem[xis[start][0]]:
                    used[j] -= 1
                    if used[j] == 0:
                        used_size -= 1
                    total -= 1
                start += 1
                check_ans()
        return ans
