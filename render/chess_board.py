import chess
import random
import sys

pieces_folder = sys.argv[2]
game_fen = sys.argv[1]

def fen_to_markdown(fen, pieces_folder):
    board = chess.Board(fen)
    piece_to_svg = {
        'r': 'rook-b.jpg',
        'n': 'knight-b.jpg',
        'b': 'bishop-b.jpg',
        'q': 'queen-b.jpg',
        'k': 'king-b.jpg',
        'p': 'pawn-b.jpg',
        'R': 'rook-w.jpg',
        'N': 'knight-w.jpg',
        'B': 'bishop-w.jpg',
        'Q': 'queen-w.jpg',
        'K': 'king-w.jpg',
        'P': 'pawn-w.jpg',
    }

    markdown_lines = ["|   | a | b | c | d | e | f | g | h |", "|---|---|---|---|---|---|---|---|---|"]

    for rank in range(8, 0, -1):
        line = f"| {rank} "

        for file in range(1, 9):
            square = chess.square(file - 1, rank - 1)
            piece = board.piece_at(square)

            if piece:
                piece_svg = piece_to_svg.get(piece.symbol(), "")
                line += f"| ![piece](./{pieces_folder}/{piece_svg}) "

            else:
                bg_no = random.randint(1, 5)
                line += f"| ![piece](./{pieces_folder}/bg-{bg_no}.jpg) "

        line += "|"
        markdown_lines.append(line)
    
    markdown_lines.append("|   | a | b | c | d | e | f | g | h |")
    return "\n".join(markdown_lines)

print(fen_to_markdown(game_fen, pieces_folder))
