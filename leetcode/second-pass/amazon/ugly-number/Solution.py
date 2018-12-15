class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False
        div = [2, 3, 5]
        while num > 1:
            ugly = False
            for d in div:
                q, r = divmod(num, d)
                if r == 0:
                    num = q
                    ugly = True
                    break
            if not ugly:
                return False
        return True