from collections import deque


class Solution(object):
    def findPermutation(self, sign):
        """
        :type s: str
        :rtype: List[int]
        """
        decr = deque()
        order = deque(range(1, len(sign) + 2))
        perm = deque()
        x = order.popleft()
        if sign[0] == 'D':
            decr.appendleft(x)
        else:
            perm.append(x)
        for s in sign:
            x = order.popleft()
            if s == 'D':
                if not decr:
                    decr.appendleft(perm.pop())
                decr.appendleft(x)
            else:
                perm.extend(decr)
                decr.clear()
                perm.append(x)
        perm.extend(decr)
        return list(perm)
