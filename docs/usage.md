# Flashscore client usage

The `@crawlora-org/flashscore` and `crawlora-flashscore` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Flashscore locally; Crawlora is independent from and not endorsed by Flashscore or its owners.

The package tracks the public API contract revision `sha256:380bb303ffcb6ff808a1db512dcc3bd90c9b7d20d62e64d1b368f37c9a6771bd` bundled with release `0.1.4`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 24 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `flashscore` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)

The Flashscore scores feed preserves its upstream delimited text response.

## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `calendar` / `calendar` | `GET /flashscore/calendar` | `category` (query, required; values: `tennis-atp`, `tennis-wta`, `golf-pga`, `golf-dp-world`, `badminton-bwf`, `motorsport-f1`) | Flashscore season calendar |
| `calendarCategories` / `calendar_categories` | `GET /flashscore/calendar-categories` | — | Flashscore season calendar categories |
| `competitions` / `competitions` | `GET /flashscore/competitions` | `sport` (query, required; values: `football`, `tennis`, `basketball`, `hockey`, `golf`, `formula-1`, `baseball`, `snooker`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `beach-soccer`, `beach-volleyball`, `boxing`, `cricket`, `cycling`, `darts`, `esports`, `field-hockey`, `floorball`, `futsal`, `handball`, `horse-racing`, `kabaddi`, `mma`, `motorsport`, `netball`, `pesapallo`, `rugby-league`, `rugby-union`, `table-tennis`, `volleyball`, `water-polo`, `winter-sports`), `day_offset` (query, optional) | Flashscore competitions by sport and date |
| `matchH2h` / `match_h2h` | `GET /flashscore/match-h2h` | `id` (query, required) | Flashscore match head-to-head and recent results |
| `matchHighlights` / `match_highlights` | `GET /flashscore/match-highlights` | `id` (query, required) | Flashscore match highlights |
| `matchInfo` / `match_info` | `GET /flashscore/match-info` | `id` (query, required) | Flashscore match venue and broadcast information |
| `matchLineups` / `match_lineups` | `GET /flashscore/match-lineups` | `id` (query, required) | Flashscore match lineups and formations |
| `matchNews` / `match_news` | `GET /flashscore/match-news` | `id` (query, required) | Flashscore match news references |
| `matchStandings` / `match_standings` | `GET /flashscore/match-standings` | `id` (query, required), `view` (query, optional; values: `overall`, `home`, `away`, `form_overall`, `overunder_overall`, `form_home`, `form_away`, `top_scorers`, `htft_overall`, `htft_home`, `htft_away`, `live_overall`, `overunder_home`, `overunder_away`) | Flashscore match league standings |
| `matchStats` / `match_stats` | `GET /flashscore/match-stats` | `id` (query, required) | Flashscore match statistics |
| `navigation` / `navigation` | `GET /flashscore/navigation` | `path` (query, optional) | Flashscore sport, category, country, and competition navigation |
| `news` / `news` | `GET /flashscore/news` | `category` (query, optional; values: `all`, `football`, `uefa-nations-league`, `tennis`, `features`, `premier-league`, `nfl`, `mlb`, `nba`, `nhl`, `formula-1`, `champions-league`, `europa-league`, `conference-league`, `darts`, `snooker`, `golf`, `road-cycling`, `laliga`, `bundesliga`, `serie-a`, `ligue-1`, `badminton`, `handball`, `hockey`, `basketball`, `cricket`, `rugby-union`, `athletics`, `baseball`, `fifa`, `rugby-league`, `motorsport`, `aussie-rules`, `flashscore-ratings`, `american-sports`, `african-football`, `combat-sports`, `winter-sports`, `transfer-news`), `page` (query, optional) | Flashscore News listings by section |
| `newsArticle` / `news_article` | `GET /flashscore/news-article` | `id` (query, required) | Flashscore news article metadata |
| `newsCategories` / `news_categories` | `GET /flashscore/news-categories` | — | Flashscore News categories |
| `rankingCategories` / `ranking_categories` | `GET /flashscore/ranking-categories` | — | Flashscore ranking categories |
| `rankings` / `rankings` | `GET /flashscore/rankings` | `category` (query, required; values: `fifa`, `tennis-atp`, `tennis-wta`, `tennis-atp-race`, `tennis-wta-race`, `tennis-atp-doubles`, `tennis-wta-doubles`, `tennis-atp-doubles-race`, `tennis-wta-doubles-race`, `badminton-bwf-singles-men`, `badminton-bwf-singles-women`, `badminton-bwf-doubles-men`, `badminton-bwf-doubles-women`, `badminton-bwf-mixed-doubles`, `golf-owgr`, `golf-wwgr`, `golf-pga-fedexcup`, `golf-pga-money`, `golf-dp-world-tour`, `golf-lpga`, `golf-asian-tour`, `golf-japan-tour`, `golf-sunshine-tour`, `golf-korn-ferry`, `golf-champions-tour`, `darts-world-ranking`, `snooker-world-ranking`, `tennis-atp-live`, `tennis-wta-live`, `tennis-atp-race-live`, `tennis-wta-race-live`, `tennis-atp-doubles-live`, `tennis-wta-doubles-live`, `tennis-atp-doubles-race-live`, `tennis-wta-doubles-race-live`) | Flashscore rankings |
| `scores` / `scores` | `GET /flashscore/scores` | `sport` (query, required; values: `football`, `tennis`, `basketball`, `hockey`, `golf`, `formula-1`, `baseball`, `snooker`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `beach-soccer`, `beach-volleyball`, `boxing`, `cricket`, `cycling`, `darts`, `esports`, `field-hockey`, `floorball`, `futsal`, `handball`, `horse-racing`, `kabaddi`, `mma`, `motorsport`, `netball`, `pesapallo`, `rugby-league`, `rugby-union`, `table-tennis`, `volleyball`, `water-polo`, `winter-sports`), `day_offset` (query, optional) | Flashscore scores and fixtures by sport |
| `search` / `search` | `GET /flashscore/search` | `q` (query, required) | Flashscore search |
| `sports` / `sports` | `GET /flashscore/sports` | — | Flashscore sports and live category counts |
| `topSearch` / `top_search` | `GET /flashscore/top-search` | — | Flashscore top search entities |
| `tournamentEvents` / `tournament_events` | `GET /flashscore/tournament-events` | `path` (query, required), `page` (query, optional) | Flashscore tournament season results or fixtures |
| `tournamentSeasons` / `tournament_seasons` | `GET /flashscore/tournament-seasons` | `path` (query, required) | Flashscore tournament archive seasons |
| `tournamentStandings` / `tournament_standings` | `GET /flashscore/tournament-standings` | `path` (query, required), `view` (query, optional; values: `overall`, `home`, `away`, `form_overall`, `form_home`, `form_away`, `overunder_overall`, `overunder_home`, `overunder_away`, `htft_overall`, `htft_home`, `htft_away`, `top_scorers`) | Flashscore competition standings table |
| `tournamentStandingsViews` / `tournament_standings_views` | `GET /flashscore/tournament-standings-views` | `path` (query, required) | Flashscore competition standings view discovery |

## Client forms

- JavaScript: import `FlashscoreClient` (also exported as `Client`) from `@crawlora-org/flashscore`; use `new FlashscoreClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `FlashscoreClient` (also exported as `Client`) from `crawlora_flashscore`; use `with FlashscoreClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncFlashscoreClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
