class Solution:
    def generate(self, numRows):
        pt = [[1], [1, 1]]
        if numRows <= 2:
            return pt[:numRows]
        else:
            for i in range(2, numRows):
                pt.append([1])
                for j in range(1, i):
                    pt[i].append(pt[i - 1][j - 1] + pt[i - 1][j])
                pt[i].append(1)
            return pt
