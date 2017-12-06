from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, t):
        n = len(nums)
        if n == 0:
            return 0
        psum = [0] * n
        psum[0] = nums[0]
        for i in xrange(1, n):
            psum[i] = psum[i-1] + nums[i]
        subsum = lambda i,j: psum[j] - (psum[i-1] if i > 0 else 0)
        cnt = defaultdict(lambda: 0)
        stack = [(0,n-1)]
        while stack:
            i, j = stack.pop()
            if subsum(i, j) == t:
                max_i = i-1
                cnt_i = 0
                for k in xrange(i, j+1):
                    if subsum(i, k) == 0:
                        max_i = k
                        cnt_i += 1
                if cnt_i == 0:
                    cnt_i = 1
                cnt_j = 0
                for k in xrange(j, max_i, -1):
                    if subsum(k, j) == 0:
                        cnt_j += 1
                if cnt_j == 0:
                    cnt_j = 1
                cnt[(i, j)] = cnt_i * cnt_j
            else:
                if i+1 <= j and (i+1, j) not in cnt:
                    stack.append((i+1, j))
                if i <= j-1 and (i, j-1) not in cnt:
                    stack.append((i, j-1))
        return sum(cnt.itervalues())

nums = [1,2,3,4,5,6,7,1,23,21,3,1,2,1,1,1,1,1,12,2,3,2,3,2,2]
t = 6
print(Solution().subarraySum(nums, t))