# this passes all the tests but, I am not sure if just sorting removes the need to do backtracking.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        def remove(x: int) -> None:
            nonlocal cnt
            cnt[x] -= 1
            if cnt[x] == 0:
                del cnt[x]
                
        cnt = Counter(changed)
        ans = []
        for x in sorted(changed):
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
                    
            dx = 2 * x
            hx, px = divmod(x, 2)
            if px == 0 and hx in cnt:
                remove(hx)
                remove(x)
                ans.append(hx)
            elif dx in cnt:
                remove(x)
                remove(dx)
                ans.append(x)                
            else:
                break
        
        return ans if len(cnt) == 0 else []
    
