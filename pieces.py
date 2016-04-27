class Piece:
    black_char = 'x'
    white_char = 'x'
    char = 'x'
    move_patterns = ()
    captured = False

    def __init__(self, color):
        if color == 'white':
            self.white_color = True
        elif color == 'black':
            self.white_color = False
        else:
            print('Error: A piece was created and its color was not defined correctly')
        if self.white_color:
            self.char = self.white_char
        elif not self.white_color:
            self.char = self.white_char


class MovePattern:
    def __init__(self, map):
        pass


class King(Piece):
    black_char = '♚'
    white_char = '♔'


class Queen(Piece):
    black_char = '♛'
    white_char = '♕'


class Rook(Piece):
    black_char = '♜'
    white_char = '♖'


class Bishop(Piece):
    black_char = '♝'
    white_char = '♗'


class Knight(Piece):
    black_char = '♞'
    white_char = '♘'


class Pawn(Piece):
    black_char = '♟'
    white_char = '♙'
