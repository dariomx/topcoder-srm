from collections import deque


class Solution:
    def averageOfLevels(self, root):
        queue = deque([(root, 0)])
        lev_sum = 0
        lev_cnt = 0
        prev_lev = 0
        ans = []
        while queue:
            node, lev = queue.popleft()
            if lev != prev_lev:
                ans.append(lev_sum / lev_cnt)
                lev_sum = 0
                lev_cnt = 0
                prev_lev = lev
            lev_sum += node.val
            lev_cnt += 1
            if node.left:
                queue.append((node.left, lev + 1))
            if node.right:
                queue.append((node.right, lev + 1))
        ans.append(lev_sum / lev_cnt)
        return ans

