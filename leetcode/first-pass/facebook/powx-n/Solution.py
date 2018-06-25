class Solution:
    def myPow(self, x, n):
        def pow(x, k):
            if k == 0:
                return 1
            elif k == 1:
                return x
            else:
                pow_k = pow(x, k // 2)
                pow_k = pow_k * pow_k
                if k % 2 == 1:
                    pow_k *= x
                print(pow_k)
                return pow_k

        if n < 0:
            x = 1 / x
        return pow(x, abs(n))

x = 8.84372
n = -5
print(Solution().myPow(x, n))