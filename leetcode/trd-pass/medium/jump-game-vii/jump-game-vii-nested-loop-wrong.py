class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                continue
            for j in reversed(range(i + minJump, min(i + maxJump, n - 1) + 1)):
                if s[j] == '1':
                    continue
                elif j == n - 1:
                    return True
        return False                                
                