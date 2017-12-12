class PeopleCircle:
    def move(self, places, start, size, deleted):
        if len(deleted) == size:
            return start
        cnt = 0
        i = start
        while cnt < places:
            i = (i + 1) % size
            if i not in deleted:
                cnt += 1
        return i

    def order(self, numMales, numFemales, K):
        n = numMales + numFemales
        state = ["M"] * n
        deleted = set()
        i = 0
        cnt = 0
        while cnt < numFemales:
            i = self.move(K-1, i, n, deleted)
            state[i] = "F"
            deleted.add(i)
            i = self.move(1, i, n, deleted)
            cnt += 1
        return "".join(state)

    def test(self, str, numMales, numFemales, K):
        state = list(str)
        n = numFemales + numFemales
        i = 0
        cnt = 0
        while cnt < numFemales:
            print("".join(state))
            i = (i+K-1) % n
            del_idx = i
            print("deleting " + state[del_idx])
            state.pop(del_idx)
            cnt += 1
            n -= 1
        return "".join(state)

#print(PeopleCircle().order(5, 3, 2))
#print(PeopleCircle().order(7, 3, 1))
print(PeopleCircle().order(0, 1, 23))
#print(PeopleCircle().test(PeopleCircle().order(25, 25, 1000), 25, 25, 1000))
#print(PeopleCircle().test("MMMMMFFFFFFMFMFMMMFFMFFFFFFFFFMMMMMMMFFMFMMMFMFMMF",25, 25, 1000))
