import sys
from collections import deque

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDelLeftMost(self, root):
        node = root
        parent = None
        while node.left:
            parent = node
            node = node.left
        if parent:
            parent.left = node.right
        else:
            root = node.right
        return node, root

    def printList(self, head):
        node = head
        while node:
            sys.stdout.write(str(node.val) + ",")
            node = node.right
        print("")

    def convertToList(self, root):
        prev = None
        head = None
        while root:
            next, root = self.getDelLeftMost(root)
            if not head:
                head = next
            next.left = None
            next.right = None
            if prev:
                prev.right = next
            prev = next
        self.printList(head)
        return head

    def findSwappedPair(self, head):
        node = head
        fst = None
        while fst is None:
            if node.val > node.right.val:
                fst = node
            else:
                node = node.right
        snd = None
        while snd is None:
            if node.right is None or node.right.val > fst.val:
                snd = node
            else:
                node = node.right
        return sorted([fst.val, snd.val])

    def createTree(self, lst):
        def getChild(s):
            val = int(s)
            if val < 0:
                return None
            else:
                return TreeNode(val)
        #
        root = getChild(lst[0])
        queue = deque()
        queue.appendleft(root)
        i = 0
        while queue:
            node = queue.pop()
            node.left = getChild(lst[i + 1])
            node.right = getChild(lst[i + 2])
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)
            i += 2
        return root

    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, root):
        return self.findSwappedPair(self.convertToList(root))

soln = Solution()
inp = "5 76 77 -1 -1 -1"
root = soln.createTree(inp.split()[1:])
print(soln.recoverTree(root))
