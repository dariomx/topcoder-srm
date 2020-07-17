import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def isBalanced(s):
    stack = []
    pair = {'(': ')', '[': ']', '{': '}'}
    top_lev = 0
    for c in s:
        if c in pair:
            if len(stack) == 0:
                top_lev += 1
            stack.append(c)
        elif stack and c == pair[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0 and top_lev in (0, 1, 2)


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
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

    # Add your own test cases here
    s3 = "{}()"
    expected_3 = True
    output_3 = isBalanced(s3)
    check(expected_3, output_3)

    s4 = "{(})"
    expected_4 = False
    output_4 = isBalanced(s4)
    check(expected_4, output_4)

    s5 = ")"
    expected_5 = False
    output_5 = isBalanced(s5)
    check(expected_5, output_5)

    s6 = ""
    expected_6 = True
    output_6 = isBalanced(s6)
    check(expected_6, output_6)

    s7 = "{}()[]"
    expected_7 = False
    output_7 = isBalanced(s7)
    check(expected_7, output_7)

