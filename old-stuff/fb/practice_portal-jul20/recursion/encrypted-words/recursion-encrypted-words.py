import math

# Add any extra import statements you may need here

# non multi-threaded for now
cache = dict()


# Add any helper functions you may need here
def findWithCache(s):
    if s in cache:
        return cache[s]
    if len(s) == 0:
        ret = ''
    else:
        half, par = divmod(len(s), 2)
        if par == 0:
            i = half - 1
        else:
            i = half
        ret = s[i] + findWithCache(s[:i]) + findWithCache(s[i + 1:])
        cache[s] = ret
    return ret


def findEncryptedWord(s):
    cache.clear()
    return findWithCache(s)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "abc"
    expected_1 = "bac"
    output_1 = findEncryptedWord(s1)
    check(expected_1, output_1)

    s2 = "abcd"
    expected_2 = "bacd"
    output_2 = findEncryptedWord(s2)
    check(expected_2, output_2)

    # Add your own test cases here

    s3 = ""
    expected_3 = ""
    output_3 = findEncryptedWord(s3)
    check(expected_3, output_3)

    s4 = "a"
    expected_4 = "a"
    output_4 = findEncryptedWord(s4)
    check(expected_4, output_4)

    s5 = "ab"
    expected_5 = "ab"
    output_5 = findEncryptedWord(s5)
    check(expected_5, output_5)



