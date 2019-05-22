class Solution(object):
    def repeatedNTimes(self, A):
        seen = set()
        for x in A:
            if x in seen:
                return x
            else:
                seen.add(x)