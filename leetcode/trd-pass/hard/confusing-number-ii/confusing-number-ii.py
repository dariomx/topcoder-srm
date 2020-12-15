# can't believe this was just backtracking

class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = [0, 1, 6, 8, 9]
        ans = 0
        def rotate(x):
            rx = ''
            for d in str(x):
                if d == '6':
                    rx += '9'
                elif d == '9':
                    rx += '6'
                else:
                    rx += d
            return int(rx[::-1])
        def confusing(x):
            return rotate(x) != x
        def rec(x):
            nonlocal ans
            if x > N:
                None
            else:
                if confusing(x):
                    ans += 1
                for d in valid:
                    nx = x*10 + d
                    if nx != x:
                        rec(nx)
        rec(0)
        return ans