from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        visits = defaultdict(lambda: 0)
        for cpd in cpdomains:
            cnt, domain = cpd.split(" ")
            parts = domain.split(".")
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                visits[subdomain] += int(cnt)
        fmt = lambda d: "%d %s" % (visits[d], d)
        return list(map(fmt, visits))
