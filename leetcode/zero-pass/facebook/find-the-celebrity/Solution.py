class Solution(object):
    def findCelebrity(self, n):
        for i in range(n):
            celeb = True
            for j in xrange(n):
                if i != j and not knows(j, i):
                    celeb = False
                    break
            if not celeb:
                continue
            for j in xrange(n):
                if i != j and knows(i, j):
                    celeb = False
                    break
            if celeb:
                return i
        return -1

