from collections import deque

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = 0
        for dir, amount in shift:
            if dir == 0:
                left += amount
            else:
                left -= amount
        s = deque(s)
        while left != 0:
            if left > 0:
                s.append(s.popleft())
                left -= 1
            else:
                s.appendleft(s.pop())
                left += 1
        return ''.join(s)