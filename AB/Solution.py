class AB:
    def createString(self, N, K):
        def findNumAB():
            for i in xrange(0, K+1):
                for j in xrange(0, K+1):
                    if i+j <= N and i*j == K:
                        return (i,j)
            return None
        #
        numAB = findNumAB()
        if numAB is None:
            return ""
        else:
            na, nb = numAB
            return "".join(["B"]*(N - (na+nb)) + ["A"]*na + ["B"]*nb)

print(AB().createString(3, 2))

# ABB