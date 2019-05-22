class Solution:
    def countAndSay(self, n):
        seq = "1"
        if n == 1:
            return seq
        for _ in range(n - 1):
            nseq = ""
            cnt = 0
            for i in range(len(seq)):
                if i == 0 or seq[i - 1] == seq[i]:
                    cnt += 1
                else:
                    nseq += str(cnt) + seq[i - 1]
                    cnt = 1
            if cnt > 0:
                nseq += str(cnt) + seq[-1]
            seq = nseq
        return seq

