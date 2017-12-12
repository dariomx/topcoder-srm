cnt = 0
for d1 in xrange(1, 7):
    for d2 in xrange(d1, 7):
        if d1+d2 == 12:
            cnt += 1
print(cnt)