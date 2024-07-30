import sys
from datetime import datetime, timezone
import json

# current_utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
history_list = json.loads(sys.argv[1])

def list_to_markdown(history_list):
    markdown = [
        '|||_Human_||||_Stockfish_||',
        '|-|-|:-:|-|:-:|:-:|:-:|:-:|',
        '|**No**|**Date and Time**|**Profile Pic**|**Username**|**From**|**To**|**From**|**To**|'
    ]   

    for i, move in enumerate(history_list):
        datetime_obj = datetime.strptime(move['datetime'], "%Y-%m-%d %H:%M:%S")
        username = move['human']['username']
        username_from = move['human']['from']
        username_to = move['human']['to']
        stockfish_from = move['stockfish']['from']
        stockfish_to = move['stockfish']['to']

        markdown.append(f'|{i + 1}|`{datetime_obj.strftime("%d/%m/%y")}` `{datetime_obj.strftime("%H:%M:%S")}`|<img src="https://github.com/{username}.png" height="50px" /> | [`{username}`](https://github.com/{username})|`{username_from}`|`{username_to}`|`{stockfish_from}`|`{stockfish_to}`|')

    return markdown

print("\n".join(list_to_markdown(history_list)))
