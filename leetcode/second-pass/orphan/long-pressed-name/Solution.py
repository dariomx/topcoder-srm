class Solution:
    def uniq_cnt(self, arr):
        uniq = []
        cnt = []
        for x in arr:
            if not uniq or x != uniq[-1]:
                uniq.append(x)
                cnt.append(1)
            else:
                cnt[-1] += 1
        return uniq, cnt

    def isLongPressedName(self, name, typed):
        uname, cname = self.uniq_cnt(name)
        utyped, ctyped = self.uniq_cnt(typed)
        return uname == utyped and \
               all((x <= y for x, y in zip(cname, ctyped)))
