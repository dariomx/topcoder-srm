from math import factorial as fact
from operator import mul


class Lottery:
    def comb(self, n, m):
        return fact(n) / (fact(n - m) * fact(m))

    def numPos(self, choices, blanks, sort, uniq):
        if not sort and not uniq:
            np = choices ** blanks
        elif not sort and uniq:
            np = reduce(mul, xrange(choices, choices - blanks, -1), 1)
        elif sort and not uniq:
            np = self.comb(choices - 1 + blanks, blanks)
        elif sort and uniq:
            np = self.comb(choices, blanks)
        return np

    def parseRule(self, ruleStr):
        name, params = ruleStr.split(":")
        choices, blanks, sort, uniq = params.strip().split(" ")
        return [ruleStr, name, int(choices), int(blanks), sort == "T", uniq == "T"]

    def scoreRule(self, rule):
        _, _, choices, blanks, sort, uniq = rule
        return rule + [self.numPos(choices, blanks, sort, uniq)]

    def sortByOdds(self, rulesStr):
        rules = map(self.parseRule, rulesStr)
        rules = map(self.scoreRule, rules)
        rules = sorted(rules, key=lambda x: (x[-1], x[1]))
        return map(lambda x: x[1], rules)