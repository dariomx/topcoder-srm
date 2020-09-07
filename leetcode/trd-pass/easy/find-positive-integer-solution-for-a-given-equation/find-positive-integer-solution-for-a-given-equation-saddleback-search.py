"""
Not mine, got it from the phorum; kinda recall having made this
exercice in the masters once, but forgot about formulating it
as a sorted matrix. lame. pathetic. die-soon.
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        n = 1000
        f = customfunction.f
        x, y = n, 1
        while 1 <= x <= n and 1 <= y <= n:
            fxy = f(x, y)
            if z < fxy:
                x -= 1
            else:
                if z == fxy:
                    ans.append((x, y))
                y += 1
        return ans