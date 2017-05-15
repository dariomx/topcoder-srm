def cardValue(fig):
    if fig == 'A':
        return 1
    elif fig == 'T':
        return 10
    elif fig == 'J':
        return 11
    elif fig == 'Q':
        return 12
    else:
        return int(fig)

class ListNode:
    def __init__(self, fig):
        self.val = cardValue(fig)
        self.next = None
        self.prev = None

def deleteNode(node):
    node.prev.next = node.next
    node.next.prev = node.prev

def createList(deck):
    start = 0
    while start < len(deck) and deck[start] == 'K':
        start += 1
    if start == len(deck) and deck[start-1] == 'K':
        return ([], 0)
    else:
        head = ListNode(deck[start])
        n = 1
        node = head
        for i in xrange(start+1, len(deck)):
            if deck[i] != 'K':
                node.next = ListNode(deck[i])
                node.next.prev = node
                node = node.next
                n += 1
        node.next = head
        head.prev = node
        return (head, n)

def printList(head):
    node = head
    lst = []
    while True:
        lst.append(node.val)
        node = node.next
        if node == head:
            break
    print(lst)

class CircleGame:
    def cardsLeft(self, deck):
        head, n = createList(deck)
        #printList(head)
        if n == 0:
            return 0
        else:
            node = head
            delCnt = None
            while n > 1 and (delCnt is None or delCnt > 0):
                delCnt = 0
                cnt = n
                while cnt > 0:
                    if node.val + node.next.val == 13:
                        deleteNode(node)
                        deleteNode(node.next)
                        n -= 2
                        delCnt += 2
                        node = node.next.next
                        cnt -= 2
                    else:
                        node = node.next
                        cnt -= 1
            return n

print(CircleGame().cardsLeft("AQK262362TKKAQ6262437892KTTJA332"))