from collections import defaultdict


class Solution:
    def exclusiveTime(self, n, logs):
        ftime = [0] * n
        stack = []
        for line in logs:
            id, tag, time = line.split(":")
            id = int(id)
            time = int(time)
            if tag == "start":
                stack.append((id, time))
            else:
                end = time
                _, start = stack.pop()
                dur = end - start + 1
                ftime[id] += dur
                if stack:
                    ftime[stack[-1][0]] -= dur
        return ftime
