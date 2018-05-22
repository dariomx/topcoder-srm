from collections import deque

class Solution:
    def averageOfLevels(self, root):
        queue = deque([(root, 0)])
        prev_lev = -1
        sum_lev = 0
        cnt_lev = 0
        avg_lev = []
        while queue:
            node, lev = queue.popleft()
            if lev != prev_lev:
                if cnt_lev > 0:
                    avg_lev.append(sum_lev / cnt_lev)
                sum_lev = 0
                cnt_lev = 0
                prev_lev = lev
            sum_lev += node.val
            cnt_lev += 1
            for child in ((node.left, node.right)):
                if child:
                    queue.append((child, lev+1))
        avg_lev.append(sum_lev / cnt_lev)
        return avg_lev