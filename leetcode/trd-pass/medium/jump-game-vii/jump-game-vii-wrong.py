class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        i, n = 0, len(s)
        while i < n:
            jumped = False
            for j in reversed(range(i + minJump, min(i + maxJump, n - 1) + 1)):
                if s[j] == '1':
                    continue
                elif j == n - 1:
                    return True
                else:
                    i = j
                    jumped = True
                    break
            if not jumped:
                return False
        return False