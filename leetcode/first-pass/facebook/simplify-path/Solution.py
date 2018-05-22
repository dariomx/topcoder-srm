class Solution:
    def simplifyPath(self, path):
        stack = []
        for dir in path.split("/"):
            if not dir or dir == ".":
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return "/" + "/".join(stack)