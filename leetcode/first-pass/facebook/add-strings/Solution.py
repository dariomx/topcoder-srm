class Solution:
    def addStrings(self, num1, num2):
        n1 = len(num1)
        n2 = len(num2)
        if n2 > n1:
            num1, num2 = num2, num1
            n1, n2 = n2, n1
        rem = 0
        ans = ""
        for i in range(n1):
            x = int(num1[n1 - 1 - i])
            y = int(num2[n2 - 1 - i]) if i < n2 else 0
            tmp = rem + x + y
            ans = str(tmp % 10) + ans
            rem = tmp // 10
        if rem > 0:
            ans = str(rem) + ans
        return ans
