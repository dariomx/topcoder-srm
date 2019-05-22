class Solution(object):
    def read(self, buf, n):
        k = 4
        total = 0
        bufk = [0] * k
        i = 0
        while True:
            cnt = read4(bufk)
            end = cnt
            total += cnt
            if total > n:
                end -= total - n
                total = n
            buf[i:i + end] = bufk[:end]
            if cnt < k or total == n:
                break
            i += end
        return total

