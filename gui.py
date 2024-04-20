import pygame

from renju import Board


class RenjuGui:
    def __init__(self, board_size=1200, board_margin=20, piece_margin=4, board_shape=22):
        """
        
        :param board_size: 棋盘长宽(pixels)
        :param board_margin: 棋盘边缘像素(pixels)
        :param piece_margin: 棋子边缘像素(pixels)
        :param board_shape: 棋盘长宽
        """
        self.board = Board(board_shape)
        self.board_size = board_size
        self.board_margin = board_margin
        self.piece_margin = piece_margin
        self.board_shape = board_shape
        
        self.cell_size = (board_size - 2 * board_margin) // board_shape
        self.piece_size = self.cell_size - piece_margin * 2
        self.screen = pygame.display.set_mode((board_size, board_size))
        pygame.display.set_caption("五子棋")
        
        # resources
        self.background = pygame.transform.scale(pygame.image.load('./assets/background.png'), (board_size, board_size))
        self.black = pygame.transform.scale(pygame.image.load('./assets/black.png'), (self.piece_size, self.piece_size))
        self.white = pygame.transform.scale(pygame.image.load('./assets/white.png'), (self.piece_size, self.piece_size))
    
    def _draw_board(self, grids):
        self.screen.blit(self.background, (0, 0))
        
        for row in range(self.board_shape):
            for col in range(self.board_shape):
                x = self.board_margin + col * self.cell_size
                y = self.board_margin + row * self.cell_size
                pygame.draw.rect(self.screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size), 1)
                
                if grids[row][col] == 1:
                    self.screen.blit(self.black, (x + self.piece_margin, y + self.piece_margin))
                elif grids[row][col] == -1:
                    self.screen.blit(self.white, (x + self.piece_margin, y + self.piece_margin))
                    
    def run(self):
        pygame.init()

        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    row = round((y - self.board_margin + self.cell_size // 2) / self.cell_size) - 1
                    col = round((x - self.board_margin + self.cell_size // 2) / self.cell_size) - 1
                    
                    success, finished, message = self.board.drop(row, col)
                    # if success and finished:
                    print(message)
            
            self._draw_board(self.board.grids)
            pygame.display.flip()
        
        pygame.quit()
        
        
if __name__ == '__main__':
    game = RenjuGui()
    game.run()

    