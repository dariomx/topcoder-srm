class Solution(object):
    def merge(self, left, right):
        merged = []
        n, m = len(left), len(right)
        i, j = 0, 0
        while i < n or j < m:
            if j == m or (i < n and left[i] < right[j]):
                merged.append(left[i])
                i += 1
            elif i == n or (j < m and left[i] > right[j]):
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
                merged.append(right[j])
                j += 1
        return merged

    def handle_parabola(self, nums, a, b, c):
        vx = -b / float(2 * a)
        f = lambda x: a * x ** 2 + b * x + c
        left, right = [], []
        for x in nums:
            if x < vx:
                left.append(x)
            else:
                right.append(x)
        if a > 0:
            left = reversed(left)
        else:
            right = reversed(right)
        left = map(f, left)
        right = map(f, right)
        return self.merge(left, right)

    def handle_line(self, nums, b, c):
        f = lambda x: b * x + c
        if b < 0:
            nums = reversed(nums)
        return map(f, nums)

    def handle_cte(self, nums, c):
        f = lambda x: c
        return map(f, nums)

    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if a != 0:
            return self.handle_parabola(nums, a, b, c)
        elif b != 0:
            return self.handle_line(nums, b, c)
        else:
            return self.handle_cte(nums, c)


nums = [-99, -94, -90, -88, -84, -83, -79, -68, -58, -52, -52, -50, -47, -45,
        -35, -29, -5, -1, 9, 12, 13, 25, 27, 33, 36, 38, 40, 46, 47, 49, 57, 57,
        61, 63, 73, 75, 79, 97, 98]
a, b, c = -2, 44, -56
print(Solution().sortTransformedArray(nums, a, b, c))
