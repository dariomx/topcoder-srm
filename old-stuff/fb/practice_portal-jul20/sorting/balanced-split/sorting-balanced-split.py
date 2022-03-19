import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
    arr.sort()
    tsum = sum(arr)
    psum = 0
    for i, x in enumerate(arr):
        psum += x
        if psum == tsum - psum:
            if i + 1 < len(arr) and arr[i] < arr[i + 1]:
                return True
            else:
                break
    return False


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
    arr_1 = [2, 1, 2, 5]
    expected_1 = True
    output_1 = balancedSplitExists(arr_1)
    check(expected_1, output_1)

    arr_2 = [3, 6, 3, 4, 4]
    expected_2 = False
    output_2 = balancedSplitExists(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    arr_3 = [1, 5, 7, 1]
    expected_3 = True
    output_3 = balancedSplitExists(arr_3)
    check(expected_3, output_3)

    arr_4 = [12, 7, 6, 7, 6]
    expected_4 = False
    output_4 = balancedSplitExists(arr_4)
    check(expected_4, output_4)

    arr_5 = [6]
    expected_5 = False
    output_5 = balancedSplitExists(arr_5)
    check(expected_5, output_5)

    arr_6 = [6, 6]
    expected_6 = False
    output_6 = balancedSplitExists(arr_6)
    check(expected_6, output_6)

    arr_7 = [7, 6, 1]
    expected_7 = True
    output_7 = balancedSplitExists(arr_7)
    check(expected_7, output_7)

