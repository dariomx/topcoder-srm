class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grp = defaultdict(list)
        ans = []
        for pid, size in enumerate(groupSizes):
            grp[size].append(pid)
            if len(grp[size]) == size:
                ans.append(grp[size])
                grp[size] = []
        return ans

