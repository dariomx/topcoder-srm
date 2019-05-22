class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def getSize(hd):
            size = 0
            node = hd
            while node:
                size += 1
                node = node.next
            return size
        def split(hd):
            size = getSize(hd)
            node = hd
            for _ in range(size//2-1):
                node = node.next
            tmp = node.next
            node.next = None
            return hd, tmp
        def merge(hd1, hd2):
            node1, node2 = hd1, hd2
            sent = ListNode(666)
            tail = sent
            def ins(x):
                nonlocal tail
                tail.next = x
                tail = x
            while node1 and node2:
                if node1.val < node2.val:
                    ins(node1)
                    node1 = node1.next
                else:
                    ins(node2)
                    node2 = node2.next
            if node1:
                ins(node1)
            if node2:
                ins(node2)
            return sent.next
        def mergeSort(hd):
            if not hd or not hd.next:
                return hd
            hd1, hd2 = split(hd)
            hd1 = mergeSort(hd1)
            hd2 = mergeSort(hd2)
            return merge(hd1, hd2)
        return mergeSort(head)