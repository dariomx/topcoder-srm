class BigBurger:
    def maxWait(self, arrival, service):
        start = 0
        maxW = 0
        for i in xrange(len(arrival)):
            a, s = arrival[i], service[i]
            if a < start:
                wait = start - a
            else:
                wait = 0
            maxW = max(maxW, wait)
            start = a + wait + s
        return maxW

print(BigBurger().maxWait([3,3,9], [2,15,14]))
