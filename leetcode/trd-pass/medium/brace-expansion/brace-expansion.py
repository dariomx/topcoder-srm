class Solution:
    def expand(self, S: str) -> List[str]:
        ans = []
        if len(S) == 0:
            ans.append('')
        elif S[0] == '{':
            i = S.index('}')
            H, T = S[1:i], S[i+1:]
            ss = self.expand(T)
            for c in sorted(H.split(',')):
                for s in ss:
                    ans.append(c + s)
        else:
            ss = self.expand(S[1:])
            for s in ss:
                ans.append(S[0] + s)
        return ans