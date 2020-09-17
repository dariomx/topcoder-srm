class Solution:
    def isGood(self, w, cnt):
        for c, k in Counter(w).items():
            if k > cnt[c]:
                return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        return sum((len(w) for w in words if self.isGood(w, cnt)))
