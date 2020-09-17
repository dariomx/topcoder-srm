class Solution:
    def freqAlphabets(self, s: str) -> str:
        deq = deque()
        ans = ''

        def empty():
            nonlocal ans
            while deq:
                d = chr(ord('a') + int(deq.popleft()) - 1)
                ans += d

        for c in s:
            if c == '#':
                x = deq.pop()
                y = deq.pop()
                dd = chr(ord('j') + int(y + x) - 10)
                empty()
                ans += dd
            else:
                deq.append(c)
        empty()
        return ans




