from sys import maxsize as maxint
from collections import defaultdict, Counter

class Solution(object):
    def minWindow(self, s, t):
        n = len(s)
        t_set = set(t)
        m = len(t_set)
        t_cnt = [0] * m
        idx = dict()
        i = 0
        for c, cnt in Counter(t).items():
            idx[c] = i
            t_cnt[i] += cnt
            i += 1
        def upd_win_fwd():
            nonlocal win_size
            c = s[j]
            if c in t_set:
                k = idx[c]
                win[k] += 1
                if win[k] == t_cnt[k]:
                    win_size += 1
        def upd_win_bck():
            nonlocal win_size
            c = s[i]
            if c in t_set:
                k = idx[c]
                if win[k] == t_cnt[k]:
                    win_size -= 1
                win[k] -= 1
        def upd_min():
            nonlocal min_len
            nonlocal min_win
            if win_size >= m:
                win_len = j - i + 1
                if win_len < min_len:
                    min_len = win_len
                    min_win = i, j
        win = [0] * m
        win_size = 0
        min_len = maxint
        min_win = None
        i, j = 0, 0
        upd_win_fwd()
        upd_min()
        while True:
            if win_size < m:
                j += 1
                if j == n:
                    break
                upd_win_fwd()
            else:
                if i == n:
                    break
                upd_win_bck()
                i += 1
            upd_min()
        if min_win:
            i, j = min_win
            return s[i:j+1]
        else:
            return ""