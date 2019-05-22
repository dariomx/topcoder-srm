class Solution(object):
    def postorder(self, root):
        stack = []
        if root:
            stack.append((root, False))
        ans = []
        while stack:
            node, is_ready = stack.pop()
            if is_ready:
                ans.append(node.val)
            else:
                stack.append((node, True))
                for chd in reversed(node.children):
                    stack.append((chd, False))
        return ans