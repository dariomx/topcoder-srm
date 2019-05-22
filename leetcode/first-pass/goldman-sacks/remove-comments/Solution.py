class Solution:
    def removeComments(self, source):
        ans = ['']
        comment = False
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if line[i] == '/' and i+1 < n and line[i+1] == '/' and not comment:
                    break
                elif line[i] == '/' and i+1 < n and line[i+1] == '*' and not comment:
                    comment = True
                    i += 2
                elif line[i] == '*' and i+1 < n and line[i+1] == '/' and comment:
                    comment = False
                    i += 2
                elif comment:
                    i += 1
                else:
                    ans[-1] += line[i]
                    i += 1
            if ans[-1] and not comment:
                ans.append('')
        if not ans[-1]:
            ans.pop()
        return ans