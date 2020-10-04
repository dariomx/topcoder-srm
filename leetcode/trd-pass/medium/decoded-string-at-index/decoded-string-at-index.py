class Solution:
    def search(self, K, stack, sizes):
        while stack:
            x = stack.pop()
            size = sizes.pop()
            if type(x) == str:
                start = size - len(x)
                if K >= start:
                    return x[K - start]
            else:
                rep = x
                K = K % (size // rep)

    def decodeAtIndex(self, S: str, K: int) -> str:
        stack = ['']
        sizes = [0]
        size = 0
        for c in S:
            if c.isalpha():
                if type(stack[-1]) != str:
                    stack.append('')
                    sizes.append(size)
                size += 1
                stack[-1] += c
                sizes[-1] += 1
            else:
                rep = int(c)
                size = size * rep
                stack.append(rep)
                sizes.append(size)
            if size >= K:
                break
        return self.search(K - 1, stack, sizes)
