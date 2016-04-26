class Piece:
    black_char = 'x'
    white_char = 'x'
    char = 'x'
    move_patterns = ()
    location = []
    captured = False

    def __init__(self, color, location):
        self.white_color = color
        self.location = location
        if self.white_color:
            self.char = self.white_char
        elif not self.white_color:
            self.char = self.white_char


class MovePattern:
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
