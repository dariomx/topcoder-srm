from collections import deque


class IntBoard:
    def __init__(self, board=None, state=None):
        self.int = 0
        self.mask32 = 0xffffffff
        self.mask3 = 0x00000007
        if (board is None) == (state is None):
            raise ValueError('Need either board or state')
        elif board is not None:
            if self._valid_state(board):
                self._load(board)
            else:
                raise ValueError('Invalid initial state for board')
        else:
            self.int = state

    def _valid_state(self, board):
        if len(board) != 2:
            return False
        if len(board[0]) != 3 or len(board[1]) != 3:
            return False
        for i in range(2):
            for j in range(3):
                if not (0 <= board[i][j] <= 5):
                    return False
        return True

    def _load(self, board):
        for i in range(2):
            for j in range(3):
                self[i, j] = board[i][j]

    def __getitem__(self, pos):
        shift = self._pos2shift(pos)
        return self._cell_mask(shift) >> shift

    def __setitem__(self, pos, val):
        if not (0 <= val <= 5):
            raise ValueError('Invalid cell value %d' % val)
        shift = self._pos2shift(pos)
        self.int &= ~self._cell_mask(shift)
        self.int |= (val & self.mask32) << shift

    def _pos2shift(self, pos):
        i, j = pos
        k = 3 * i + j
        return k * 3

    def _cell_mask(self, shift):
        return ((self.int & self.mask32) & (self.mask3 << shift))

    def swap(self, pos1, pos2):
        tmp = self[pos1]
        self[pos1] = self[pos2]
        self[pos2] = tmp

    def get_state(self):
        return self.int & self.mask32

    def set_state(self, state):
        self.int = state & self.mask32

    def get_board(self):
        board = [[0, 0, 0], [0, 0, 0]]
        for i in range(2):
            for j in range(3):
                board[i][j] = self[i, j]
        return board


class Solution:
    def _neighbors(self, pos):
        i, j = pos
        for di, dj in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
            ni, nj = i + di, j + dj
            if (i, j) == (ni, nj):
                continue
            if not (0 <= ni < 2 and 0 <= nj < 3):
                continue
            yield ni, nj

    def _zero_pos(self, board):
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    return i, j
        raise ValueError('Could not find zero')

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        goalState = IntBoard([[1, 2, 3], [4, 5, 0]]).get_state()
        iBoard = IntBoard(board)
        iniState = iBoard.get_state()
        zeroPos = self._zero_pos(board)
        queue = deque([(iniState, zeroPos, 0)])
        visited = set([iniState])
        while queue:
            state, pos, moves = queue.popleft()
            if state == goalState:
                return moves
            for nei_pos in self._neighbors(pos):
                iBoard.set_state(state)
                iBoard.swap(pos, nei_pos)
                new_state = iBoard.get_state()
                if new_state in visited:
                    continue
                visited.add(new_state)
                queue.append((new_state, nei_pos, moves + 1))
        return -1