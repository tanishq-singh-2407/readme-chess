import sys
import chess

def is_valid_uci_move(uci_move):
    if len(uci_move) != 4:
        return False
    if not (uci_move[0] in 'abcdefgh' and uci_move[1] in '12345678'):
        return False
    if not (uci_move[2] in 'abcdefgh' and uci_move[3] in '12345678'):
        return False
    return True

game_fen = sys.argv[1]
move = sys.argv[2]

board = chess.Board(game_fen)

if is_valid_uci_move(move) and chess.Move.from_uci(move) in board.legal_moves:
    print("yes")
else:
    print("no")
