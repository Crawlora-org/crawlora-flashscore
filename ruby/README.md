# Crawlora Flashscore API client for Ruby (`crawlora-flashscore`)

This Ruby gem calls Crawlora's hosted Flashscore API at `https://api.crawlora.net/api/v1`. It exposes 54 endpoints covering scores, match details, competitions, teams, players, odds, and news; it does not call or scrape Flashscore directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-flashscore"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/flashscore"

client = Crawlora::Flashscore::Client.new
result = client.request("flashscore-search", JSON.parse("{\"q\": \"football\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 54 API operations.

```ruby
client = Crawlora::Flashscore::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Flashscore API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-flashscore/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-flashscore) for account setup, the API operation reference, and release history.
