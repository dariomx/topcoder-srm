from rmq import RMQ

class TestRMQ:
    def test5(self):
        n = 5
        rmq = RMQ(n)
        rmq[n-1] = 0
        assert rmq.query(n-1, n) == 0
        assert rmq[n-1] == 0
        rmq[n-2] = 2
        assert rmq.query(n-2, n-1) == 2
        assert rmq[n-2] == 2
        assert rmq.query(n-2, n) == 0

