class Solution:
    def bulbSwitch(self, n: int) -> int:
        fmt = lambda arr: ''.join(map(lambda x: str(int(x)), arr))
        bulb = [True] * n
        onprd = n
        for i in range(2, n+1):
            if i == 2:
                onprd -= n // 2
            else:
                q = n // i
                if q % 2 == 1:
                    onprd -= i % 2
            oncnt = 0
            for j in range(n):
                if (j+1) % i == 0:
                    bulb[j] = not bulb[j]
                oncnt += int(bulb[j])
            args = (i, oncnt, onprd, fmt(bulb))
            print("%02d: %02d vs %02d: %s" % args)
        return oncnt


# main
Solution().bulbSwitch(16)
