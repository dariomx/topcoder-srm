class Solution:
    def selfDividingNumbers(self, left, right):
        ans = []
        for x in range(left, right + 1):
            is_self = True
            for d in map(int, str(x)):
                if d == 0 or x % d != 0:
                    is_self = False
                    break
            if is_self:
                ans.append(x)
        return ans

