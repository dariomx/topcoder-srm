class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = 0
        changed = False
        for d in map(int, str(num)):
            if not changed and d == 6:
                d = 9
                changed = True
            ans = ans * 10 + d
        return ans