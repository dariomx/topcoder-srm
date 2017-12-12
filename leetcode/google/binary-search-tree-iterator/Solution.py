# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

ME = 0
LEFT = 1
RIGHT = 2


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root:
            self.stack = [(root, LEFT)]
        else:
            self.stack = []
        self.next_val = None

    def hasNext(self):
        """
        :rtype: bool
        """
        self.next_val = self.get_next()
        return self.next_val is not None

    def next(self):
        return self.next_val

    def get_next(self):
        """
        :rtype: int
        """
        while self.stack:
            node, proc = self.stack.pop()
            if proc == LEFT:
                self.stack.append((node, ME))
                if node.left:
                    self.stack.append((node.left, LEFT))
            elif proc == ME:
                self.stack.append((node, RIGHT))
                return node.val
            else:
                if node.right:
                    self.stack.append((node.right, LEFT))
        return None

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())
