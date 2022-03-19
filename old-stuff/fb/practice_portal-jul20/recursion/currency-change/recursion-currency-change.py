import math

# Add any extra import statements you may need here


# Add any helper functions you may need here
cache = dict()


def canChange(targetMoney, denominations):
    if targetMoney in cache:
        return cache[targetMoney]
    elif targetMoney < 0:
        return False
    elif targetMoney == 0:
        return True

    if targetMoney == 0:
        return True
    elif targetMoney in denominations:
        ret = True
    else:
        ret = False
        for denom in denominations:
            if canChange(targetMoney - denom, denominations):
                ret = True
                break
    cache[targetMoney] = ret
    return ret


def canGetExactChange(targetMoney, denominations):
    cache.clear()
    return canChange(targetMoney, denominations)


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
    target_1 = 94
    arr_1 = [5, 10, 25, 100, 200]
    expected_1 = False
    output_1 = canGetExactChange(target_1, arr_1)
    check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    # Add your own test cases here

    target_3 = 666
    arr_3 = [1]
    expected_3 = True
    output_3 = canGetExactChange(target_3, arr_3)
    check(expected_3, output_3)

    target_4 = 123
    arr_4 = [1, 2, 3]
    expected_4 = True
    output_4 = canGetExactChange(target_4, arr_4)
    check(expected_4, output_4)

    target_5 = 1 * 3 + 2 * 5 + 3 * 7
    arr_5 = [3, 5, 7]
    expected_5 = True
    output_5 = canGetExactChange(target_5, arr_5)
    check(expected_5, output_5)

    target_5 = 1 * 3 + 2 * 5 + 3 * 7
    arr_5 = [3, 7]
    expected_5 = True
    output_5 = canGetExactChange(target_5, arr_5)
    check(expected_5, output_5)

    target_6 = 11
    arr_6 = [3, 7]
    expected_6 = False
    output_6 = canGetExactChange(target_6, arr_6)
    check(expected_6, output_6)

    target_7 = 0
    arr_7 = [3, 7]
    expected_7 = True
    output_7 = canGetExactChange(target_7, arr_7)
    check(expected_7, output_7)

    target_8 = -1
    arr_8 = [3, 7]
    expected_8 = False
    output_8 = canGetExactChange(target_8, arr_8)
    check(expected_8, output_8)



