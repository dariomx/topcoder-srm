class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        busy = None
        for i in range(n):
            if seats[i] == 0:
                if busy is not None:
                    seats[i] = -abs(i - busy)
            else:
                busy = i
        busy = None
        ans = 0
        for i in reversed(range(n)):
            if seats[i] <= 0:
                if busy is None:
                    seats[i] *= -1
                elif seats[i] == 0:
                    seats[i] = abs(i - busy)
                else:
                    seats[i] = min(-seats[i], abs(i - busy))
                ans = max(ans, seats[i])
            else:
                busy = i
        return ans
