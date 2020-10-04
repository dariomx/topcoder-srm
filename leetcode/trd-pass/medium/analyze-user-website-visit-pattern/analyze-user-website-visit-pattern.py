class Solution:
    def gen_seq_user(self, i, user, visits, seq):
        if len(seq) == 3:
            yield (user, tuple(seq))
        elif len(seq) < 3 and i < len(visits):
            yield from self.gen_seq_user(i + 1, user, visits, seq)
            seq.append(visits[i])
            yield from self.gen_seq_user(i + 1, user, visits, seq)
            seq.pop()

    def gen_seq(self, username, timestamp, website):
        visits = []
        seq = []
        prevUser = None
        sent = (None, None, None)
        for u, _, w in sorted(zip(username, timestamp, website)) + [sent]:
            if u != prevUser:
                seq.clear()
                yield from self.gen_seq_user(0, u, visits, seq)
                visits.clear()
                prevUser = u
            visits.append(w)

    def mostVisitedPattern(self, username: List[str], timestamp: List[int],
                           website: List[str]) -> List[str]:
        usr = defaultdict(set)
        usr[None] = set()
        ans = None
        for u, seq in self.gen_seq(username, timestamp, website):
            usr[seq].add(u)
            if len(usr[seq]) > len(usr[ans]) or \
                    (len(usr[seq]) == len(usr[ans]) and seq < ans):
                ans = seq
        return ans
