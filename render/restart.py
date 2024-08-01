import sys

winner_name = sys.argv[1]

markdown = [
    f"|{winner_name} (winner)|one more game?|",
     "|----------------------|:------------:|",
     "|![Alt Text](./assets/winner.gif)|for restart [click here](https://github.com/tanishq-singh-2407/readme-chess/issues/new?title=chess_restart&body=Just+push+%27Submit+new+issue%27.+You+don%27t+need+to+do+anything+else.)|"
]

print("\n".join(markdown))
