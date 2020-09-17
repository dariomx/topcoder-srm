# this is improved version, after realizing in phorum that i just had
# a single query (my prefix sum array was nice but better for multiple
# queries scenario)

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                dest: int) -> int:
        n = len(distance)
        totd = 0
        dist = 0
        if dest < start:
            start, dest = dest, start
        for i in range(n):
            totd += distance[i]
            if start <= i < dest:
                dist += distance[i]
        return min(totd - dist, dist)
