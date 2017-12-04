from collections import defaultdict


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def appendNode(last, node):
    last.next = node
    node.prev = last
    return node


def deleteNode(node):
    node.prev.next = node.next
    node.next.prev = node.prev


class Solution(object):
    def createList(self, senate):
        head = ListNode(senate[0])
        last = head
        for party in senate[1:]:
            last = appendNode(last, ListNode(party))
        last.next = head
        head.prev = last
        return head

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        partyName = {'R': 'Radiant', 'D': 'Dire'}
        enemy = {'R': 'D', 'D': 'R'}
        cnt = defaultdict(lambda: 0)
        for party in senate:
            cnt[party] += 1
        node = self.createList(senate)
        while True:
            party = node.val
            if cnt[enemy[party]] == 0:
                return partyName[party]
            else:
                n = node.next
                while n.val == party:
                    n = n.next
                deleteNode(n)
                cnt[enemy[party]] -= 1
                node = node.next
