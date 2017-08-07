from collections import defaultdict


class Solution(object):
    def search_dfs(self, x, y, word, board, visited, path, rev=False):
        if (x, y) in visited or len(path) > len(word):
            return False
        w = ''.join(path)
        if rev:
            w = w[::-1]
        # print(w)
        if w == word:
            return True
        n, m = len(board), len(board[0])
        for (w, z) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            visited.add((x, y))
            if 0 <= w < n and 0 <= z < m and \
                    self.search_dfs(w, z, word, board, visited, \
                                    path + [board[w][z]], rev):
                return True
            visited.remove((x, y))
        return False

    def search_word(self, word, board, char_pos):
        visited = set()
        fwd_pos = [(pos, False) for pos in char_pos[word[0]]]
        rev_pos = [(pos, True) for pos in char_pos[word[-1]]]
        for (x, y), rev in (fwd_pos + rev_pos):
            visited.clear()
            c = board[x][y]
            found = self.search_dfs(x, y, word, board, visited, [c], rev=rev)
            if found:
                return True
        return False

    def get_char_pos(self, board):
        char_pos = defaultdict(list)
        n, m = len(board), len(board[0])
        for (x, y) in ((i, j) for i in xrange(n) for j in xrange(m)):
            char_pos[board[x][y]].append((x, y))
        return char_pos

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
        char_pos = self.get_char_pos(board)
        for w in words:
            if self.search_word(w, board, char_pos):
                found.append(w)
        return list(set(found))
