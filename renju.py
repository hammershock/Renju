import numpy as np


class Board:
    def __init__(self, board_shape):
        self.board_shape = board_shape
        self.grids = np.zeros((board_shape, board_shape))
        self.turn = 1
        self.finished = False
    
    @property
    def status_message(self) -> str:
        if not self.finished:
            return 'waiting for black' if self.turn == 1 else "waiting for white"
        else:
            return 'black wins' if self.turn == -1 else 'white wins'
    
    def drop(self, row, col):
        success = False
        if not self.finished and 0 <= row < self.board_shape and self.board_shape > col >= 0 == self.grids[row][col]:
            self.grids[row][col] = self.turn
            self.finished = self._check(row, col)
            self.turn = -self.turn
            success = True
        return success, self.finished, self.status_message
    
    def _check(self, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 0
            for i in range(-4, 5):
                x = row + i * dx
                y = col + i * dy
                if 0 <= x < self.board_shape and 0 <= y < self.board_shape and self.grids[x][y] == self.turn:
                    count += 1
                    if count == 5:
                        return True
                else:
                    count = 0
        return False
