# kinda lame, this was supposedly done in logarithmic time, though did not
# get totally rt the trick

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(n - 1, 0, -1):
            y = n - x
            if '0' in str(x) or '0' in str(y):
                continue
            else:
                return (x, y)

