class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        def write_last(last, chars, i, cnt):
            if last is not None:
                chars[i] = last
                i += 1
                if cnt > 1:
                    for d in str(cnt):
                        chars[i] = d
                        i += 1
            return i

        # main
        i = 0
        last = None
        cnt = 0
        for c in chars:
            if c == last:
                cnt += 1
            else:
                i = write_last(last, chars, i, cnt)
                last = c
                cnt = 1
        return write_last(last, chars, i, cnt)
