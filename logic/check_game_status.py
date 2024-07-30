import chess
import sys

is_game_draw = lambda board: True if board.is_stalemate() or board.can_claim_draw() or board.can_claim_threefold_repetition() or board.is_insufficient_material() else False

game_fen = sys.argv[1]
board = chess.Board(game_fen)

if board.is_checkmate():
    print("checkmate")

elif is_game_draw(board):
    print("draw")

else:
    print("stillon")
