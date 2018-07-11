class Solution:
    def exclusiveTime(self, n, logs):
        x_time = [0] * n
        stack = []
        for line in logs:
            fid, tag, ts = line.split(':')
            fid, ts = int(fid), int(ts)
            if tag == 'start':
                stack.append((fid, ts))
            else:
                _, start = stack.pop()
                end = ts
                dur = end - start + 1
                x_time[fid] += dur
                if stack:
                    p_fid = stack[-1][0]
                    x_time[p_fid] -= dur
        return x_time