# crawlora-flashscore — Flashscore API client for Python

Python client for Crawlora's hosted Flashscore API. It exposes 54 API endpoints covering scores, match details, competitions, teams, players, odds, and news. Requests go to [Crawlora](https://crawlora.net/?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-python-homepage); the package does not run a browser or scrape
Flashscore locally. A Crawlora account and `CRAWLORA_API_KEY` are required,
and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by
Flashscore or its owners.

## Install

```sh
python -m pip install crawlora-flashscore
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-python-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=pypi&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-python-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.py`, then run `python example.py` after installing the package and setting your API key.

```python
import os

from crawlora_flashscore import FlashscoreClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with FlashscoreClient(api_key=api_key) as client:
    result_1 = client.sports()
    print(result_1)
    result_2 = client.scores(sport='football', day_offset=0)
    print(result_2)
```

The package also exports `Client` as an alias for `FlashscoreClient`. Operation
methods are available directly in snake_case and through the `flashscore`
group. The async package client is `AsyncFlashscoreClient`; see the [online
endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/docs/usage.md) and [runnable example](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/examples/python.py).

### Async usage

The package also exports `AsyncClient` for asynchronous requests:

```python
import asyncio
import os

from crawlora_flashscore import AsyncClient

async def main():
    api_key = os.environ.get("CRAWLORA_API_KEY")
    if not api_key:
        raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")
    async with AsyncClient(api_key=api_key) as client:
        result_1 = await client.sports()
        print(result_1)

asyncio.run(main())
```

See the [runnable example](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/examples/python.py) for a complete usage example.

## Supported Flashscore API endpoints

This package exposes every route below through direct snake_case methods and the `flashscore` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/flashscore/calendar` | `flashscore-calendar` | Flashscore season calendar |
| `GET` | `/flashscore/calendar-categories` | `flashscore-calendar-categories` | Flashscore season calendar categories |
| `GET` | `/flashscore/competitions` | `flashscore-competitions` | Flashscore competitions by sport and date |
| `GET` | `/flashscore/entity-news` | `flashscore-entity-news` | Flashscore news for a team, player, tournament or sport |
| `GET` | `/flashscore/match-box-score` | `flashscore-match-box-score` | Flashscore basketball, hockey and baseball box score |
| `GET` | `/flashscore/match-darts` | `flashscore-match-darts` | Flashscore darts throw-by-throw and statistics |
| `GET` | `/flashscore/match-h2h` | `flashscore-match-h2h` | Flashscore match head-to-head and recent results |
| `GET` | `/flashscore/match-highlights` | `flashscore-match-highlights` | Flashscore match highlights |
| `GET` | `/flashscore/match-info` | `flashscore-match-info` | Flashscore match venue and broadcast information |
| `GET` | `/flashscore/match-lineups` | `flashscore-match-lineups` | Flashscore match lineups and formations |
| `GET` | `/flashscore/match-missing-players` | `flashscore-match-missing-players` | Flashscore missing and doubtful players |
| `GET` | `/flashscore/match-momentum` | `flashscore-match-momentum` | Flashscore football match momentum |
| `GET` | `/flashscore/match-news` | `flashscore-match-news` | Flashscore match news references |
| `GET` | `/flashscore/match-odds` | `flashscore-match-odds` | Flashscore match bookmaker odds comparison |
| `GET` | `/flashscore/match-player-stats` | `flashscore-match-player-stats` | Flashscore football player match statistics and ratings |
| `GET` | `/flashscore/match-point-by-point` | `flashscore-match-point-by-point` | Flashscore point-by-point scoring history |
| `GET` | `/flashscore/match-predicted-lineups` | `flashscore-match-predicted-lineups` | Flashscore predicted lineups |
| `GET` | `/flashscore/match-report` | `flashscore-match-report` | Flashscore editorial match report |
| `GET` | `/flashscore/match-standings` | `flashscore-match-standings` | Flashscore match league standings |
| `GET` | `/flashscore/match-stats` | `flashscore-match-stats` | Flashscore match statistics |
| `GET` | `/flashscore/match-tv` | `flashscore-match-tv` | Flashscore match TV and streaming broadcasters |
| `GET` | `/flashscore/navigation` | `flashscore-navigation` | Flashscore sport, category, country, and competition navigation |
| `GET` | `/flashscore/news` | `flashscore-news` | Flashscore News listings by section |
| `GET` | `/flashscore/news-article` | `flashscore-news-article` | Flashscore news article metadata |
| `GET` | `/flashscore/news-article-body` | `flashscore-news-article-body` | Flashscore news article with full text |
| `GET` | `/flashscore/news-categories` | `flashscore-news-categories` | Flashscore News categories |
| `GET` | `/flashscore/news-most-read` | `flashscore-news-most-read` | Flashscore most-read news |
| `GET` | `/flashscore/odds-geos` | `flashscore-odds-geos` | Flashscore odds markets, subdivisions and odds enums |
| `GET` | `/flashscore/player` | `flashscore-player` | Flashscore player profile and career |
| `GET` | `/flashscore/player-fixtures` | `flashscore-player-fixtures` | Flashscore player fixtures |
| `GET` | `/flashscore/player-injuries` | `flashscore-player-injuries` | Flashscore player injury history |
| `GET` | `/flashscore/player-match-log` | `flashscore-player-match-log` | Flashscore player match log |
| `GET` | `/flashscore/player-news` | `flashscore-player-news` | Flashscore player news |
| `GET` | `/flashscore/player-results` | `flashscore-player-results` | Flashscore player results |
| `GET` | `/flashscore/player-transfers` | `flashscore-player-transfers` | Flashscore player transfer history |
| `GET` | `/flashscore/ranking-categories` | `flashscore-ranking-categories` | Flashscore ranking categories |
| `GET` | `/flashscore/rankings` | `flashscore-rankings` | Flashscore rankings |
| `GET` | `/flashscore/scores` | `flashscore-scores` | Flashscore scores and fixtures by sport |
| `GET` | `/flashscore/search` | `flashscore-search` | Flashscore search |
| `GET` | `/flashscore/sports` | `flashscore-sports` | Flashscore sports and live category counts |
| `GET` | `/flashscore/team` | `flashscore-team` | Flashscore team profile |
| `GET` | `/flashscore/team-fixtures` | `flashscore-team-fixtures` | Flashscore team fixtures |
| `GET` | `/flashscore/team-news` | `flashscore-team-news` | Flashscore team news headlines |
| `GET` | `/flashscore/team-outright-odds` | `flashscore-team-outright-odds` | Flashscore team title odds |
| `GET` | `/flashscore/team-results` | `flashscore-team-results` | Flashscore team results |
| `GET` | `/flashscore/team-squad` | `flashscore-team-squad` | Flashscore team squad |
| `GET` | `/flashscore/team-transfers` | `flashscore-team-transfers` | Flashscore team transfers |
| `GET` | `/flashscore/top-search` | `flashscore-top-search` | Flashscore top search entities |
| `GET` | `/flashscore/tournament-archive-seasons` | `flashscore-tournament-archive-seasons` | Flashscore competition seasons by stage id |
| `GET` | `/flashscore/tournament-events` | `flashscore-tournament-events` | Flashscore tournament season results or fixtures |
| `GET` | `/flashscore/tournament-outright-odds` | `flashscore-tournament-outright-odds` | Flashscore competition winner odds |
| `GET` | `/flashscore/tournament-seasons` | `flashscore-tournament-seasons` | Flashscore tournament archive seasons |
| `GET` | `/flashscore/tournament-standings` | `flashscore-tournament-standings` | Flashscore competition standings table |
| `GET` | `/flashscore/tournament-standings-views` | `flashscore-tournament-standings-views` | Flashscore competition standings view discovery |

## Configuration

Pass your key through `api_key` or read `CRAWLORA_API_KEY` from the environment.
Keep credentials out of source control and logs. Requests go to Crawlora's
hosted API.
