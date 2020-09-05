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

    def yearToDays(self, year):
        days = 0
        for y in range(1970, year):
            days += 365
            if self.isLeap(y):
                days += 1
        return days

    def monthToDays(self, month):
        daysMon = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
        return sum(daysMon[m-1] for m in range(1, month))

    def adjustLeap(self, day, month, year):
        if self.isLeap(year) and (month, day) > (2, 29):
            return 1
        else:
            return 0

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayName = {0: "Thursday", 1: "Friday", 2: "Saturday", 3: "Sunday",
                   4: "Monday", 5: "Tuesday", 6: "Wednesday"}
        numDays = self.yearToDays(year) + \
                  self.monthToDays(month) + \
                  (day - 1) + \
                  self.adjustLeap(day, month, year)
        return dayName[numDays % 7]



