class Solution:
    def restoreIpAddresses(self, s):
        ans = []
        n = len(s)
        min = {1:0, 2:10, 3:100}
        max = {1:9, 2:99, 3:255}
        def rec(i, ip):
            if len(ip) == 4:
                if i == n:
                    ans.append(".".join(ip))
            else:
                rem = n - i
                for k in range(1, 4):
                    if rem < k:
                        break
                    tok = s[i:i+k]
                    if min[k] <= int(tok) <= max[k]:
                        ip.append(tok)
                        rec(i+k, ip)
                        ip.pop()
        rec(0, [])
        return ans