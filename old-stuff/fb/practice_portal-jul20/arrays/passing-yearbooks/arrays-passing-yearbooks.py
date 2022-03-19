import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def pass_yb(arr, tmp, sig, own):
    done = 0
    for i, x in enumerate(arr):
        j = x - 1
        if (j == i and not own[j]) or j != i:
            sig[j] += 1
            tmp[j] = x
        if j == i:
            own[j] = True
            done += 1
    return tmp, arr, done


def findSignatureCounts(arr):
    n = len(arr)
    tmp = [0] * n
    sig = [0] * n
    own = [False] * n
    done = 0
    while done < n:
        arr, tmp, done = pass_yb(arr, tmp, sig, own)
    return sig


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='',
              end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [2, 1]
    expected_1 = [2, 2]
    output_1 = findSignatureCounts(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2]
    expected_2 = [1, 1]
    output_2 = findSignatureCounts(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
