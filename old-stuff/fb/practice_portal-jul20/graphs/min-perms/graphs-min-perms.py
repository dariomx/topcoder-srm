import math
# Add any extra import statements you may need here
from collections import deque


# Add any helper functions you may need here
def is_sorted(arr):
    if len(arr) == 0:
        return True
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def minOperations(arr):
    queue = deque([(arr, 0)])
    visited = set()
    n = len(arr)
    while queue:
        perm, steps = queue.popleft()
        if is_sorted(perm):
            return steps
        for i in range(n - 1):
            for j in range(i + 1, n):
                key = tuple(perm + [i, j])
                if key in visited:
                    continue
                visited.add(key)
                new_perm = perm[:i] + perm[i:(j + 1)][::-1] + perm[j + 1:]
                queue.append((new_perm, steps + 1))
    raise ValueError('Could not sort!')


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
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
