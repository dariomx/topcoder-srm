class Solution:
    def addOperators(self, num, target):
        if len(num) == 0:
            return []
        num = list(map(int, num))
        ans = []

        def rec_app(i, src, dst):
            if i == len(src):
                rec_mul(1, dst, [dst[0]], [str(dst[0])])
            else:
                if dst[-1] > 0:
                    last = dst.pop()
                    dst.append(last * 10 + src[i])
                    rec_app(i + 1, src, dst)
                    dst.pop()
                    dst.append(last)
                dst.append(src[i])
                rec_app(i + 1, src, dst)
                dst.pop()

        def rec_mul(i, src, dst, exp):
            if i == len(src):
                rec_add(1, dst, exp, dst[0], exp[0])
            else:
                last = dst.pop()
                last_exp = exp.pop()
                dst.append(last * src[i])
                exp.append(last_exp + '*' + str(src[i]))
                rec_mul(i + 1, src, dst, exp)
                dst.pop()
                exp.pop()
                dst.append(last)
                exp.append(last_exp)
                dst.append(src[i])
                exp.append(str(src[i]))
                rec_mul(i + 1, src, dst, exp)
                dst.pop()
                exp.pop()

        def rec_add(i, src, src_exp, res, exp):
            if i == len(src):
                if res == target:
                    ans.append(exp)
            else:
                x = src[i]
                xs = src_exp[i]
                rec_add(i + 1, src, src_exp, res + x, exp + '+' + xs)
                rec_add(i + 1, src, src_exp, res - x, exp + '-' + xs)

        rec_app(1, num, [num[0]])
        return ans