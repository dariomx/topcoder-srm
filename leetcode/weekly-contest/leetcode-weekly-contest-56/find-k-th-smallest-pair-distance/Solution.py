class Solution(object):
    def fetch(self, ini_d, seq, used, dist, k, kth_d):
        d = ini_d
        for i in seq:
            if used[i]:
                k -= 1
                d += dist[i]
                print(d)
                kth_d = max(kth_d, d)
                if k == 0:
                    break
            else:
                break
        return k, kth_d

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        dist = [0] * (n - 1)
        for i in xrange(0, n - 1):
            dist[i] = nums[i + 1] - nums[i]
        idx_d = range(n - 1)
        idx_d.sort(key=lambda i: dist[i])
        kth_d = 0
        used = [False] * (n - 1)
        print(nums)
        print(dist)
        print(idx_d)
        for i in idx_d:
            used[i] = True
            k, kth_d = self.fetch(0, xrange(i, -1, -1), used, dist, k, kth_d)
            if k == 0:
                return kth_d
            k, kth_d = self.fetch(dist[i], xrange(i + 1, n - 1), used, dist, k, kth_d)
            if k == 0:
                return kth_d