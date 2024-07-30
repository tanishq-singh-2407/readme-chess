import sys

winner_name = sys.argv[1]

markdown = [
    f"|{winner_name} (winner)|one more game?|",
     "|----------------------|:------------:|",
     "|![Alt Text](./Michael_Sprays_Champagne.gif)|for restart [click here](https://github.com/tanishq-singh-2407/tanishq-singh-2407/issues/new?title=chess_restart&body=Just+push+%27Submit+new+issue%27.+You+don%27t+need+to+do+anything+else.)|"
]

print("\n".join(markdown))
