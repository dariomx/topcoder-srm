from collections import deque, defaultdict


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return s
        perm = []
        curr = list(s)
        cnt = defaultdict(lambda: 0)
        for c in curr:
            cnt[c] += 1
        curr.sort(key=lambda c: -cnt[c])
        curr = deque(curr)
        next = deque()
        win = deque()
        win_set = set()
        while True:
            size_perm = len(perm)
            while curr:
                c = curr.popleft()
                if c in win_set:
                    next.append(c)
                else:
                    win.append(c)
                    win_set.add(c)
                    perm.append(c)
                if len(win) == k:
                    win_set.remove(win.popleft())
            if len(next) == 0:
                return ''.join(perm)
            elif size_perm == len(perm):
                print(perm)
                print(win)
                print(next)
                return ''
            curr, next = next, curr
            next.clear()

