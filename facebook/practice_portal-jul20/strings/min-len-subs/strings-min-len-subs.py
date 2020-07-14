import math
# Add any extra import statements you may need here
from collections import Counter


# Add any helper functions you may need here
def is_substr(cntS, cntT):
    for sym, cnt in cntT.items():
        if cntT[sym] > cntS.get(sym, 0):
            return False
    return True


def canShrink(sym, cntS, cntT):
    if cntS[sym] - 1 >= cntT[sym]:
        cntS[sym] -= 1
        if cntS[sym] == 0:
            del cntS[sym]
        return True
    else:
        return False


def min_length_substring(s, t):
    cntS = Counter(s)
    cntT = Counter(t)
    if not is_substr(cntS, cntT):
        return -1
    start, end = 0, len(s) - 1
    while start <= end:
        if canShrink(s[start], cntS, cntT):
            start += 1
        elif canShrink(s[end], cntS, cntT):
            end -= 1
        else:
            break
    return end - start + 1


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='',
              end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

# Add your own test cases here
