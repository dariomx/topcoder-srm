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
            if (left1, height1) not in hidden:
                visible.append((left1, height1))
            if (right1, 0) not in hidden:
                visible.append((right1, 0))
            pend.append((left2, height2))
            pend.append((right2, 0))
        elif right2 <= right1:
            if height1 > height2:
                if (left1, height1) not in hidden:
                    visible.append((left1, height1))
                pend.append((right1, 0))
                hidden.add((left2, height2))
                hidden.add((right2, height2))
            else:
                if (left1, height1) not in hidden:
                    visible.append((left1, height1))
                pend.append((left2, height2))
                pend.append((right2, height2))
                pend.append((right1, 0))
        else:
            if height2 < height1:
                if (left1, height1) not in hidden:
                    visible.append((left1, height1))
                pend.append((right1, height2))
                pend.append((right2, 0))
                hidden.add((left2, height2))
            else:
                if (left1, height1) not in hidden:
                    visible.append((left1, height1))
                pend.append((left2, height2))
                pend.append((right2, 0))
                hidden.add((right1, height1))

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(buildings)
        if n == 0:
            return []
        elif n == 1:
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
            self.intersect(buildings[i - 1], buildings[i], visible, pend,
                           hidden)
        visible.extend(pend)
        return self.merge(self.removeDup(visible))
