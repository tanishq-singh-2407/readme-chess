import chess
import sys

game_fen = sys.argv[1]
uci_move = sys.argv[2]

board = chess.Board(game_fen)
board.push(chess.Move.from_uci(uci_move))

print(board.fen())
