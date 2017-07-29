from collections import deque


class Solution(object):
    def removeDup(self, arr):
        ret = []
        prev = arr[0]
        for i in xrange(1, len(arr)):
            x = arr[i]
            if x != prev:
                ret.append(prev)
                prev = x
        ret.append(prev)
        return ret

    def merge(self, points):
        ret = []
        px, py = points[0]
        for x, y in points[1:]:
            if y != py:
                ret.append([px, py])
                px, py = x, y
        ret.append([px, py])
        return ret

    def intersect(self, b1, b2, visible, pend, hidden):
        left1, right1, height1 = b1
        left2, right2, height2 = b2
        if right1 < left2:
            visible.append((left1, height1))
            visible.append((right1, 0))
            pend.append((left2, height2))
            pend.append((right2, 0))
        elif right2 <= right1:
            if height1 > height2:
                visible.append((left1, height1))
                pend.append((right1, 0))
                hidden.add((left2, height2))
                hidden.add((right2, height2))
            else:
                if left1 < left2:
                    visible.append((left1, height1))
                else:
                    hidden.add((left1, height1))
                pend.append((left2, height2))
                pend.append((right2, height2))
                pend.append((right1, 0))
        else:
            if height2 < height1:
                visible.append((left1, height1))
                pend.append((right1, height2))
                pend.append((right2, 0))
                hidden.add((left2, height2))
            else:
                visible.append((left1, height1))
                pend.append((left2, height2))
                pend.append((right2, 0))
                hidden.add((right1, height1))

    def removeHidden(self, visible, hidden):
        ret = []
        for x in visible:
            if x not in hidden:
                ret.append(x)
        return ret

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(buildings)
        if n == 0:
            return []
        buildings = self.removeDup(buildings)
        n = len(buildings)
        if n == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]
        visible, pend = deque(), deque()
        hidden = set()
        self.intersect(buildings[0], buildings[1], visible, pend, hidden)
        for i in xrange(2, n):
            newPend = deque()
            left, right, height = buildings[i]
            while pend:
                x, y = pend.popleft()
                if x < left:
                    visible.append((x, y))
                elif left <= x <= right and y <= height:
                    None
                else:
                    newPend.append((x, y))
            pend = newPend
            self.intersect(buildings[i - 1], buildings[i], visible, pend, hidden)
        visible.extend(pend)
        visible = self.removeHidden(visible, hidden)
        return self.merge(self.removeDup(visible))

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[1,2,1],[1,2,2],[1,2,3]]
buildings = [[1,5,3], [1,5,3], [1,5,3]]
print(Solution().getSkyline(buildings))