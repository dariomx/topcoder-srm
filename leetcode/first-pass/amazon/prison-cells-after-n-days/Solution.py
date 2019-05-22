class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        k = 8  # not really arbitrary to capped on maximum #bits to fit in
        # integer
        mask_k = 2 ** k - 1
        trans = [None] * (mask_k + 1)

        def gbit(x, i):
            return (x & (1 << (k - 1 - i))) >> (k - 1 - i)

        def sbit(x, i, bit):
            off_i = ~(1 << (k - 1 - i)) & mask_k
            return (x & off_i) | (bit << (k - 1 - i))

        def next_state(state):
            nstate = 0
            for i in range(1, k - 1):
                bit = int(gbit(state, i - 1) == gbit(state, i + 1))
                nstate = sbit(nstate, i, bit)
            return nstate

        def dist(start, end):
            d = 0
            state = start
            while state != end:
                d += 1
                state = trans[state]
            return d

        def handle_cycle(start, state, day):
            cycle_size = day - dist(start, state)
            for _ in range((N - day) % cycle_size):
                state = trans[state]
            return state

        # main
        start = int("".join(map(str, cells)), 2)
        state = start
        for day in range(N):
            if trans[state] is None:
                trans[state] = next_state(state)
                state = trans[state]
            else:
                state = handle_cycle(start, state, day)
                break
        return [int(b) for b in format(state, "0%db" % k)]
