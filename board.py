from pieces import King
from pieces import Queen
from pieces import Rook
from pieces import Bishop
from pieces import Knight
from pieces import Pawn


class Board:
    start_board = {
                   Pawn('white'): (6, 0),
                   Pawn('white'): (6, 1),
                   Pawn('white'): (6, 2),
                   Pawn('white'): (6, 3),
                   Pawn('white'): (6, 4),
                   Pawn('white'): (6, 5),
                   Pawn('white'): (6, 6),
                   Pawn('white'): (6, 7),
                   Rook('white'): (7, 0),
                   Knight('white'): (7, 1),
                   Bishop('white'): (7, 2),
                   Queen('white'): (7, 3),
                   King('white'): (7, 4),
                   Bishop('white'): (7, 5),
                   Knight('white'): (7, 6),
                   Rook('white'): (7, 7),
                   Pawn('black'): (0, 0),
                   Pawn('black'): (0, 1),
                   Pawn('black'): (0, 2),
                   Pawn('black'): (0, 3),
                   Pawn('black'): (0, 4),
                   Pawn('black'): (0, 5),
                   Pawn('black'): (0, 6),
                   Pawn('black'): (0, 7),
                   Rook('black'): (1, 0),
                   Knight('black'): (1, 1),
                   Bishop('black'): (1, 2),
                   Queen('black'): (1, 3),
                   King('black'): (1, 4),
                   Bishop('black'): (1, 5),
                   Knight('black'): (1, 6),
                   Rook('black'): (1, 7),
                   }

    def __init__(self):
        self.board = {}
        for piece in self.start_board:
            self.board[piece] = self.start_board[piece]

    def board_array(self):
        board = [[None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None],
                 [None, None, None, None, None, None, None, None]]
        for piece in self.board:
            board[self.board[piece][0]][self.board[piece][1]] = piece
        return board

    def piece_at(self, location):
        x = location[0]
        y = location[1]
        return self.board_array()[x][y]

    def move_piece(self, from_loc, to_loc):
        self.board[self.piece_at(from_loc)] = to_loc


#Both of the sides use an unordered list to store the positions of the chess pieces
# class WhiteSide:
#     color_white = True
#
#     def __init__(self): #add controller(player object) attribute that stores positions of pieces
#         self.pieces = [Pawn(True, (6, 0)),
#                        Pawn(True, (6, 1)),
#                        Pawn(True, (6, 2)),
#                        Pawn(True, (6, 3)),
#                        Pawn(True, (6, 4)),
#                        Pawn(True, (6, 5)),
#                        Pawn(True, (6, 6)),
#                        Pawn(True, (6, 7)),
#                        Rook(True, (7, 0)),
#                        Knight(True, (7, 1)),
#                        Bishop(True, (7, 2)),
#                        Queen(True, (7, 3)),
#                        King(True, (7, 4)),
#                        Bishop(True, (7, 5)),
#                        Knight(True, (7, 6)),
#                        Rook(True, (7, 7))
#                        ]
#
#
# class BlackSide:
#     color_white = False
#
#     def __init__(self): #add controller(player object) attribute that stores positions of pieces
#         self.pieces = [Pawn(False, (0, 0)),
#                        Pawn(False, (0, 1)),
#                        Pawn(False, (0, 2)),
#                        Pawn(False, (0, 3)),
#                        Pawn(False, (0, 4)),
#                        Pawn(False, (0, 5)),
#                        Pawn(False, (0, 6)),
#                        Pawn(False, (0, 7)),
#                        Rook(False, (1, 0)),
#                        Knight(False, (1, 1)),
#                        Bishop(False, (1, 2)),
#                        Queen(False, (1, 3)),
#                        King(False, (1, 4)),
#                        Bishop(False, (1, 5)),
#                        Knight(False, (1, 6)),
#                        Rook(False, (1, 7))
#                        ]
