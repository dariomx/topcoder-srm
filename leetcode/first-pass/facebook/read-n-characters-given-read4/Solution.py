class Solution(object):
    def read(self, out, n):
        k = 4
        m = 0
        buf = [' '] * k
        while m < n:
            cnt = read4(buf)
            for i in range(cnt):
                out[m] = buf[i]
                m += 1
                if m == n:
                    break
            if cnt < k:
                break
        return m
