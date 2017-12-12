class GForce:
    def eqErr(self, a, b):
        return abs(a - b) < 1e-7

    def interpolY(self, x1, y1, x2, y2, x3):
        m = (y2 - y1) / float(x2 - x1)
        y3 = m*(x3 - x1) + y1
        return x3, y3

    def interpolX(self, x1, y1, x2, y2, y3):
        mp = (x2 - x1) / float(y2 - y1)
        x3 = mp*(y3 - y1) + x1
        return x3, y3

    def area(self, x1, y1, x2, y2):
        if self.eqErr(y1, y2):
            return y1 * abs(x2 - x1)
        else:
            x3, y3 = self.interpolX(x1, x2, x2, y2, 0)
            if x3 < x1:
                bigTri = (x2 - x3) * y2 / 2
                smallTri = (x1 - x3) * y1 / 2
            else:
                bigTri = (x3 - x1) * y1 / 2
                smallTri = (x3 - x2) * y2 /2
            return bigTri - smallTri

    def avgAccel(self, period, accel, time):
        n = len(time)
        x1, y1 = time[0], accel[0]
        i = 1
        currPer = 0
        maxAvg = 0
        currSum = 0
        while i < n:
            currPer += time[i] - x1
            if currPer > period:
                x2, y2 = self.interpolY(x1, y1, time[i], accel[i], \
                                        time[i] - (currPer - period))
                currPer = period
            else:
                x2, y2 = time[i], accel[i]
                i += 1
            currSum += self.area(x1, y1, x2, y2)
            if self.eqErr(currPer, period):
                maxAvg = max(maxAvg, currSum/currPer)
                currSum = 0
                currPer = 0
            x1, y1 = x2, y2
        return maxAvg

#print(GForce().avgAccel(100, [1500,1500,500,2000], [0,100,150,225]))
print(GForce().avgAccel(500, [5,30,5], [0,1000,2000]))