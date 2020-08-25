class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        k = 5
        ans = []
        prev = None
        for sid, score in sorted(items, key=lambda t: (t[0], -t[1])):
            if sid != prev:
                cnt = acc = 0
                prev = sid
            if cnt < k:
                cnt += 1
                acc += score
                if cnt == k:
                    ans.append([sid, acc // cnt])
        return ans
