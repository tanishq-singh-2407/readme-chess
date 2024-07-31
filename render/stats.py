import sys
import json

counts = json.loads(sys.argv[1])

markdown = [
     "| game | count |",
     "|------|-------|",
    f"| humans | {counts['humans']} |",
    f"| stockfish | {counts['stockfish']} |",
    f"| draw | {counts['draw']} |"
]

print("\n".join(markdown))
