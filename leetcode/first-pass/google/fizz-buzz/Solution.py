class Solution:
    def fizzBuzz(self, n):
        ans = []
        for x in range(1, n+1):
            mul3 = x % 3 == 0
            mul5 = x % 5 == 0
            if mul3 and mul5:
                s = "FizzBuzz"
            elif mul3:
                s = "Fizz"
            elif mul5:
                s = "Buzz"
            else:
                s = str(x)
            ans.append(s)
        return ans