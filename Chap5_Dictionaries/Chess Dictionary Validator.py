chess_pieces = {
    "1h": "bking",
    "6c": "wqueen",
    "2g": "bbishop",
    "5h": "bqueen",
    "3e": "wking",
}  # position: colorpiece

piece = {
    "w": {  # white pieces
        "pawn": 8,
        "knight": 2,
        "bishop": 2,
        "rook": 2,
        "queen": 1,
        "king": 1,
    },
    "b": {  # black pieces
        "pawn": 8,
        "knight": 2,
        "bishop": 2,
        "rook": 2,
        "queen": 1,
        "king": 1,
    },
}

# the chess board has 1a to 8h as valid spaces
number = {1, 2, 3, 4, 5, 6, 7, 8}
letter = {"a", "b", "c", "d", "e", "f", "g", "h"}

piece_choice = input("Enter your chess piece of choice: ")


def isValidChessBoard():
    if "w" or "b" in piece.key():
        return True
        print("This is a valid piece.")

    else:
        return False
        print("This is not a valid piece.")


isValidChessBoard()
