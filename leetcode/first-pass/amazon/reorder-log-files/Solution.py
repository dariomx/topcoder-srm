class Solution:
    def reorderLogFiles(self, logs):
        keys = []
        n = len(logs)
        for i in range(n):
            toks = logs[i].split()
            if toks[1].isdigit():
                k = (1, i, "")
            else:
                k = (0, " ".join(toks[1:]), toks[0])
            keys.append(k)
        perm = sorted(range(n), key=lambda i: keys[i])
        return [logs[i] for i in perm]

