import os

from crawlora_flashscore import FlashscoreClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FlashscoreClient(api_key=api_key) as client:
    sports = client.sports()
    print('sports', sports)
    scores = client.scores(sport='football', day_offset=0)
    print('scores', scores)
