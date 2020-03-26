from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []
        n = len(s)
        m = len(words)
        k = len(words[0])
        words = Counter(words)
        i = 0
        ans = []
        while n - i >= k*m:
            wseen = defaultdict(lambda: 0)
            for j in range(m):
                w = s[(i + j*k):(i + j*k + k)]
                if w in words and wseen[w] < words[w]:
                    wseen[w] += 1
                else:
                    break
            if len(wseen) == len(words) and wseen == words:
                ans.append(i)
            i += 1
        return ans
