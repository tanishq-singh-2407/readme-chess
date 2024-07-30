import sys


count_human = sys.argv[1]
count_stockfish = sys.argv[2]
count_draw = sys.argv[3]

count_list = ["human", "stockfish", "draw"]

markdown = [
     "| game      | count             |",
     "|-----------|-------------------|",
    f"| human     | {count_human}     |",
    f"| stockfish | {count_stockfish} |",
    f"| draw      | {count_draw}      |"
]

print("\n".join(markdown))
