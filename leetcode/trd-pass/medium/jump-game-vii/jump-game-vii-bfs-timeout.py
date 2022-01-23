class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque([0])
        while queue:
            i = queue.popleft()
            if i == len(s) - 1:
                return True
            for j in range(i + minJump, min(i + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    queue.append(j)
        return False