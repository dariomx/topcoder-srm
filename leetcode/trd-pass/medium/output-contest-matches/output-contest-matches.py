class Solution:
    def findContestMatch(self, n: int) -> str:
        matches = [str(i) for i in range(1, n+1)]
        k = len(matches)
        while k > 1:
            tmp = []
            for i in range(k // 2):
                match = "(%s,%s)" % (matches[i], matches[k-1-i])
                tmp.append(match)
            matches = tmp
            k = len(matches)
        return matches[0]