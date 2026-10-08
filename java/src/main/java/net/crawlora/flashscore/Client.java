package net.crawlora.flashscore;

import net.crawlora.Json;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/** Client for the Flashscore endpoints hosted by Crawlora. */
public final class Client implements AutoCloseable {
    public static final String DEFAULT_BASE_URL = "https://api.crawlora.net/api/v1";
    public static final int OPERATION_COUNT = 54;
    public static final List<String> OPERATION_IDS = List.of(
            "flashscore-calendar",
            "flashscore-calendar-categories",
            "flashscore-competitions",
            "flashscore-entity-news",
            "flashscore-match-box-score",
            "flashscore-match-darts",
            "flashscore-match-h2h",
            "flashscore-match-highlights",
            "flashscore-match-info",
            "flashscore-match-lineups",
            "flashscore-match-missing-players",
            "flashscore-match-momentum",
            "flashscore-match-news",
            "flashscore-match-odds",
            "flashscore-match-player-stats",
            "flashscore-match-point-by-point",
            "flashscore-match-predicted-lineups",
            "flashscore-match-report",
            "flashscore-match-standings",
            "flashscore-match-stats",
            "flashscore-match-tv",
            "flashscore-navigation",
            "flashscore-news",
            "flashscore-news-article",
            "flashscore-news-article-body",
            "flashscore-news-categories",
            "flashscore-news-most-read",
            "flashscore-odds-geos",
            "flashscore-player",
            "flashscore-player-fixtures",
            "flashscore-player-injuries",
            "flashscore-player-match-log",
            "flashscore-player-news",
            "flashscore-player-results",
            "flashscore-player-transfers",
            "flashscore-ranking-categories",
            "flashscore-rankings",
            "flashscore-scores",
            "flashscore-search",
            "flashscore-sports",
            "flashscore-team",
            "flashscore-team-fixtures",
            "flashscore-team-news",
            "flashscore-team-outright-odds",
            "flashscore-team-results",
            "flashscore-team-squad",
            "flashscore-team-transfers",
            "flashscore-top-search",
            "flashscore-tournament-archive-seasons",
            "flashscore-tournament-events",
            "flashscore-tournament-outright-odds",
            "flashscore-tournament-seasons",
            "flashscore-tournament-standings",
            "flashscore-tournament-standings-views"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("flashscore-calendar", new Operation("flashscore-calendar", "GET", "/flashscore/calendar", Map.ofEntries(Map.entry("category", new Param("category", "query", true, "string", List.of("tennis-atp", "tennis-wta", "golf-pga", "golf-dp-world", "badminton-bwf", "motorsport-f1"), "csv"))), List.of("application/json")));
        operations.put("flashscore-calendar-categories", new Operation("flashscore-calendar-categories", "GET", "/flashscore/calendar-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-competitions", new Operation("flashscore-competitions", "GET", "/flashscore/competitions", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports", "moto-racing", "ski-jumping", "alpine-skiing", "cross-country-skiing", "biathlon"), "csv")), Map.entry("day_offset", new Param("day_offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-entity-news", new Operation("flashscore-entity-news", "GET", "/flashscore/entity-news", Map.ofEntries(Map.entry("type", new Param("type", "query", true, "string", List.of("team", "player", "tournament", "sport"), "csv")), Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-box-score", new Operation("flashscore-match-box-score", "GET", "/flashscore/match-box-score", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-darts", new Operation("flashscore-match-darts", "GET", "/flashscore/match-darts", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-h2h", new Operation("flashscore-match-h2h", "GET", "/flashscore/match-h2h", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-highlights", new Operation("flashscore-match-highlights", "GET", "/flashscore/match-highlights", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-info", new Operation("flashscore-match-info", "GET", "/flashscore/match-info", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-lineups", new Operation("flashscore-match-lineups", "GET", "/flashscore/match-lineups", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-missing-players", new Operation("flashscore-match-missing-players", "GET", "/flashscore/match-missing-players", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-momentum", new Operation("flashscore-match-momentum", "GET", "/flashscore/match-momentum", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-news", new Operation("flashscore-match-news", "GET", "/flashscore/match-news", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-odds", new Operation("flashscore-match-odds", "GET", "/flashscore/match-odds", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("geo", new Param("geo", "query", false, "string", List.of("AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"), "csv")), Map.entry("subdivision", new Param("subdivision", "query", false, "string", List.of("AB", "AK", "AL", "AR", "AZ", "BC", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MB", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NB", "NC", "ND", "NE", "NH", "NJ", "NL", "NM", "NS", "NT", "NU", "NV", "NY", "OH", "OK", "ON", "OR", "PA", "PE", "QC", "RI", "SC", "SD", "SK", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "YT"), "csv")), Map.entry("betting_type", new Param("betting_type", "query", false, "string", List.of("HOME_DRAW_AWAY", "HOME_AWAY", "DRAW_NO_BET", "DOUBLE_CHANCE", "ASIAN_HANDICAP", "EUROPEAN_HANDICAP", "OVER_UNDER", "BOTH_TEAMS_TO_SCORE", "CORRECT_SCORE", "HALF_FULL_TIME", "ODD_OR_EVEN", "TO_QUALIFY", "NEXT_GOAL", "TOP_POSITION_MERGED", "TO_WIN_AND_TOP_POSITION", "WIN_EACH_WAY"), "csv")), Map.entry("scope", new Param("scope", "query", false, "string", List.of("FULL_TIME", "FULL_TIME_OVER_TIME", "FIRST_HALF", "SECOND_HALF", "FIRST_PERIOD", "FIRST_QUARTER", "FIRST_SET", "SECOND_SET"), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-player-stats", new Operation("flashscore-match-player-stats", "GET", "/flashscore/match-player-stats", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("player_id", new Param("player_id", "query", false, "string", List.of(), "csv")), Map.entry("group", new Param("group", "query", false, "string", List.of("top_stats", "shots", "attack", "passes", "defense", "goalkeeping", "general"), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-point-by-point", new Operation("flashscore-match-point-by-point", "GET", "/flashscore/match-point-by-point", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-predicted-lineups", new Operation("flashscore-match-predicted-lineups", "GET", "/flashscore/match-predicted-lineups", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-report", new Operation("flashscore-match-report", "GET", "/flashscore/match-report", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-standings", new Operation("flashscore-match-standings", "GET", "/flashscore/match-standings", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("view", new Param("view", "query", false, "string", List.of("overall", "home", "away", "form_overall", "overunder_overall", "form_home", "form_away", "top_scorers", "htft_overall", "htft_home", "htft_away", "live_overall", "overunder_home", "overunder_away"), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-stats", new Operation("flashscore-match-stats", "GET", "/flashscore/match-stats", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-tv", new Operation("flashscore-match-tv", "GET", "/flashscore/match-tv", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("geo", new Param("geo", "query", false, "string", List.of("AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"), "csv"))), List.of("application/json")));
        operations.put("flashscore-navigation", new Operation("flashscore-navigation", "GET", "/flashscore/navigation", Map.ofEntries(Map.entry("path", new Param("path", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news", new Operation("flashscore-news", "GET", "/flashscore/news", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("all", "football", "uefa-nations-league", "tennis", "features", "premier-league", "nfl", "mlb", "nba", "nhl", "formula-1", "champions-league", "europa-league", "conference-league", "darts", "snooker", "golf", "road-cycling", "laliga", "bundesliga", "serie-a", "ligue-1", "badminton", "handball", "hockey", "basketball", "cricket", "rugby-union", "athletics", "baseball", "fifa", "rugby-league", "motorsport", "aussie-rules", "flashscore-ratings", "american-sports", "african-football", "combat-sports", "winter-sports", "transfer-news"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news-article", new Operation("flashscore-news-article", "GET", "/flashscore/news-article", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news-article-body", new Operation("flashscore-news-article-body", "GET", "/flashscore/news-article-body", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news-categories", new Operation("flashscore-news-categories", "GET", "/flashscore/news-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-news-most-read", new Operation("flashscore-news-most-read", "GET", "/flashscore/news-most-read", Map.of(), List.of("application/json")));
        operations.put("flashscore-odds-geos", new Operation("flashscore-odds-geos", "GET", "/flashscore/odds-geos", Map.of(), List.of("application/json")));
        operations.put("flashscore-player", new Operation("flashscore-player", "GET", "/flashscore/player", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-fixtures", new Operation("flashscore-player-fixtures", "GET", "/flashscore/player-fixtures", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-injuries", new Operation("flashscore-player-injuries", "GET", "/flashscore/player-injuries", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-match-log", new Operation("flashscore-player-match-log", "GET", "/flashscore/player-match-log", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-news", new Operation("flashscore-player-news", "GET", "/flashscore/player-news", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-results", new Operation("flashscore-player-results", "GET", "/flashscore/player-results", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-player-transfers", new Operation("flashscore-player-transfers", "GET", "/flashscore/player-transfers", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-ranking-categories", new Operation("flashscore-ranking-categories", "GET", "/flashscore/ranking-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-rankings", new Operation("flashscore-rankings", "GET", "/flashscore/rankings", Map.ofEntries(Map.entry("category", new Param("category", "query", true, "string", List.of("fifa", "tennis-atp", "tennis-wta", "tennis-atp-race", "tennis-wta-race", "tennis-atp-doubles", "tennis-wta-doubles", "tennis-atp-doubles-race", "tennis-wta-doubles-race", "badminton-bwf-singles-men", "badminton-bwf-singles-women", "badminton-bwf-doubles-men", "badminton-bwf-doubles-women", "badminton-bwf-mixed-doubles", "golf-owgr", "golf-wwgr", "golf-pga-fedexcup", "golf-pga-money", "golf-dp-world-tour", "golf-lpga", "golf-asian-tour", "golf-japan-tour", "golf-sunshine-tour", "golf-korn-ferry", "golf-champions-tour", "darts-world-ranking", "snooker-world-ranking", "tennis-atp-live", "tennis-wta-live", "tennis-atp-race-live", "tennis-wta-race-live", "tennis-atp-doubles-live", "tennis-wta-doubles-live", "tennis-atp-doubles-race-live", "tennis-wta-doubles-race-live"), "csv"))), List.of("application/json")));
        operations.put("flashscore-scores", new Operation("flashscore-scores", "GET", "/flashscore/scores", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports", "moto-racing", "ski-jumping", "alpine-skiing", "cross-country-skiing", "biathlon"), "csv")), Map.entry("day_offset", new Param("day_offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-search", new Operation("flashscore-search", "GET", "/flashscore/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-sports", new Operation("flashscore-sports", "GET", "/flashscore/sports", Map.of(), List.of("application/json")));
        operations.put("flashscore-team", new Operation("flashscore-team", "GET", "/flashscore/team", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-fixtures", new Operation("flashscore-team-fixtures", "GET", "/flashscore/team-fixtures", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-news", new Operation("flashscore-team-news", "GET", "/flashscore/team-news", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-outright-odds", new Operation("flashscore-team-outright-odds", "GET", "/flashscore/team-outright-odds", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("geo", new Param("geo", "query", false, "string", List.of("AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"), "csv")), Map.entry("subdivision", new Param("subdivision", "query", false, "string", List.of("AB", "AK", "AL", "AR", "AZ", "BC", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MB", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NB", "NC", "ND", "NE", "NH", "NJ", "NL", "NM", "NS", "NT", "NU", "NV", "NY", "OH", "OK", "ON", "OR", "PA", "PE", "QC", "RI", "SC", "SD", "SK", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "YT"), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-results", new Operation("flashscore-team-results", "GET", "/flashscore/team-results", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-squad", new Operation("flashscore-team-squad", "GET", "/flashscore/team-squad", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("slug", new Param("slug", "query", false, "string", List.of(), "csv")), Map.entry("scope", new Param("scope", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-team-transfers", new Operation("flashscore-team-transfers", "GET", "/flashscore/team-transfers", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("type", new Param("type", "query", false, "string", List.of("all", "arrivals", "departures"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-top-search", new Operation("flashscore-top-search", "GET", "/flashscore/top-search", Map.of(), List.of("application/json")));
        operations.put("flashscore-tournament-archive-seasons", new Operation("flashscore-tournament-archive-seasons", "GET", "/flashscore/tournament-archive-seasons", Map.ofEntries(Map.entry("stage_id", new Param("stage_id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-tournament-events", new Operation("flashscore-tournament-events", "GET", "/flashscore/tournament-events", Map.ofEntries(Map.entry("path", new Param("path", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-tournament-outright-odds", new Operation("flashscore-tournament-outright-odds", "GET", "/flashscore/tournament-outright-odds", Map.ofEntries(Map.entry("tournament_id", new Param("tournament_id", "query", true, "string", List.of(), "csv")), Map.entry("geo", new Param("geo", "query", false, "string", List.of("AE", "AL", "AM", "AO", "AR", "AT", "AU", "AZ", "BA", "BD", "BE", "BG", "BO", "BR", "BY", "CA", "CH", "CI", "CL", "CM", "CN", "CO", "CR", "CY", "CZ", "DE", "DK", "DO", "DZ", "EC", "EE", "EG", "ES", "ET", "FI", "FR", "GB", "GE", "GH", "GR", "GT", "HK", "HN", "HR", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JO", "JP", "KE", "KG", "KH", "KR", "KW", "KZ", "LA", "LB", "LK", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MK", "MM", "MN", "MT", "MX", "MY", "NG", "NI", "NL", "NO", "NP", "NZ", "PA", "PE", "PH", "PK", "PL", "PT", "PY", "QA", "RO", "RS", "RU", "SA", "SD", "SE", "SG", "SI", "SK", "SN", "SV", "TH", "TN", "TR", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VE", "VN", "XK", "ZA", "ZM", "ZW"), "csv")), Map.entry("subdivision", new Param("subdivision", "query", false, "string", List.of("AB", "AK", "AL", "AR", "AZ", "BC", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MB", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NB", "NC", "ND", "NE", "NH", "NJ", "NL", "NM", "NS", "NT", "NU", "NV", "NY", "OH", "OK", "ON", "OR", "PA", "PE", "QC", "RI", "SC", "SD", "SK", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY", "YT"), "csv"))), List.of("application/json")));
        operations.put("flashscore-tournament-seasons", new Operation("flashscore-tournament-seasons", "GET", "/flashscore/tournament-seasons", Map.ofEntries(Map.entry("path", new Param("path", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-tournament-standings", new Operation("flashscore-tournament-standings", "GET", "/flashscore/tournament-standings", Map.ofEntries(Map.entry("path", new Param("path", "query", true, "string", List.of(), "csv")), Map.entry("view", new Param("view", "query", false, "string", List.of("overall", "home", "away", "form_overall", "form_home", "form_away", "overunder_overall", "overunder_home", "overunder_away", "htft_overall", "htft_home", "htft_away", "top_scorers"), "csv"))), List.of("application/json")));
        operations.put("flashscore-tournament-standings-views", new Operation("flashscore-tournament-standings-views", "GET", "/flashscore/tournament-standings-views", Map.ofEntries(Map.entry("path", new Param("path", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        OPERATIONS = Collections.unmodifiableMap(operations);
    }

    private final String apiKey;
    private final String baseUrl;
    private final Duration timeout;
    private final HttpClient http;
    private volatile boolean closed;

    /** Create a client using Crawlora's hosted API and the default 30 second timeout. */
    public Client(String apiKey) {
        this(apiKey, DEFAULT_BASE_URL, Duration.ofSeconds(30));
    }

    /** Create a client with an explicit hosted API base URL and request timeout. */
    public Client(String apiKey, String baseUrl, Duration timeout) {
        if (apiKey == null || apiKey.isBlank()) throw new IllegalArgumentException("apiKey is required");
        if (baseUrl == null || baseUrl.isBlank()) throw new IllegalArgumentException("baseUrl is required");
        this.apiKey = apiKey;
        this.baseUrl = baseUrl.replaceAll("/+$", "");
        this.timeout = Objects.requireNonNull(timeout, "timeout");
        if (timeout.isZero() || timeout.isNegative()) throw new IllegalArgumentException("timeout must be positive");
        this.http = HttpClient.newBuilder().connectTimeout(timeout).build();
    }

    public String getBaseUrl() { return baseUrl; }
    public Duration getTimeout() { return timeout; }
    public int getOperationCount() { return OPERATION_COUNT; }
    public List<String> getOperationIds() { return OPERATION_IDS; }
    public static Map<String, Operation> operations() { return OPERATIONS; }

    /** Dispatch a selected operation by id. Parameters use the exact OpenAPI names. */
    public Object request(String operationId, Map<String, ?> params) {
        if (closed) throw new IllegalStateException("client is closed");
        Operation operation = OPERATIONS.get(operationId);
        if (operation == null) throw new IllegalArgumentException("unknown Flashscore operation: " + operationId);
        Map<String, ?> values = params == null ? Map.of() : params;
        Set<String> unknown = new TreeSet<>(values.keySet());
        unknown.removeAll(operation.params().keySet());
        if (!unknown.isEmpty()) throw new IllegalArgumentException("unknown parameters for " + operationId + ": " + unknown);

        String path = operation.path();
        List<Map.Entry<String, String>> query = new ArrayList<>();
        for (Param param : operation.params().values()) {
            Object value = values.get(param.name());
            if (value == null) {
                if (param.required()) throw new IllegalArgumentException("missing required parameter: " + param.name());
                continue;
            }
            validateEnum(param, value);
            if (param.location().equals("path")) {
                path = path.replace("{" + param.name() + "}", pathEncode(value.toString()));
            } else {
                addQuery(query, param, value);
            }
        }
        if (path.matches(".*\\{[^}]+}.*")) throw new IllegalArgumentException("missing path parameter for " + operationId);
        StringBuilder url = new StringBuilder(baseUrl).append(path);
        for (int i = 0; i < query.size(); i++) {
            url.append(i == 0 ? '?' : '&').append(queryEncode(query.get(i).getKey()))
                    .append('=').append(queryEncode(query.get(i).getValue()));
        }
        HttpRequest request = HttpRequest.newBuilder(URI.create(url.toString()))
                .timeout(timeout)
                .header("x-api-key", apiKey)
                .header("Accept", acceptHeader(operation))
                .GET().build();
        try {
            HttpResponse<String> response = http.send(request, HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
            String body = response.body();
            String contentType = response.headers().firstValue("content-type").orElse("").toLowerCase();
            Object parsed = body;
            if (contentType.contains("application/json") && !body.isEmpty()) {
                try { parsed = Json.parse(body); }
                catch (RuntimeException error) { throw new CrawloraException("Crawlora returned invalid JSON", error); }
            }
            if (response.statusCode() < 200 || response.statusCode() >= 300) {
                String message = "Crawlora request failed with HTTP " + response.statusCode();
                if (parsed instanceof Map<?, ?> map && map.get("msg") != null) message = map.get("msg").toString();
                throw new CrawloraException(message, response.statusCode(), parsed);
            }
            return parsed;
        } catch (InterruptedException error) {
            Thread.currentThread().interrupt();
            throw new CrawloraException("Crawlora request interrupted", error);
        } catch (IOException error) {
            throw new CrawloraException("Crawlora network request failed", error);
        }
    }

    public Object calendar(Map<String, ?> params) { return request("flashscore-calendar", params); }
    public Object calendarCategories(Map<String, ?> params) { return request("flashscore-calendar-categories", params); }
    public Object competitions(Map<String, ?> params) { return request("flashscore-competitions", params); }
    public Object entityNews(Map<String, ?> params) { return request("flashscore-entity-news", params); }
    public Object matchBoxScore(Map<String, ?> params) { return request("flashscore-match-box-score", params); }
    public Object matchDarts(Map<String, ?> params) { return request("flashscore-match-darts", params); }
    public Object matchH2h(Map<String, ?> params) { return request("flashscore-match-h2h", params); }
    public Object matchHighlights(Map<String, ?> params) { return request("flashscore-match-highlights", params); }
    public Object matchInfo(Map<String, ?> params) { return request("flashscore-match-info", params); }
    public Object matchLineups(Map<String, ?> params) { return request("flashscore-match-lineups", params); }
    public Object matchMissingPlayers(Map<String, ?> params) { return request("flashscore-match-missing-players", params); }
    public Object matchMomentum(Map<String, ?> params) { return request("flashscore-match-momentum", params); }
    public Object matchNews(Map<String, ?> params) { return request("flashscore-match-news", params); }
    public Object matchOdds(Map<String, ?> params) { return request("flashscore-match-odds", params); }
    public Object matchPlayerStats(Map<String, ?> params) { return request("flashscore-match-player-stats", params); }
    public Object matchPointByPoint(Map<String, ?> params) { return request("flashscore-match-point-by-point", params); }
    public Object matchPredictedLineups(Map<String, ?> params) { return request("flashscore-match-predicted-lineups", params); }
    public Object matchReport(Map<String, ?> params) { return request("flashscore-match-report", params); }
    public Object matchStandings(Map<String, ?> params) { return request("flashscore-match-standings", params); }
    public Object matchStats(Map<String, ?> params) { return request("flashscore-match-stats", params); }
    public Object matchTv(Map<String, ?> params) { return request("flashscore-match-tv", params); }
    public Object navigation(Map<String, ?> params) { return request("flashscore-navigation", params); }
    public Object news(Map<String, ?> params) { return request("flashscore-news", params); }
    public Object newsArticle(Map<String, ?> params) { return request("flashscore-news-article", params); }
    public Object newsArticleBody(Map<String, ?> params) { return request("flashscore-news-article-body", params); }
    public Object newsCategories(Map<String, ?> params) { return request("flashscore-news-categories", params); }
    public Object newsMostRead(Map<String, ?> params) { return request("flashscore-news-most-read", params); }
    public Object oddsGeos(Map<String, ?> params) { return request("flashscore-odds-geos", params); }
    public Object player(Map<String, ?> params) { return request("flashscore-player", params); }
    public Object playerFixtures(Map<String, ?> params) { return request("flashscore-player-fixtures", params); }
    public Object playerInjuries(Map<String, ?> params) { return request("flashscore-player-injuries", params); }
    public Object playerMatchLog(Map<String, ?> params) { return request("flashscore-player-match-log", params); }
    public Object playerNews(Map<String, ?> params) { return request("flashscore-player-news", params); }
    public Object playerResults(Map<String, ?> params) { return request("flashscore-player-results", params); }
    public Object playerTransfers(Map<String, ?> params) { return request("flashscore-player-transfers", params); }
    public Object rankingCategories(Map<String, ?> params) { return request("flashscore-ranking-categories", params); }
    public Object rankings(Map<String, ?> params) { return request("flashscore-rankings", params); }
    public Object scores(Map<String, ?> params) { return request("flashscore-scores", params); }
    public Object search(Map<String, ?> params) { return request("flashscore-search", params); }
    public Object sports(Map<String, ?> params) { return request("flashscore-sports", params); }
    public Object team(Map<String, ?> params) { return request("flashscore-team", params); }
    public Object teamFixtures(Map<String, ?> params) { return request("flashscore-team-fixtures", params); }
    public Object teamNews(Map<String, ?> params) { return request("flashscore-team-news", params); }
    public Object teamOutrightOdds(Map<String, ?> params) { return request("flashscore-team-outright-odds", params); }
    public Object teamResults(Map<String, ?> params) { return request("flashscore-team-results", params); }
    public Object teamSquad(Map<String, ?> params) { return request("flashscore-team-squad", params); }
    public Object teamTransfers(Map<String, ?> params) { return request("flashscore-team-transfers", params); }
    public Object topSearch(Map<String, ?> params) { return request("flashscore-top-search", params); }
    public Object tournamentArchiveSeasons(Map<String, ?> params) { return request("flashscore-tournament-archive-seasons", params); }
    public Object tournamentEvents(Map<String, ?> params) { return request("flashscore-tournament-events", params); }
    public Object tournamentOutrightOdds(Map<String, ?> params) { return request("flashscore-tournament-outright-odds", params); }
    public Object tournamentSeasons(Map<String, ?> params) { return request("flashscore-tournament-seasons", params); }
    public Object tournamentStandings(Map<String, ?> params) { return request("flashscore-tournament-standings", params); }
    public Object tournamentStandingsViews(Map<String, ?> params) { return request("flashscore-tournament-standings-views", params); }

    private static String acceptHeader(Operation operation) {
        return operation.produces().isEmpty() ? "application/json" : String.join(", ", operation.produces());
    }

    private static void validateEnum(Param param, Object value) {
        if (param.enumValues().isEmpty()) return;
        for (Object item : items(value)) {
            if (!param.enumValues().contains(String.valueOf(item))) {
                throw new IllegalArgumentException("invalid " + param.name() + ": expected one of " + param.enumValues());
            }
        }
    }

    private static void addQuery(List<Map.Entry<String, String>> query, Param param, Object value) {
        List<?> values = items(value);
        String delimiter = switch (param.collectionFormat()) {
            case "ssv" -> " ";
            case "tsv" -> "\t";
            case "pipes" -> "|";
            default -> ",";
        };
        if (value instanceof Iterable<?> || value.getClass().isArray()) {
            String joined = String.join(delimiter, values.stream().map(String::valueOf).toList());
            query.add(Map.entry(param.name(), joined));
        } else {
            query.add(Map.entry(param.name(), String.valueOf(value)));
        }
    }

    private static List<?> items(Object value) {
        if (value instanceof Iterable<?> iterable) {
            List<Object> result = new ArrayList<>();
            iterable.forEach(result::add);
            return result;
        }
        if (value != null && value.getClass().isArray()) {
            int length = java.lang.reflect.Array.getLength(value);
            List<Object> result = new ArrayList<>(length);
            for (int i = 0; i < length; i++) result.add(java.lang.reflect.Array.get(value, i));
            return result;
        }
        return List.of(value);
    }

    private static String pathEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8).replace("+", "%20");
    }

    private static String queryEncode(String value) {
        return URLEncoder.encode(value, StandardCharsets.UTF_8);
    }

    @Override public void close() { closed = true; }
}
