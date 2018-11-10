from math import inf

class Solution(object):
    def findRestaurant(self, list1, list2):
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        idx1 = {x:i for (i,x) in enumerate(list1)}
        min_isum = inf
        ans = []
        for i in range(len(list2)):
            r2 = list2[i]
            if r2 in idx1:
                isum = i + idx1[r2]
                if isum < min_isum:
                    min_isum = isum
                    ans = [r2]
                elif isum == min_isum:
                    ans.append(r2)
        return ans