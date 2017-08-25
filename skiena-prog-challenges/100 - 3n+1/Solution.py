# @JUDGE_ID: dario.mx@gmail.com 100 Python "collatz"

from sys import stdin


def collatz(n, cache):
    cycle_len = 0
    x = n
    while x > 1:
        if x in cache:
            break
        elif x % 2 == 1:
            x = 3 * x + 1
        else:
            x /= 2
        cycle_len += 1
    if x in cache:
        cycle_len += cache[x]
    else:
        cycle_len += 1
    cache[n] = cycle_len
    return cycle_len


# main
cache = dict()
for line in stdin:
    max_cycle = 0
    [start, end] = map(int, line.split())
    for n in range(start, end + 1):
        max_cycle = max(max_cycle, collatz(n, cache))
    print "%d %d %d" % (start, end, max_cycle)
