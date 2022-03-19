class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def doneTasks(t):
            cnt = 0
            for dur in time:
                cnt += t // dur
            return cnt
        
        start, end = 1, totalTrips * min(time) 
        ans = None
        while start <= end:
            mid = (start + end) // 2
            if doneTasks(mid) >= totalTrips:      
                ans = mid
                end = mid - 1
            else:
                if ans is None:
                    ans = mid
                start = mid + 1
        return ans
