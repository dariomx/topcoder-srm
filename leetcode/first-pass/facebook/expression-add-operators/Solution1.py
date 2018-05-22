from itertools import product

class Solution:
    def addOperators(self, num, target):
        n = len(num)
        ans = []
        for perm in product(['*','','+','-'], repeat=n-1):
            exp = num[0]
            for i in range(1, n):
                exp += perm[i-1] + num[i]
            try:
                if eval(exp) == target:
                    ans.append(exp)
            except:
                None
        return ans

num = "1000000009"
target = 9
print(Solution().addOperators(num, target))