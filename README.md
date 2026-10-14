# Flashscore clients for Crawlora

Official Crawlora client packages for the hosted Flashscore API. Access 54 API endpoints covering scores, match details, competitions, teams, players, odds, and news from JavaScript/TypeScript, Python, Go, Ruby, Java, and PHP. These clients call Crawlora's hosted API; they do not scrape Flashscore locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Flashscore or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/flashscore`](javascript/README.md)
- Python: [`crawlora-flashscore`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-flashscore`](go.mod)
- Ruby: [`crawlora-flashscore`](ruby/README.md)
- Java: [`net.crawlora:crawlora-flashscore:0.3.6`](java/README.md)
- PHP: [`crawlora/flashscore`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=flashscore-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The six language clients provide access to all 54 selected public Flashscore API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

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

## License

MIT. See [LICENSE](LICENSE).
