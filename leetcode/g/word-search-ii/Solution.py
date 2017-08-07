class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(board)
        if n > 0:
            m = len(board[0])
        if 0 in (n, m):
            return []
        words = set(words)
        found = set()
        visited = set()
        stack = [((0, 0), [board[0][0]])]
        while stack:
            (x, y), path = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            w = ''.join(path)
            for i in xrange(0, len(w)):
                wk = w[i:]
                print(wk)
                if wk in words:
                    found.add(wk)
                r_wk = wk[::-1]
                print(r_wk)
                if r_wk in words:
                    found.add(r_wk)
            for (w, z) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= w < n and 0 <= z < m:
                    stack.append(((w, z), path + [board[w][z]]))
        return list(found)
