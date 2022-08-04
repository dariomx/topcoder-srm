# this version cheats cause i saw the editorial soln: sorting eliminates the need to check
# both 2*x and x//2 possibilities. 

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        def remove(x: int) -> None:
            nonlocal cnt
            cnt[x] -= 1
            if cnt[x] == 0:
                del cnt[x]
                
        cnt = Counter(changed)
        ans = []
        heapify(changed)
        while changed:
            x = heappop(changed)
            dx = 2 * x            
            if x not in cnt:
                continue
            elif x == 0:
                if cnt[x] >= 2:
                    remove(0)
                    remove(0)
                    ans.append(0)
                    continue
                else:
                    break            
            elif dx in cnt:
                remove(x)
                remove(dx)
                ans.append(x)                
            else:
                break
        
        return ans if len(cnt) == 0 else []
    
