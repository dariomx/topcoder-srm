# experiment #1
def n_digit(n):
    seq = ''
    for i in range(1, n + 1):
        seq += str(i)
        if len(seq) >= n:
            break
    return int(seq[n-1])


# main
for n in range(1, 3001):
    print("%d -> %d" % (n, n_digit(n)))
