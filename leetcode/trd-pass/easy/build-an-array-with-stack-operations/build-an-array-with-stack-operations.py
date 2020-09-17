class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for x in range(1, n+1):
            if i == len(target):
                break
            if target[i] == x:
                ans.append("Push")
                i += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans