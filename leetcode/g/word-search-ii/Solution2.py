class Solution(object):
    def search_dfs(self, x, y, word, board, rev=False):
        n, m = len(board), len(board[0])
        visited = set()
        stack = [((x, y), [board[x][y]])]
        while stack:
            (x, y), path = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if len(path) > len(word):
                continue
            w = ''.join(path)
            print(w)
            if rev:
                w = w[::-1]
            if word == w:
                return True
            for (w, z) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= w < n and 0 <= z < m:
                    stack.append(((w, z), path + [board[w][z]]))
        return False

    def search_word(self, word, board):
        n, m = len(board), len(board[0])
        for (x, y) in ((i, j) for i in xrange(n) for j in xrange(m)):
            found = (board[x][y] == word[0] and \
                     self.search_dfs(x, y, word, board)) or \
                    (board[x][y] == word[-1] and \
                     self.search_dfs(x, y, word, board, rev=True))
            if found:
                return True
        return False

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
        found = []
        for w in words:
            if self.search_word(w, board):
                found.append(w)
        return found
