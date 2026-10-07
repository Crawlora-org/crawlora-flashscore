require "json"
require "net/http"
require "uri"

module Crawlora
  module Flashscore
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"flashscore-calendar": {"id": "flashscore-calendar", "method": "GET", "params": [{"description": "Calendar category from flashscore-calendar-categories", "enum": ["tennis-atp", "tennis-wta", "golf-pga", "golf-dp-world", "badminton-bwf", "motorsport-f1"], "in": "query", "name": "category", "required": true, "type": "string", "x-example": "tennis-atp"}], "path": "/flashscore/calendar", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["tennis-atp", "tennis-wta", "golf-pga", "golf-dp-world", "badminton-bwf", "motorsport-f1"], "in": "query", "name": "category", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-calendar-categories": {"id": "flashscore-calendar-categories", "method": "GET", "params": [], "path": "/flashscore/calendar-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-competitions": {"id": "flashscore-competitions", "method": "GET", "params": [{"description": "Sport key", "enum": ["football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}, {"description": "Days from today; -7 to 7; defaults to 0", "in": "query", "maximum": 7, "minimum": -7, "name": "day_offset", "type": "integer", "x-example": 0}], "path": "/flashscore/competitions", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"], "in": "query", "name": "sport", "required": true, "type": "string"}, {"in": "query", "name": "day_offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-match-h2h": {"id": "flashscore-match-h2h", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "xtmHKGT0"}], "path": "/flashscore/match-h2h", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-highlights": {"id": "flashscore-match-highlights", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "j52jHsN8"}], "path": "/flashscore/match-highlights", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-info": {"id": "flashscore-match-info", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "xtmHKGT0"}], "path": "/flashscore/match-info", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-lineups": {"id": "flashscore-match-lineups", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "j52jHsN8"}], "path": "/flashscore/match-lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-missing-players": {"id": "flashscore-match-missing-players", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "f75igXFG"}], "path": "/flashscore/match-missing-players", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-news": {"id": "flashscore-match-news", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "xtmHKGT0"}], "path": "/flashscore/match-news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-odds": {"id": "flashscore-match-odds", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "p0aFxkkn"}, {"description": "Viewer market country code from flashscore-odds-geos; defaults to GB", "enum": ["AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string", "x-example": "GB"}, {"description": "US state (with geo US) or Canadian province (with geo CA) code from flashscore-odds-geos; rejected with any other geo", "enum": ["AB", "AK", "AL", "AR", "AZ", "BC", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MB", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NB", "NC", "ND", "NE", "NH", "NJ", "NL", "NM", "NS", "NT", "NU", "NV", "NY", "OH", "OK", "ON", "OR", "PA", "PE", "QC", "RI", "SC", "SD", "SK", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "YT"], "in": "query", "name": "subdivision", "type": "string", "x-example": "NJ"}, {"description": "Optional filter to one betting type", "enum": ["HOME_DRAW_AWAY", "HOME_AWAY", "DRAW_NO_BET", "DOUBLE_CHANCE", "ASIAN_HANDICAP", "EUROPEAN_HANDICAP", "OVER_UNDER", "BOTH_TEAMS_TO_SCORE", "CORRECT_SCORE", "HALF_FULL_TIME", "ODD_OR_EVEN", "TO_QUALIFY", "NEXT_GOAL", "TOP_POSITION_MERGED", "TO_WIN_AND_TOP_POSITION", "WIN_EACH_WAY"], "in": "query", "name": "betting_type", "type": "string", "x-example": "HOME_DRAW_AWAY"}, {"description": "Optional filter to one scope", "enum": ["FULL_TIME", "FULL_TIME_OVER_TIME", "FIRST_HALF", "SECOND_HALF", "FIRST_PERIOD", "FIRST_QUARTER", "FIRST_SET", "SECOND_SET"], "in": "query", "name": "scope", "type": "string", "x-example": "FULL_TIME"}], "path": "/flashscore/match-odds", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}, {"enum": ["AB", "AK", "AL", "AR", "AZ", "BC", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MB", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NB", "NC", "ND", "NE", "NH", "NJ", "NL", "NM", "NS", "NT", "NU", "NV", "NY", "OH", "OK", "ON", "OR", "PA", "PE", "QC", "RI", "SC", "SD", "SK", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "YT"], "in": "query", "name": "subdivision", "type": "string"}, {"enum": ["HOME_DRAW_AWAY", "HOME_AWAY", "DRAW_NO_BET", "DOUBLE_CHANCE", "ASIAN_HANDICAP", "EUROPEAN_HANDICAP", "OVER_UNDER", "BOTH_TEAMS_TO_SCORE", "CORRECT_SCORE", "HALF_FULL_TIME", "ODD_OR_EVEN", "TO_QUALIFY", "NEXT_GOAL", "TOP_POSITION_MERGED", "TO_WIN_AND_TOP_POSITION", "WIN_EACH_WAY"], "in": "query", "name": "betting_type", "type": "string"}, {"enum": ["FULL_TIME", "FULL_TIME_OVER_TIME", "FIRST_HALF", "SECOND_HALF", "FIRST_PERIOD", "FIRST_QUARTER", "FIRST_SET", "SECOND_SET"], "in": "query", "name": "scope", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-predicted-lineups": {"id": "flashscore-match-predicted-lineups", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "f75igXFG"}], "path": "/flashscore/match-predicted-lineups", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-standings": {"id": "flashscore-match-standings", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "xtmHKGT0"}, {"description": "Standings/table view; defaults to overall", "enum": ["overall", "home", "away", "form_overall", "overunder_overall", "form_home", "form_away", "top_scorers", "htft_overall", "htft_home", "htft_away", "live_overall", "overunder_home", "overunder_away"], "in": "query", "name": "view", "type": "string", "x-example": "overall"}], "path": "/flashscore/match-standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "form_overall", "overunder_overall", "form_home", "form_away", "top_scorers", "htft_overall", "htft_home", "htft_away", "live_overall", "overunder_home", "overunder_away"], "in": "query", "name": "view", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-stats": {"id": "flashscore-match-stats", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "xtmHKGT0"}], "path": "/flashscore/match-stats", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-match-tv": {"id": "flashscore-match-tv", "method": "GET", "params": [{"description": "Eight-character Flashscore match id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "p0aFxkkn"}, {"description": "Viewer market country code from flashscore-odds-geos; defaults to GB", "enum": ["AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string", "x-example": "GB"}], "path": "/flashscore/match-tv", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"], "in": "query", "name": "geo", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-navigation": {"id": "flashscore-navigation", "method": "GET", "params": [{"description": "Relative Flashscore navigation path; defaults to /. Use a path returned by flashscore-sports or flashscore-navigation.", "in": "query", "name": "path", "type": "string", "x-example": "/basketball/usa/"}], "path": "/flashscore/navigation", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "path", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-news": {"id": "flashscore-news", "method": "GET", "params": [{"description": "News section key; defaults to all", "enum": ["all", "football", "uefa-nations-league", "tennis", "features", "premier-league", "nfl", "mlb", "nba", "nhl", "formula-1", "champions-league", "europa-league", "conference-league", "darts", "snooker", "golf", "road-cycling", "laliga", "bundesliga", "serie-a", "ligue-1", "badminton", "handball", "hockey", "basketball", "cricket", "rugby-union", "athletics", "baseball", "fifa", "rugby-league", "motorsport", "aussie-rules", "flashscore-ratings", "american-sports", "african-football", "combat-sports", "winter-sports", "transfer-news"], "in": "query", "name": "category", "type": "string", "x-example": "football"}, {"description": "1-based page, 1 to 100; defaults to 1", "in": "query", "maximum": 100, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/flashscore/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["all", "football", "uefa-nations-league", "tennis", "features", "premier-league", "nfl", "mlb", "nba", "nhl", "formula-1", "champions-league", "europa-league", "conference-league", "darts", "snooker", "golf", "road-cycling", "laliga", "bundesliga", "serie-a", "ligue-1", "badminton", "handball", "hockey", "basketball", "cricket", "rugby-union", "athletics", "baseball", "fifa", "rugby-league", "motorsport", "aussie-rules", "flashscore-ratings", "american-sports", "african-football", "combat-sports", "winter-sports", "transfer-news"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-news-article": {"id": "flashscore-news-article", "method": "GET", "params": [{"description": "Eight-character Flashscore article id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "GYDHQ2yR"}], "path": "/flashscore/news-article", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-news-categories": {"id": "flashscore-news-categories", "method": "GET", "params": [], "path": "/flashscore/news-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-odds-geos": {"id": "flashscore-odds-geos", "method": "GET", "params": [], "path": "/flashscore/odds-geos", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-player": {"id": "flashscore-player", "method": "GET", "params": [{"description": "Eight-character Flashscore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "UmV9iQmE"}, {"description": "Optional player slug; must match the id when supplied", "in": "query", "name": "slug", "type": "string", "x-example": "haaland-erling"}], "path": "/flashscore/player", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "slug", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-player-injuries": {"id": "flashscore-player-injuries", "method": "GET", "params": [{"description": "Eight-character Flashscore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "UmV9iQmE"}, {"description": "Optional player slug; must match the id when supplied", "in": "query", "name": "slug", "type": "string", "x-example": "haaland-erling"}], "path": "/flashscore/player-injuries", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "slug", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-player-transfers": {"id": "flashscore-player-transfers", "method": "GET", "params": [{"description": "Eight-character Flashscore player id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "UmV9iQmE"}, {"description": "Optional player slug; must match the id when supplied", "in": "query", "name": "slug", "type": "string", "x-example": "haaland-erling"}], "path": "/flashscore/player-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "slug", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-ranking-categories": {"id": "flashscore-ranking-categories", "method": "GET", "params": [], "path": "/flashscore/ranking-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-rankings": {"id": "flashscore-rankings", "method": "GET", "params": [{"description": "Ranking category from flashscore-ranking-categories", "enum": ["fifa", "tennis-atp", "tennis-wta", "tennis-atp-race", "tennis-wta-race", "tennis-atp-doubles", "tennis-wta-doubles", "tennis-atp-doubles-race", "tennis-wta-doubles-race", "badminton-bwf-singles-men", "badminton-bwf-singles-women", "badminton-bwf-doubles-men", "badminton-bwf-doubles-women", "badminton-bwf-mixed-doubles", "golf-owgr", "golf-wwgr", "golf-pga-fedexcup", "golf-pga-money", "golf-dp-world-tour", "golf-lpga", "golf-asian-tour", "golf-japan-tour", "golf-sunshine-tour", "golf-korn-ferry", "golf-champions-tour", "darts-world-ranking", "snooker-world-ranking", "tennis-atp-live", "tennis-wta-live", "tennis-atp-race-live", "tennis-wta-race-live", "tennis-atp-doubles-live", "tennis-wta-doubles-live", "tennis-atp-doubles-race-live", "tennis-wta-doubles-race-live"], "in": "query", "name": "category", "required": true, "type": "string", "x-example": "tennis-atp"}], "path": "/flashscore/rankings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["fifa", "tennis-atp", "tennis-wta", "tennis-atp-race", "tennis-wta-race", "tennis-atp-doubles", "tennis-wta-doubles", "tennis-atp-doubles-race", "tennis-wta-doubles-race", "badminton-bwf-singles-men", "badminton-bwf-singles-women", "badminton-bwf-doubles-men", "badminton-bwf-doubles-women", "badminton-bwf-mixed-doubles", "golf-owgr", "golf-wwgr", "golf-pga-fedexcup", "golf-pga-money", "golf-dp-world-tour", "golf-lpga", "golf-asian-tour", "golf-japan-tour", "golf-sunshine-tour", "golf-korn-ferry", "golf-champions-tour", "darts-world-ranking", "snooker-world-ranking", "tennis-atp-live", "tennis-wta-live", "tennis-atp-race-live", "tennis-wta-race-live", "tennis-atp-doubles-live", "tennis-wta-doubles-live", "tennis-atp-doubles-race-live", "tennis-wta-doubles-race-live"], "in": "query", "name": "category", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-scores": {"id": "flashscore-scores", "method": "GET", "params": [{"description": "Sport key", "enum": ["football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"], "in": "query", "name": "sport", "required": true, "type": "string", "x-example": "football"}, {"description": "Days from today; -7 to 7; defaults to 0", "in": "query", "maximum": 7, "minimum": -7, "name": "day_offset", "type": "integer", "x-example": 0}], "path": "/flashscore/scores", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"], "in": "query", "name": "sport", "required": true, "type": "string"}, {"in": "query", "name": "day_offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-search": {"id": "flashscore-search", "method": "GET", "params": [{"description": "Search phrase (2 to 80 characters)", "in": "query", "maxLength": 80, "minLength": 2, "name": "q", "required": true, "type": "string", "x-example": "Champions League"}], "path": "/flashscore/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-sports": {"id": "flashscore-sports", "method": "GET", "params": [], "path": "/flashscore/sports", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-team": {"id": "flashscore-team", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}], "path": "/flashscore/team", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-team-fixtures": {"id": "flashscore-team-fixtures", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}, {"description": "1-based page from 1 to 300; defaults to 1", "in": "query", "maximum": 300, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/flashscore/team-fixtures", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-team-news": {"id": "flashscore-team-news", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}], "path": "/flashscore/team-news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-team-results": {"id": "flashscore-team-results", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}, {"description": "1-based page from 1 to 300; defaults to 1", "in": "query", "maximum": 300, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/flashscore/team-results", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-team-squad": {"id": "flashscore-team-squad", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}, {"description": "Optional team slug; must match the id when supplied", "in": "query", "name": "slug", "type": "string", "x-example": "manchester-city"}, {"description": "Squad statistics scope key from the scopes list of a previous response (for example overall-all or league-SY30SsKF); defaults to overall-all", "in": "query", "name": "scope", "type": "string", "x-example": "overall-all"}], "path": "/flashscore/team-squad", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"in": "query", "name": "slug", "type": "string"}, {"in": "query", "name": "scope", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-team-transfers": {"id": "flashscore-team-transfers", "method": "GET", "params": [{"description": "Eight-character Flashscore team id", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "Wtn9Stg0"}, {"description": "Transfer direction filter; defaults to all", "enum": ["all", "arrivals", "departures"], "in": "query", "name": "type", "type": "string", "x-example": "all"}, {"description": "1-based page from 1 to 300; defaults to 1", "in": "query", "maximum": 300, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/flashscore/team-transfers", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}, {"enum": ["all", "arrivals", "departures"], "in": "query", "name": "type", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-top-search": {"id": "flashscore-top-search", "method": "GET", "params": [], "path": "/flashscore/top-search", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "flashscore-tournament-events": {"id": "flashscore-tournament-events", "method": "GET", "params": [{"description": "Relative Flashscore competition season results or fixtures path", "in": "query", "name": "path", "required": true, "type": "string", "x-example": "/football/england/premier-league-2026-2027/fixtures/"}, {"description": "1-based page; defaults to 1", "in": "query", "maximum": 100, "minimum": 1, "name": "page", "type": "integer", "x-example": 1}], "path": "/flashscore/tournament-events", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "path", "required": true, "type": "string"}, {"in": "query", "name": "page", "type": "integer"}], "security": ["ApiKeyAuth"]}, "flashscore-tournament-seasons": {"id": "flashscore-tournament-seasons", "method": "GET", "params": [{"description": "Relative Flashscore competition archive path ending in /archive/", "in": "query", "name": "path", "required": true, "type": "string", "x-example": "/football/europe/champions-league/archive/"}], "path": "/flashscore/tournament-seasons", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "path", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-tournament-standings": {"id": "flashscore-tournament-standings", "method": "GET", "params": [{"description": "Relative Flashscore competition path from flashscore-navigation or flashscore-competitions; omit /standings/", "in": "query", "name": "path", "required": true, "type": "string", "x-example": "/football/england/premier-league/"}, {"description": "View returned by flashscore-tournament-standings-views; defaults to overall", "enum": ["overall", "home", "away", "form_overall", "form_home", "form_away", "overunder_overall", "overunder_home", "overunder_away", "htft_overall", "htft_home", "htft_away", "top_scorers"], "in": "query", "name": "view", "type": "string", "x-example": "overall"}], "path": "/flashscore/tournament-standings", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "path", "required": true, "type": "string"}, {"enum": ["overall", "home", "away", "form_overall", "form_home", "form_away", "overunder_overall", "overunder_home", "overunder_away", "htft_overall", "htft_home", "htft_away", "top_scorers"], "in": "query", "name": "view", "type": "string"}], "security": ["ApiKeyAuth"]}, "flashscore-tournament-standings-views": {"id": "flashscore-tournament-standings-views", "method": "GET", "params": [{"description": "Relative Flashscore competition path from flashscore-navigation or flashscore-competitions; omit /standings/", "in": "query", "name": "path", "required": true, "type": "string", "x-example": "/football/england/premier-league/"}], "path": "/flashscore/tournament-standings-views", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "path", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["flashscore-calendar", "flashscore-calendar-categories", "flashscore-competitions", "flashscore-match-h2h", "flashscore-match-highlights", "flashscore-match-info", "flashscore-match-lineups", "flashscore-match-missing-players", "flashscore-match-news", "flashscore-match-odds", "flashscore-match-predicted-lineups", "flashscore-match-standings", "flashscore-match-stats", "flashscore-match-tv", "flashscore-navigation", "flashscore-news", "flashscore-news-article", "flashscore-news-categories", "flashscore-odds-geos", "flashscore-player", "flashscore-player-injuries", "flashscore-player-transfers", "flashscore-ranking-categories", "flashscore-rankings", "flashscore-scores", "flashscore-search", "flashscore-sports", "flashscore-team", "flashscore-team-fixtures", "flashscore-team-news", "flashscore-team-results", "flashscore-team-squad", "flashscore-team-transfers", "flashscore-top-search", "flashscore-tournament-events", "flashscore-tournament-seasons", "flashscore-tournament-standings", "flashscore-tournament-standings-views"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-flashscore-ruby/0.2.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = Net::HTTP::Get.new(uri)
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = @transport.call(url, request.to_hash, @timeout)
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('calendar') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-calendar', params, response_type: response_type)
      end
      define_method('calendar_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-calendar-categories', params, response_type: response_type)
      end
      define_method('competitions') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-competitions', params, response_type: response_type)
      end
      define_method('match_h2h') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-h2h', params, response_type: response_type)
      end
      define_method('match_highlights') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-highlights', params, response_type: response_type)
      end
      define_method('match_info') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-info', params, response_type: response_type)
      end
      define_method('match_lineups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-lineups', params, response_type: response_type)
      end
      define_method('match_missing_players') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-missing-players', params, response_type: response_type)
      end
      define_method('match_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-news', params, response_type: response_type)
      end
      define_method('match_odds') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-odds', params, response_type: response_type)
      end
      define_method('match_predicted_lineups') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-predicted-lineups', params, response_type: response_type)
      end
      define_method('match_standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-standings', params, response_type: response_type)
      end
      define_method('match_stats') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-stats', params, response_type: response_type)
      end
      define_method('match_tv') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-match-tv', params, response_type: response_type)
      end
      define_method('navigation') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-navigation', params, response_type: response_type)
      end
      define_method('news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-news', params, response_type: response_type)
      end
      define_method('news_article') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-news-article', params, response_type: response_type)
      end
      define_method('news_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-news-categories', params, response_type: response_type)
      end
      define_method('odds_geos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-odds-geos', params, response_type: response_type)
      end
      define_method('player') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-player', params, response_type: response_type)
      end
      define_method('player_injuries') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-player-injuries', params, response_type: response_type)
      end
      define_method('player_transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-player-transfers', params, response_type: response_type)
      end
      define_method('ranking_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-ranking-categories', params, response_type: response_type)
      end
      define_method('rankings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-rankings', params, response_type: response_type)
      end
      define_method('scores') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-scores', params, response_type: response_type)
      end
      define_method('search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-search', params, response_type: response_type)
      end
      define_method('sports') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-sports', params, response_type: response_type)
      end
      define_method('team') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team', params, response_type: response_type)
      end
      define_method('team_fixtures') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team-fixtures', params, response_type: response_type)
      end
      define_method('team_news') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team-news', params, response_type: response_type)
      end
      define_method('team_results') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team-results', params, response_type: response_type)
      end
      define_method('team_squad') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team-squad', params, response_type: response_type)
      end
      define_method('team_transfers') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-team-transfers', params, response_type: response_type)
      end
      define_method('top_search') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-top-search', params, response_type: response_type)
      end
      define_method('tournament_events') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-tournament-events', params, response_type: response_type)
      end
      define_method('tournament_seasons') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-tournament-seasons', params, response_type: response_type)
      end
      define_method('tournament_standings') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-tournament-standings', params, response_type: response_type)
      end
      define_method('tournament_standings_views') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('flashscore-tournament-standings-views', params, response_type: response_type)
      end

      private

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
