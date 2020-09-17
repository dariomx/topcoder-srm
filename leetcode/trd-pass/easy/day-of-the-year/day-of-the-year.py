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

    def daysMonth(self, month, year):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month == 2:
            return 28 + int(self.isLeap(year))
        else:
            return 30

    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        ans = day
        for m in range(1, month):
            ans += self.daysMonth(m, year)
        return ans