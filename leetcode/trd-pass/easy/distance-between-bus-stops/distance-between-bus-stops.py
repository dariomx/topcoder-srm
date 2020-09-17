# this was overkill cause we had a single src-dst query

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, dest: int) -> int:
        n = len(distance)
        psum = [0] * n
        psum[0] = distance[0]
        for i in range(1, n):
            psum[i] = psum[i-1] + distance[i]
        def subSum(i, j):
            if i > j:
                return 0
            else:
                return psum[j] - psum[i] + distance[i]
        if dest < start:
            start, dest = dest, start
        clockwise = subSum(dest, n-1) + subSum(0, start-1)
        counterwise = subSum(start, dest-1)
        return min(clockwise, counterwise)
