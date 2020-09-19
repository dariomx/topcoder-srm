class Solution:
    def isLeap(self, year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def numberOfDays(self, Y: int, M: int) -> int:
        if M in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif M == 2:
            return 28 + int(self.isLeap(Y))
        else:
            return 30

