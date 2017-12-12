def binSum(x, y):
    n = min(len(x), len(y))
    m = max(len(x), len(y))
    res = ""
    rem = 0
    for i in xrange(n-1,-1,-1):
        sum2 = rem + int(x[i]) + int(y[i])
        rem = sum2 / 2
        sum2 %= 2
        res = str(sum2) + res
        print(res)
    if m == len(y):
        z = y
    else:
        z = x
    for i in xrange(m - n - 1, -1, -1):
        sum2 = rem + int(z[i])
        rem = sum2 / 2
        sum2 %= 2
        res = str(sum2) + res
        print(res)
    res = str(rem) + res
    return res

print(binSum('10101', '110'))

#10101
#  110
#11011