import math


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def reverse(head):
    new_head = head_even = tail_even = tail_odd = None
    node = head

    def handle_even():
        nonlocal new_head, head_even, tail_even, tail_odd, node
        if tail_odd is not None:
            tail_odd.next = head_even
        tail_even.next = node
        if new_head is None:
            new_head = head_even
        head_even = tail_even = None

    while node:
        if node.data % 2 == 0:
            if head_even is None:
                head_even = tail_even = node
                node = node.next
                tail_even.next = None
            else:
                tmp = node.next
                node.next = head_even
                head_even = node
                node = tmp
        else:
            if tail_even is None:
                if tail_odd is not None:
                    tail_odd.next = node
            else:
                handle_even()
            tail_odd = node
            if new_head is None:
                new_head = tail_odd
            node = node.next
            tail_odd.next = None
    if tail_even is not None:
        handle_even()
    return new_head


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printLinkedList(head):
    print('[', end='')
    while head != None:
        print(head.data, end='')
        head = head.next
        if head != None:
            print(' ', end='')
    print(']', end='')


test_case_number = 1


def check(expectedHead, outputHead):
    global test_case_number
    tempExpectedHead = expectedHead
    tempOutputHead = outputHead
    result = True
    while expectedHead != None and outputHead != None:
        result &= (expectedHead.data == outputHead.data)
        expectedHead = expectedHead.next
        outputHead = outputHead.next

    if not (outputHead == None and expectedHead == None):
        result = False

    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, ' Test #', test_case_number, sep='')
    else:
        print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='',
              end='')
        printLinkedList(tempExpectedHead)
        print(' Your output: ', end='')
        printLinkedList(tempOutputHead)
        print()
    test_case_number += 1


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


if __name__ == "__main__":
    head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
    expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
    output_1 = reverse(head_1)
    check(expected_1, output_1)

    head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
    expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
    output_2 = reverse(head_2)
    check(expected_2, output_2)

    # Add your own test cases here
    head_3 = createLinkedList([])
    expected_3 = createLinkedList([])
    output_3 = reverse(head_3)
    check(expected_3, output_3)

    head_4 = createLinkedList([1])
    expected_4 = createLinkedList([1])
    output_4 = reverse(head_4)
    check(expected_4, output_4)

    head_5 = createLinkedList([2])
    expected_5 = createLinkedList([2])
    output_5 = reverse(head_5)
    check(expected_5, output_5)

    head_6 = createLinkedList([1, 3])
    expected_6 = createLinkedList([1, 3])
    output_6 = reverse(head_6)
    check(expected_6, output_6)

    head_7 = createLinkedList([2, 4])
    expected_7 = createLinkedList([4, 2])
    output_7 = reverse(head_7)
    check(expected_7, output_7)

    head_8 = createLinkedList([1, 3, 2, 18, 24, 3, 5, 7, 9, 6, 12, 13, 15])
    expected_8 = createLinkedList([1, 3, 24, 18, 2, 3, 5, 7, 9, 12, 6, 13, 15])
    output_8 = reverse(head_8)
    check(expected_8, output_8)
