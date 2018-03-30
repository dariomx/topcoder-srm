from sys import maxsize as maxint


class Solution:
    def threeSum(self, nums):
        def calc_key(x, y, z):
            nonlocal base
            arr = sorted((x, y, z))
            key = 0
            for i in range(2):
                key += (base ** i) * arr[i]
            return key

        def search_triples(sum1):
            nonlocal n
            triples = []
            used = dict()
            for i in range(n):
                y = nums[i]
                for j in range(i + 1, n):
                    z = nums[j]
                    x = -(y + z)
                    if x in sum1:
                        k = sum1[x]
                        if k == i or k == j:
                            continue
                        key = calc_key(x, y, z)
                        if key not in used:
                            used[key] = True
                            triples.append((x, y, z))
            return triples

        n = len(nums)
        sum1 = dict()
        minn, maxn = maxint, -maxint
        zeros = 0
        for i in range(n):
            sum1[nums[i]] = i
            minn = min(minn, nums[i])
            maxn = max(maxn, nums[i])
            if nums[i] == 0:
                zeros += 1
        if zeros >= 3 and zeros == n:
            return [[0, 0, 0]]
        base = maxn - minn + 1
        return search_triples(sum1)

