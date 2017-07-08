from math import sqrt

class Archimedes:
    def approximatePi(self, numSides):
        sideSq = 3.0
        n = 3
        while n <= numSides:
            pi = (n * sqrt(sideSq)) / 2
            n *= 2
            sideSq = 2 - 2*sqrt(1 - sideSq/4)
        newPi = (n * sqrt(sideSq)) / 2
        if n/2 == numSides:
            return pi
        elif n == numSides:
            newPi
        else:
            print("%f %f %d %d %d %d %f" %(pi, newPi,  n, n/2, n - numSides, n - n/2, (n - numSides)/float(n - n/2)))
            return pi - (pi - newPi) * (n - numSides)/float(n - n/2)

print(Archimedes().approximatePi(8))