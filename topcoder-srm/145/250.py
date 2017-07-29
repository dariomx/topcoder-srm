class Bonuses:
    def getDivision(self, points):
        n = len(points)
        totPoints = float(sum(points))
        perc = [0] * n
        for i in xrange(n):
            perc[i] = int(100 * points[i]/totPoints)
        totPerc = sum(perc)
        if totPerc < 100:
            for i in sorted(xrange(n), key=lambda j: (-points[j], j)):
                perc[i] += 1
                totPerc += 1
                if totPerc == 100:
                    return perc
        return perc

print(Bonuses().getDivision([5,5,5,5,5,5]))