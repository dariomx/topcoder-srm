class Solution:
    def compress(self, nums: list[int]) -> list[int]:
        cnums = []
        prev = None
        cnt = 0
        for x in (nums + [0]):
            if x == prev:
                cnt += 1
            else:
                if cnt > 0:
                    cnums.append((-cnt, prev))
                cnt = 1
                prev = x
        return cnums

    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        cnums = self.compress(nums)
        heapify(cnums)
        used = defaultdict(lambda: 0)
        nsub = 0
        while len(cnums) >= K:
            tmp = []
            for _ in range(K):
                cnt, x = heappop(cnums)
                cnt += 1
                used[x] += 1
                if cnt != 0:
                    tmp.append((cnt, x))
            nsub += 1
            while tmp:
                heappush(cnums, tmp.pop())
        for cnt, x in cnums:
            avail = nsub - used[x]
            if abs(cnt) > avail:
                return False
        return True