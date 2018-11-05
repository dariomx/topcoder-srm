from collections import deque


class Solution:
    def isPalindrome(self, arr):
        n = len(arr)
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                return False
        return True

    def isSymmetric(self, root):
        queue = deque()
        level = []
        if root:
            queue.append((root, 0))
            level.append(root.val)
        prevLev = None
        while queue:
            node, lev = queue.popleft()
            if lev != prevLev:
                if not self.isPalindrome(level):
                    return False
                else:
                    level = [node.val if node else None]
                    prevLev = lev
            else:
                level.append(node.val if node else None)
            if node:
                queue.append((node.left, lev + 1))
                queue.append((node.right, lev + 1))
        return self.isPalindrome(level)