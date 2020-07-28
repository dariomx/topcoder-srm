class Solution(object):
    def days_month(self, y, m):
        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        d = days[m]
        if y % 4 == 0 and m == 2:
            d += 1
        return d

    # taken from wikipedia, did not know all cases
    def days_year(self, y):
        if y % 4 != 0:
            return 365
        elif y % 100 != 0:
            return 366
        elif y % 400 != 0:
            return 365
        else:
            return 366

    def epoch_days(self, date, ini_year=1971):
        ndays = 0
        year, month, day = map(int, date.split('-'))
        for y in range(ini_year, year):
            ndays += self.days_year(y)
        for m in range(1, month):
            ndays += self.days_month(year, m)
        ndays += day
        print((date, ndays))
        return ndays

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.epoch_days(date1) - self.epoch_days(date2))
