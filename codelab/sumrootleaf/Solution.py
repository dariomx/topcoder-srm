from collections import deque

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(str):
    str2node = lambda s: None if s=="-1" else TreeNode(int(s))
    toks = str.split()
    n = int(toks[0])
    heap = [None] + map(str2node, toks[1:])
    for i in xrange(1, n+1):
        if heap[i] is None:
            continue
        if 2*i <= n:
            heap[i].left = heap[2*i]
        if 2*i + 1 <= n:
            heap[i].right = heap[2*i + 1]
    return heap[1]

class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, root):
        leafSum = 0
        stack = []
        stack.append((root,0))
        while stack:
            node, parVal = stack.pop()
            nodeVal = parVal*10 + node.val
            if not node.left and not node.right:
                leafSum += nodeVal
            if node.left:
                stack.append((node.left, nodeVal))
            if node.right:
                stack.append((node.right, nodeVal))
        return leafSum % 1003

str = "17 1 2 3 4 5 -1 6 7 8 -1 -1 -1 -1 -1 -1 -1 -1"
print(Solution().sumNumbers(buildTree(str)))