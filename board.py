from pieces import King
from pieces import Queen
from pieces import Rook
from pieces import Bishop
from pieces import Knight
from pieces import Pawn


#Uses a list to store the positions of its chess pieces
class Board:
    empty_board = [[None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None],
                   [None, None, None, None, None, None, None, None]]

    def __init__(self):
        self.board = self.empty_board
        self.white_side = WhiteSide()
        self.black_side = BlackSide()
        self.compose_board()

    def compose_board(self):
        self.board = self.empty_board
        for piece in self.white_side.pieces + self.black_side.pieces:
            self.board[piece.location[0]][piece.location[1]] = piece
        return self.board

    def piece_at(self, position):
        return self.board[position[0]][position[1]]


#Both of the sides use an unordered list to store the positions of the chess pieces
class WhiteSide:
    color_white = True

    def __init__(self): #add controller(player object) attribute that stores positions of pieces
        self.pieces = [Pawn(True, (6, 0)),
                       Pawn(True, (6, 1)),
                       Pawn(True, (6, 2)),
                       Pawn(True, (6, 3)),
                       Pawn(True, (6, 4)),
                       Pawn(True, (6, 5)),
                       Pawn(True, (6, 6)),
                       Pawn(True, (6, 7)),
                       Rook(True, (7, 0)),
                       Knight(True, (7, 1)),
                       Bishop(True, (7, 2)),
                       Queen(True, (7, 3)),
                       King(True, (7, 4)),
                       Bishop(True, (7, 5)),
                       Knight(True, (7, 6)),
                       Rook(True, (7, 7))
                       ]


class BlackSide:
    color_white = False

    def __init__(self): #add controller(player object) attribute that stores positions of pieces
        self.pieces = [Pawn(False, (0, 0)),
                       Pawn(False, (0, 1)),
                       Pawn(False, (0, 2)),
                       Pawn(False, (0, 3)),
                       Pawn(False, (0, 4)),
                       Pawn(False, (0, 5)),
                       Pawn(False, (0, 6)),
                       Pawn(False, (0, 7)),
                       Rook(False, (1, 0)),
                       Knight(False, (1, 1)),
                       Bishop(False, (1, 2)),
                       Queen(False, (1, 3)),
                       King(False, (1, 4)),
                       Bishop(False, (1, 5)),
                       Knight(False, (1, 6)),
                       Rook(False, (1, 7))
                       ]
