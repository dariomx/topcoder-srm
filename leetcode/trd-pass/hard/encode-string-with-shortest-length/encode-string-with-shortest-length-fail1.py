from functools import lru_cache


class Solution:
    def encode(self, string: str) -> str:
        def compress(rep, cnt):
            nonlocal ans
            if len(rep) == 0:
                return ''
            elif cnt == 1:
                return rep
            else:
                ans[rep] = rep
                rec(rep, 0, '', 0, '')
                return '%d[%s]' % (cnt, ans[rep])
        @lru_cache(None)
        def rec(s, i, rep, cnt, enc):
            nonlocal ans
            # print(i, rep, cnt, enc)
            if i == len(s):
                enc += compress(rep, cnt)
                if len(enc) < len(ans[s]):
                    ans[s] = enc
            else:
                if cnt == 1:
                    rec(s, i + 1, rep + s[i], 1, enc)
                if len(rep) > 0 and rep == s[i:(i + len(rep))]:
                    rec(s, i + len(rep), rep, cnt + 1, enc)
                comp = compress(rep, cnt)
                rec(s, i + 1, s[i], 1, enc + comp)
        ans = {string: string, '':''}
        rec(string, 0, '', 0, '')
        return ans[string]

print(Solution().encode('aaaaaaaaaabbbaaaaabbb'))
