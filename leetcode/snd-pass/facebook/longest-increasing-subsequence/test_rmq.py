from random import randint, seed

import pytest

from rmq import RMQ

RAND_SEED = 666
RAND_N = 1000
seed(RAND_SEED)
RAND_A = [randint(0, RAND_N) for _ in range(RAND_N)]

class TestRMQ:
    @pytest.mark.parametrize('A',
                             [
                                 [10, 9, 2, 5, 3, 7, 101, 18],
                                 [666],
                                 [4, 3, 2, 1],
                                 RAND_A
                             ])
    def test_find_max(self, A):
        n = len(A)
        rmq = RMQ(A)
        for i in range(n):
            for j in range(i, n):
                subA = A[i:(j + 1)]
                exp_max = i + subA.index(max(subA))
                act_max = rmq.find_max(i, j)
                assert act_max == exp_max, '%d, %d' % (i, j)
