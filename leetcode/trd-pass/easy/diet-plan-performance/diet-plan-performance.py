class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T = 0
        cnt = 0
        ans = 0
        for i in range(len(calories)):
            cnt += 1
            T += calories[i]
            if cnt > k:
                T -= calories[i-k]
                cnt -= 1
            if cnt == k:
                if T < lower:
                    ans -= 1
                elif T > upper:
                    ans += 1
        return ans