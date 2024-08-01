import chess
import sys

game_fen = sys.argv[1]

def list_possible_moves(fen):
    move_list = {}
    board = chess.Board(fen)
    legal_moves = list(board.legal_moves)

    for move in legal_moves:
        from_square = chess.square_name(move.from_square)
        to_square = chess.square_name(move.to_square)

        if from_square not in move_list:
            move_list[from_square] = []

        move_list[from_square].append(to_square)

    return move_list

def list_to_markdown(move_list):
    markdown_lines = ['| From |  To  |', '|------|------|']

    for from_move in move_list:
        line = f"|  {from_move}  | "
        
        for i in range(0, len(move_list[from_move])):
            to_move = move_list[from_move][i]
            line += f"[{to_move}](https://github.com/tanishq-singh-2407/readme-chess/issues/new?title=chess_move_{from_move}{to_move}&labels=make+move&body=Just+push+%27Submit+new+issue%27.+You+don%27t+need+to+do+anything+else.), "

        line = line[:-2] + " |"
        markdown_lines.append(line)

    return "\n".join(markdown_lines)

print(list_to_markdown(list_possible_moves(game_fen)))
