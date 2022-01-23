class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        zeros = deque([i for i in range(n) if s[i] == '0'])
        queue = deque([zeros.popleft()])
        while queue:
            i = queue.popleft()
            if i == n - 1:
                return True
            while zeros and  (i + minJump) > zeros[0]:
                zeros.popleft()
            while zeros and (i + minJump) <= zeros[0] <= min(i + maxJump, n - 1):
                queue.append(zeros.popleft())
        return False