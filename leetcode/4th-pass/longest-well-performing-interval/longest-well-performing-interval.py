from sortedcontainers import SortedKeyList

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        bitarr = [int(h > 8) for h in hours]
        slist = SortedKeyList(key=lambda t: t[0])
        psum = 0
        ans = 0
        
        print(bitarr)
        
        for i, x in enumerate(bitarr):
            psum += x
            score_i = 2*psum - (i+1)
            if score_i > 0:
                ans = max(ans, i + 1)
            else:
                for _, j in slist.irange_key(max_key=score_i, inclusive=(False,False)):
                    ans = max(ans, i - j)
            slist.add((score_i, i))
            
        return ans

