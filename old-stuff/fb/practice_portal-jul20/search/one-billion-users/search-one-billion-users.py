import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def users_day(growthRates, day):
    return sum((math.pow(g, day) for g in growthRates))


# target is assumed to be integer
def calc_max_days(maxG, target):
    if maxG <= 1:
        raise ValueError('Can never reach the target')
    else:
        return int(math.ceil(math.log(target) / math.log(maxG)))


def getBillionUsersDay(growthRates):
    target = 1000000000
    maxG = max(growthRates)
    start = 1
    end = calc_max_days(maxG, target)
    while start <= end:
        mid = (start + end) // 2
        users = users_day(growthRates, mid)
        if users == target or \
                (users > target and (
                        mid == 0 or users_day(growthRates, mid - 1) < target)):
            return mid
        elif users < target:
            start = mid + 1
        else:
            end = mid - 1
    raise ValueError('Could not find the day!')


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
    test_1 = [1.1, 1.2, 1.3]
    expected_1 = 79
    output_1 = getBillionUsersDay(test_1)
    check(expected_1, output_1)

    test_2 = [1.01, 1.02]
    expected_2 = 1047
    output_2 = getBillionUsersDay(test_2)
    check(expected_2, output_2)

    # Add your own test cases here
    test_3 = [1000000000]
    expected_3 = 1
    output_3 = getBillionUsersDay(test_3)
    check(expected_3, output_3)

    test_4 = [1000000001]
    expected_4 = 1
    output_4 = getBillionUsersDay(test_4)
    check(expected_4, output_4)

    test_5 = [1.001]
    expected_5 = 20734
    output_5 = getBillionUsersDay(test_5)
    check(expected_5, output_5)
