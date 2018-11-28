from math import sqrt

class Solution:
    def checkPerfectNumber(self, num):
        if num < 2:
            return False
        sumd = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num%i == 0:
                sumd += i
                sumd += num // i
                if sumd > num:
                    return False
        return num == sumd