from Solution import Solution

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def main():
    soln = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(soln.isPalindrome(head))

if __name__ == '__main__':
    main()

