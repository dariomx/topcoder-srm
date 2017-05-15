class BinaryCode:
    def decode_int(self, P0, Q):
        P = [0] * len(Q)
        P[0] = P0
        P[1] = Q[0] - P[0]
        for i in xrange(1, len(P) - 1):
            P[i + 1] = Q[i] - P[i] - P[i - 1]
        return P

    def encode(self, P):
        Q = [0] * len(P)
        Q[0] = P[0] + P[1]
        for i in xrange(1, len(Q) - 1):
            Q[i] = P[i - 1] + P[i] + P[i + 1]
        i = len(Q) - 1
        Q[i] = P[i - 1] + P[i]
        return Q

    def list2str(self, lst):
        return "".join(map(str, lst))

    def check_dec(self, P, Q):
        return self.list2str(P) if self.encode(P) == Q else "NONE"

    def decode(self, msg):
        Q = map(int, msg)
        P0 = self.decode_int(0, Q)
        P1 = self.decode_int(1, Q)
        check_dec_Q = lambda P: self.check_dec(P, Q)
        return map(check_dec_Q, [P0, P1])