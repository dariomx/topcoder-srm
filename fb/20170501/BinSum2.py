def binSum(x, y):
    ix = len(x) - 1
    iy = len(y) - 1
    rem = 0
    ans = ""
    while ix >= 0 or iy >= 0:
        sum2 = rem
        if ix >= 0:
            sum2 += int(x[ix])
        if iy >= 0:
            sum2 += int(y[iy])
        rem = sum2 / 2
        sum2 %= 2
        ans = str(sum2) + ans
        ix -= 1
        iy -= 1
    ans = str(rem) + ans
    return ans

print(binSum('10101', '110'))
