class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        word = ''
        queue = deque()
        ans = []
        for c in text + ' ':
            if c == ' ':
                queue.append(word)
                if len(queue) == 3:
                    if queue[0] == first and queue[1] == second:
                        ans.append(queue[2])
                    queue.popleft()
                word = ''
            else:
                word += c
        return ans