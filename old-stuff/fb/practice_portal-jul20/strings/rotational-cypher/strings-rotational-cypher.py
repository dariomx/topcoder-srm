import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
    upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    digit = [chr(i) for i in range(ord('0'), ord('9') + 1)]

    def get_arr(c):
        if c.isupper():
            return upper
        elif c.islower():
            return lower
        elif c.isdigit():
            return digit
        else:
            return None

    ans = ''
    for c in input:
        arr = get_arr(c)
        if arr is None:
            ans += c
        else:
            i = ord(c) - ord(arr[0])
            ans += arr[(i + rotation_factor) % len(arr)]
    return ans


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
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
