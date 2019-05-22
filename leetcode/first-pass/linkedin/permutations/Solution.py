class Solution(object):
    def permute(self, nums):
        def perm(xs):
            if len(xs) <= 1:
                yield xs
            else:
                x = xs[0]
                for p in perm(xs[1:]):
                    for i in range(len(p) + 1):
                        p.insert(i, x)
                        yield list(p)
                        p.pop(i)

        return list(perm(nums))


