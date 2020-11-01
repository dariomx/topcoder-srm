class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i, j in zip(l, r):
            sub = nums[i:(j+1)]
            heapify(sub)
            sndLast = heappop(sub)
            last = heappop(sub)
            diff = last - sndLast
            ans.append(True)
            while sub:
                sndLast = last
                last = heappop(sub)
                if last - sndLast != diff:
                    ans[-1] = False
                    break
        return ans