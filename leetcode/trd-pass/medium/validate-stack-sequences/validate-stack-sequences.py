class Solution:
    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        n = len(pushed)
        i = 0
        stack = []
        for j in range(n):
            while not stack or stack[-1] != popped[j]:
                if i < n:
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False
            stack.pop()
        return True 
