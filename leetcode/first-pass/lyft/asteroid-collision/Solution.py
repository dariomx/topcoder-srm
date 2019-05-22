class Solution:
    def asteroidCollision(self, asteroids):
        ans = []
        pos = []
        for x in asteroids:
            if x < 0:
                while pos and abs(pos[-1]) < abs(x):
                    pos.pop()
                if not pos:
                    ans.append(x)
                elif abs(pos[-1]) == abs(x):
                    pos.pop()
            else:
                pos.append(x)
        ans += pos
        return ans
