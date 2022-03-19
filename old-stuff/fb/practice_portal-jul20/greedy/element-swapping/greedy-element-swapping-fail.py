import math
# Add any extra import statements you may need here
from heapq import heapify, heappop


# Add any helper functions you may need here
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DList:
    def __init__(self, nodes):
        self.head = None
        self.tail = None
        for n in nodes:
            self.append(n)

    def append(self, node):
        self._connect(self.tail, node)
        self.tail = node

    def swapPrev(self, node):
        if node.prev is None:
            return
            # backup pointers
        prev_prev = node.prev.prev
        node_prev = node.prev
        node_next = node.next
        # clear both nodes
        node.prev.prev = node.prev.next = None
        node.prev = node.next = None
        # re-connect
        self._connect(prev_prev, node)
        self._connect(node, node_prev)
        self._connect(node_prev, node_next)
        if prev_prev is None:
            self.head = node

            # this is really Python list type, but just to follow problem
            # notation

    def to_array(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def _connect(self, node1, node2):
        if node1:
            node1.next = node2
        if node2:
            node2.prev = node1


def findMinArray(arr, k):
    nodes = [Node(x) for x in arr]
    heap = [(x, n) for (x, n) in zip(arr, nodes)]
    heapify(heap)
    dList = DList(nodes)
    while len(heap) > 0 and k > 0:
        x, node = heappop(heap)
        while node.prev and node.prev.val > node.val and k > 0:
            dList.swapPrev(node)
            k -= 1
    return dList.to_array()


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
    n_1 = 3
    arr_1 = [5, 3, 1]
    k_1 = 2
    expected_1 = [1, 5, 3]
    output_1 = findMinArray(arr_1, k_1)
    check(expected_1, output_1)

    n_2 = 5
    arr_2 = [8, 9, 11, 2, 1]
    k_2 = 3
    expected_2 = [2, 8, 9, 11, 1]
    output_2 = findMinArray(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
