import chess
import chess.engine
import os
import sys

STOCKFISH_PATH = os.path.join(os.getcwd(), "chess/stockfish", "16_x64_binary")

game_fen = sys.argv[1]
board = chess.Board(game_fen)

engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
result = engine.play(board, chess.engine.Limit(time=.5))

board.push(result.move)
engine.quit()

print(board.fen())
