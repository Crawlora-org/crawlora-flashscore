# Flashscore client usage

The `@crawlora-org/flashscore` and `crawlora-flashscore` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Flashscore locally; Crawlora is independent from and not endorsed by Flashscore or its owners.

The package tracks the public API contract revision `sha256:fcaf7e58d82dcbe73e54cddcffc79511b5d01e2c25d511531656862dfe91fb3e` bundled with release `0.2.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 38 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `flashscore` group and the generated `Client` alias.

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
| `matchMissingPlayers` / `match_missing_players` | `GET /flashscore/match-missing-players` | `id` (query, required) | Flashscore missing and doubtful players |
| `matchNews` / `match_news` | `GET /flashscore/match-news` | `id` (query, required) | Flashscore match news references |
| `matchOdds` / `match_odds` | `GET /flashscore/match-odds` | `id` (query, required), `geo` (query, optional; values: `AE`, `AL`, `AM`, `AO`, `AR`, `AT`, `AU`, `AZ`, `BA`, `BD`, `BE`, `BG`, `BO`, `BR`, `BY`, `CA`, `CH`, `CI`, `CL`, `CM`, `CN`, `CO`, `CR`, `CY`, `CZ`, `DE`, `DK`, `DO`, `DZ`, `EC`, `EE`, `EG`, `ES`, `ET`, `FI`, `FR`, `GB`, `GE`, `GH`, `GR`, `GT`, `HK`, `HN`, `HR`, `HU`, `ID`, `IE`, `IL`, `IN`, `IQ`, `IR`, `IS`, `IT`, `JO`, `JP`, `KE`, `KG`, `KH`, `KR`, `KW`, `KZ`, `LA`, `LB`, `LK`, `LT`, `LU`, `LV`, `LY`, `MA`, `MD`, `ME`, `MK`, `MM`, `MN`, `MT`, `MX`, `MY`, `NG`, `NI`, `NL`, `NO`, `NP`, `NZ`, `PA`, `PE`, `PH`, `PK`, `PL`, `PT`, `PY`, `QA`, `RO`, `RS`, `RU`, `SA`, `SD`, `SE`, `SG`, `SI`, `SK`, `SN`, `SV`, `TH`, `TN`, `TR`, `TW`, `TZ`, `UA`, `UG`, `US`, `UY`, `UZ`, `VE`, `VN`, `XK`, `ZA`, `ZM`, `ZW`), `subdivision` (query, optional; values: `AB`, `AK`, `AL`, `AR`, `AZ`, `BC`, `CA`, `CO`, `CT`, `DC`, `DE`, `FL`, `GA`, `HI`, `IA`, `ID`, `IL`, `IN`, `KS`, `KY`, `LA`, `MA`, `MB`, `MD`, `ME`, `MI`, `MN`, `MO`, `MS`, `MT`, `NB`, `NC`, `ND`, `NE`, `NH`, `NJ`, `NL`, `NM`, `NS`, `NT`, `NU`, `NV`, `NY`, `OH`, `OK`, `ON`, `OR`, `PA`, `PE`, `QC`, `RI`, `SC`, `SD`, `SK`, `TN`, `TX`, `UT`, `VA`, `VT`, `WA`, `WI`, `WV`, `WY`, `YT`), `betting_type` (query, optional; values: `HOME_DRAW_AWAY`, `HOME_AWAY`, `DRAW_NO_BET`, `DOUBLE_CHANCE`, `ASIAN_HANDICAP`, `EUROPEAN_HANDICAP`, `OVER_UNDER`, `BOTH_TEAMS_TO_SCORE`, `CORRECT_SCORE`, `HALF_FULL_TIME`, `ODD_OR_EVEN`, `TO_QUALIFY`, `NEXT_GOAL`, `TOP_POSITION_MERGED`, `TO_WIN_AND_TOP_POSITION`, `WIN_EACH_WAY`), `scope` (query, optional; values: `FULL_TIME`, `FULL_TIME_OVER_TIME`, `FIRST_HALF`, `SECOND_HALF`, `FIRST_PERIOD`, `FIRST_QUARTER`, `FIRST_SET`, `SECOND_SET`) | Flashscore match bookmaker odds comparison |
| `matchPredictedLineups` / `match_predicted_lineups` | `GET /flashscore/match-predicted-lineups` | `id` (query, required) | Flashscore predicted lineups |
| `matchStandings` / `match_standings` | `GET /flashscore/match-standings` | `id` (query, required), `view` (query, optional; values: `overall`, `home`, `away`, `form_overall`, `overunder_overall`, `form_home`, `form_away`, `top_scorers`, `htft_overall`, `htft_home`, `htft_away`, `live_overall`, `overunder_home`, `overunder_away`) | Flashscore match league standings |
| `matchStats` / `match_stats` | `GET /flashscore/match-stats` | `id` (query, required) | Flashscore match statistics |
| `matchTv` / `match_tv` | `GET /flashscore/match-tv` | `id` (query, required), `geo` (query, optional; values: `AE`, `AL`, `AM`, `AO`, `AR`, `AT`, `AU`, `AZ`, `BA`, `BD`, `BE`, `BG`, `BO`, `BR`, `BY`, `CA`, `CH`, `CI`, `CL`, `CM`, `CN`, `CO`, `CR`, `CY`, `CZ`, `DE`, `DK`, `DO`, `DZ`, `EC`, `EE`, `EG`, `ES`, `ET`, `FI`, `FR`, `GB`, `GE`, `GH`, `GR`, `GT`, `HK`, `HN`, `HR`, `HU`, `ID`, `IE`, `IL`, `IN`, `IQ`, `IR`, `IS`, `IT`, `JO`, `JP`, `KE`, `KG`, `KH`, `KR`, `KW`, `KZ`, `LA`, `LB`, `LK`, `LT`, `LU`, `LV`, `LY`, `MA`, `MD`, `ME`, `MK`, `MM`, `MN`, `MT`, `MX`, `MY`, `NG`, `NI`, `NL`, `NO`, `NP`, `NZ`, `PA`, `PE`, `PH`, `PK`, `PL`, `PT`, `PY`, `QA`, `RO`, `RS`, `RU`, `SA`, `SD`, `SE`, `SG`, `SI`, `SK`, `SN`, `SV`, `TH`, `TN`, `TR`, `TW`, `TZ`, `UA`, `UG`, `US`, `UY`, `UZ`, `VE`, `VN`, `XK`, `ZA`, `ZM`, `ZW`) | Flashscore match TV and streaming broadcasters |
| `navigation` / `navigation` | `GET /flashscore/navigation` | `path` (query, optional) | Flashscore sport, category, country, and competition navigation |
| `news` / `news` | `GET /flashscore/news` | `category` (query, optional; values: `all`, `football`, `uefa-nations-league`, `tennis`, `features`, `premier-league`, `nfl`, `mlb`, `nba`, `nhl`, `formula-1`, `champions-league`, `europa-league`, `conference-league`, `darts`, `snooker`, `golf`, `road-cycling`, `laliga`, `bundesliga`, `serie-a`, `ligue-1`, `badminton`, `handball`, `hockey`, `basketball`, `cricket`, `rugby-union`, `athletics`, `baseball`, `fifa`, `rugby-league`, `motorsport`, `aussie-rules`, `flashscore-ratings`, `american-sports`, `african-football`, `combat-sports`, `winter-sports`, `transfer-news`), `page` (query, optional) | Flashscore News listings by section |
| `newsArticle` / `news_article` | `GET /flashscore/news-article` | `id` (query, required) | Flashscore news article metadata |
| `newsCategories` / `news_categories` | `GET /flashscore/news-categories` | — | Flashscore News categories |
| `oddsGeos` / `odds_geos` | `GET /flashscore/odds-geos` | — | Flashscore odds markets, subdivisions and odds enums |
| `player` / `player` | `GET /flashscore/player` | `id` (query, required), `slug` (query, optional) | Flashscore player profile and career |
| `playerInjuries` / `player_injuries` | `GET /flashscore/player-injuries` | `id` (query, required), `slug` (query, optional) | Flashscore player injury history |
| `playerTransfers` / `player_transfers` | `GET /flashscore/player-transfers` | `id` (query, required), `slug` (query, optional) | Flashscore player transfer history |
| `rankingCategories` / `ranking_categories` | `GET /flashscore/ranking-categories` | — | Flashscore ranking categories |
| `rankings` / `rankings` | `GET /flashscore/rankings` | `category` (query, required; values: `fifa`, `tennis-atp`, `tennis-wta`, `tennis-atp-race`, `tennis-wta-race`, `tennis-atp-doubles`, `tennis-wta-doubles`, `tennis-atp-doubles-race`, `tennis-wta-doubles-race`, `badminton-bwf-singles-men`, `badminton-bwf-singles-women`, `badminton-bwf-doubles-men`, `badminton-bwf-doubles-women`, `badminton-bwf-mixed-doubles`, `golf-owgr`, `golf-wwgr`, `golf-pga-fedexcup`, `golf-pga-money`, `golf-dp-world-tour`, `golf-lpga`, `golf-asian-tour`, `golf-japan-tour`, `golf-sunshine-tour`, `golf-korn-ferry`, `golf-champions-tour`, `darts-world-ranking`, `snooker-world-ranking`, `tennis-atp-live`, `tennis-wta-live`, `tennis-atp-race-live`, `tennis-wta-race-live`, `tennis-atp-doubles-live`, `tennis-wta-doubles-live`, `tennis-atp-doubles-race-live`, `tennis-wta-doubles-race-live`) | Flashscore rankings |
| `scores` / `scores` | `GET /flashscore/scores` | `sport` (query, required; values: `football`, `tennis`, `basketball`, `hockey`, `golf`, `formula-1`, `baseball`, `snooker`, `american-football`, `aussie-rules`, `badminton`, `bandy`, `beach-soccer`, `beach-volleyball`, `boxing`, `cricket`, `cycling`, `darts`, `esports`, `field-hockey`, `floorball`, `futsal`, `handball`, `horse-racing`, `kabaddi`, `mma`, `motorsport`, `netball`, `pesapallo`, `rugby-league`, `rugby-union`, `table-tennis`, `volleyball`, `water-polo`, `winter-sports`), `day_offset` (query, optional) | Flashscore scores and fixtures by sport |
| `search` / `search` | `GET /flashscore/search` | `q` (query, required) | Flashscore search |
| `sports` / `sports` | `GET /flashscore/sports` | — | Flashscore sports and live category counts |
| `team` / `team` | `GET /flashscore/team` | `id` (query, required) | Flashscore team profile |
| `teamFixtures` / `team_fixtures` | `GET /flashscore/team-fixtures` | `id` (query, required), `page` (query, optional) | Flashscore team fixtures |
| `teamNews` / `team_news` | `GET /flashscore/team-news` | `id` (query, required) | Flashscore team news headlines |
| `teamResults` / `team_results` | `GET /flashscore/team-results` | `id` (query, required), `page` (query, optional) | Flashscore team results |
| `teamSquad` / `team_squad` | `GET /flashscore/team-squad` | `id` (query, required), `slug` (query, optional), `scope` (query, optional) | Flashscore team squad |
| `teamTransfers` / `team_transfers` | `GET /flashscore/team-transfers` | `id` (query, required), `type` (query, optional; values: `all`, `arrivals`, `departures`), `page` (query, optional) | Flashscore team transfers |
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
