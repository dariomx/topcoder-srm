from collections import defaultdict


class Solution:
    def leastBricks(self, wall):
        sum_cnt = defaultdict(lambda: 0)
        max_cnt = 0
        for row in wall:
            psum = 0
            for i in range(len(row) - 1):
                psum += row[i]
                sum_cnt[psum] += 1
                max_cnt = max(max_cnt, sum_cnt[psum])
        return len(wall) - max_cnt
