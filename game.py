import time
import board
from player import Player


class Game:
    def __init__(self):
        self.start_time = time.time()
        self.game_board = board.Board()
        self.player_white = Player()
        self.player_black = Player()
        self.player_white.my_turn = True

    def display_board(self):
        current_board = self.game_board.board_array()
        current_row_display = 'Board:'
        for x in current_board:
            print(current_row_display)
            current_row_display = ''
            for y in x:
                if y == 0:
                    current_row_display += '- '
                else:
                    current_row_display += (str(y.char) + ' ')
        print(current_row_display)

    def move_piece(self, from_loc, to_loc):
        self.game_board.move_piece(from_loc, to_loc)
        self.display_board()

    def get_info(self, player):
        pass

    def turn(self):
        pass