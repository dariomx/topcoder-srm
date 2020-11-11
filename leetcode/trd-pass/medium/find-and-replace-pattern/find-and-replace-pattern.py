class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            perm = {}
            codom = set()
            matches = True
            for x, y in zip(word, pattern):
                px = perm.get(x, None)
                if px is None:
                    if y in codom:
                        matches = False
                        break
                    else:
                        perm[x] = y
                        codom.add(y)
                elif px != y:
                    matches = False
                    break
            if matches:
                ans.append(word)
        return ans