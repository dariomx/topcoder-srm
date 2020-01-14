from bisect import bisect_left


class Solution:
    def nextClosestTime(self, time):
        tarr = list(map(int, time.replace(":", "")))
        is_overload = lambda x: (i == 2 and x > 59) or (i == 0 and x > 23)
        digs = sorted(set(tarr))
        k = len(digs)
        rem = 1
        for i in range(3, -1, -1):
            j = bisect_left(digs, tarr[i])
            j = (j + rem) % k
            tarr[i] = digs[j]
            overloaded = (i < 3 and is_overload(tarr[i] * 10 + tarr[i + 1]))
            if (rem > 0 and j == 0) or overloaded:
                rem = 1
                tarr[i] = digs[0]
                if overloaded:
                    tarr[i + 1] = digs[0]
            else:
                rem = 0
        to_str = lambda arr: "".join(map(str, arr[:2]))
        return to_str(tarr[:2]) + ":" + to_str(tarr[2:])


