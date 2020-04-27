from collections import defaultdict, Counter
from heapq import heapify, heappop, heappush


class Solution:
    def sameGroup(self, A, B, grp):
        n = len(A)
        even, odd = defaultdict(list), defaultdict(list)
        for i in range(n):
            if i % 2 == 0:
                even[A[i]].append(i)
            else:
                odd[A[i]].append(i)
        for ix in even.values():
            heapify(ix)
        for ix in odd.values():
            heapify(ix)
        for i in range(n):
            a, b = A[i], B[i]
            if i % 2 == 0:
                assert i == heappop(even[a])
                cand = even[b] if b in even else None
            else:
                assert i == heappop(odd[a])
                cand = odd[b] if b in odd else None
            if a == b:
                continue
            elif cand is None or len(cand) == 0:
                return False
            else:
                j = heappop(cand)
                A[i], A[j] = A[j], A[i]
                grp.add(''.join(A))
                if i % 2 == 0:
                    heappush(even[a], j)
                else:
                    heappush(odd[a], j)
        return True

    def numSpecialEquivGroups(self, A):
        def getCnt(x):
            if x not in cnt:
                cnt[x] = Counter(x)
            return cnt[x]

        A = set(A)
        ans = 0
        cnt = {}
        while A:
            x = A.pop()
            cx = getCnt(x)
            ans += 1
            grp = set()
            for y in A:
                if cx != getCnt(y):
                    continue
                if self.sameGroup(list(x), list(y), grp):
                    grp.add(y)
            A -= grp
        return ans