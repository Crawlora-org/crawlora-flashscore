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
    public static final int OPERATION_COUNT = 24;
    public static final List<String> OPERATION_IDS = List.of(
            "flashscore-calendar",
            "flashscore-calendar-categories",
            "flashscore-competitions",
            "flashscore-match-h2h",
            "flashscore-match-highlights",
            "flashscore-match-info",
            "flashscore-match-lineups",
            "flashscore-match-news",
            "flashscore-match-standings",
            "flashscore-match-stats",
            "flashscore-navigation",
            "flashscore-news",
            "flashscore-news-article",
            "flashscore-news-categories",
            "flashscore-ranking-categories",
            "flashscore-rankings",
            "flashscore-scores",
            "flashscore-search",
            "flashscore-sports",
            "flashscore-top-search",
            "flashscore-tournament-events",
            "flashscore-tournament-seasons",
            "flashscore-tournament-standings",
            "flashscore-tournament-standings-views"
    );

    private static final Map<String, Operation> OPERATIONS;
    static {
        Map<String, Operation> operations = new LinkedHashMap<>();
        operations.put("flashscore-calendar", new Operation("flashscore-calendar", "GET", "/flashscore/calendar", Map.ofEntries(Map.entry("category", new Param("category", "query", true, "string", List.of("tennis-atp", "tennis-wta", "golf-pga", "golf-dp-world", "badminton-bwf", "motorsport-f1"), "csv"))), List.of("application/json")));
        operations.put("flashscore-calendar-categories", new Operation("flashscore-calendar-categories", "GET", "/flashscore/calendar-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-competitions", new Operation("flashscore-competitions", "GET", "/flashscore/competitions", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"), "csv")), Map.entry("day_offset", new Param("day_offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-h2h", new Operation("flashscore-match-h2h", "GET", "/flashscore/match-h2h", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-highlights", new Operation("flashscore-match-highlights", "GET", "/flashscore/match-highlights", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-info", new Operation("flashscore-match-info", "GET", "/flashscore/match-info", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-lineups", new Operation("flashscore-match-lineups", "GET", "/flashscore/match-lineups", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-news", new Operation("flashscore-match-news", "GET", "/flashscore/match-news", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-standings", new Operation("flashscore-match-standings", "GET", "/flashscore/match-standings", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv")), Map.entry("view", new Param("view", "query", false, "string", List.of("overall", "home", "away", "form_overall", "overunder_overall", "form_home", "form_away", "top_scorers", "htft_overall", "htft_home", "htft_away", "live_overall", "overunder_home", "overunder_away"), "csv"))), List.of("application/json")));
        operations.put("flashscore-match-stats", new Operation("flashscore-match-stats", "GET", "/flashscore/match-stats", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-navigation", new Operation("flashscore-navigation", "GET", "/flashscore/navigation", Map.ofEntries(Map.entry("path", new Param("path", "query", false, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news", new Operation("flashscore-news", "GET", "/flashscore/news", Map.ofEntries(Map.entry("category", new Param("category", "query", false, "string", List.of("all", "football", "uefa-nations-league", "tennis", "features", "premier-league", "nfl", "mlb", "nba", "nhl", "formula-1", "champions-league", "europa-league", "conference-league", "darts", "snooker", "golf", "road-cycling", "laliga", "bundesliga", "serie-a", "ligue-1", "badminton", "handball", "hockey", "basketball", "cricket", "rugby-union", "athletics", "baseball", "fifa", "rugby-league", "motorsport", "aussie-rules", "flashscore-ratings", "american-sports", "african-football", "combat-sports", "winter-sports", "transfer-news"), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news-article", new Operation("flashscore-news-article", "GET", "/flashscore/news-article", Map.ofEntries(Map.entry("id", new Param("id", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-news-categories", new Operation("flashscore-news-categories", "GET", "/flashscore/news-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-ranking-categories", new Operation("flashscore-ranking-categories", "GET", "/flashscore/ranking-categories", Map.of(), List.of("application/json")));
        operations.put("flashscore-rankings", new Operation("flashscore-rankings", "GET", "/flashscore/rankings", Map.ofEntries(Map.entry("category", new Param("category", "query", true, "string", List.of("fifa", "tennis-atp", "tennis-wta", "tennis-atp-race", "tennis-wta-race", "tennis-atp-doubles", "tennis-wta-doubles", "tennis-atp-doubles-race", "tennis-wta-doubles-race", "badminton-bwf-singles-men", "badminton-bwf-singles-women", "badminton-bwf-doubles-men", "badminton-bwf-doubles-women", "badminton-bwf-mixed-doubles", "golf-owgr", "golf-wwgr", "golf-pga-fedexcup", "golf-pga-money", "golf-dp-world-tour", "golf-lpga", "golf-asian-tour", "golf-japan-tour", "golf-sunshine-tour", "golf-korn-ferry", "golf-champions-tour", "darts-world-ranking", "snooker-world-ranking", "tennis-atp-live", "tennis-wta-live", "tennis-atp-race-live", "tennis-wta-race-live", "tennis-atp-doubles-live", "tennis-wta-doubles-live", "tennis-atp-doubles-race-live", "tennis-wta-doubles-race-live"), "csv"))), List.of("application/json")));
        operations.put("flashscore-scores", new Operation("flashscore-scores", "GET", "/flashscore/scores", Map.ofEntries(Map.entry("sport", new Param("sport", "query", true, "string", List.of("football", "tennis", "basketball", "hockey", "golf", "formula-1", "baseball", "snooker", "american-football", "aussie-rules", "badminton", "bandy", "beach-soccer", "beach-volleyball", "boxing", "cricket", "cycling", "darts", "esports", "field-hockey", "floorball", "futsal", "handball", "horse-racing", "kabaddi", "mma", "motorsport", "netball", "pesapallo", "rugby-league", "rugby-union", "table-tennis", "volleyball", "water-polo", "winter-sports"), "csv")), Map.entry("day_offset", new Param("day_offset", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-search", new Operation("flashscore-search", "GET", "/flashscore/search", Map.ofEntries(Map.entry("q", new Param("q", "query", true, "string", List.of(), "csv"))), List.of("application/json")));
        operations.put("flashscore-sports", new Operation("flashscore-sports", "GET", "/flashscore/sports", Map.of(), List.of("application/json")));
        operations.put("flashscore-top-search", new Operation("flashscore-top-search", "GET", "/flashscore/top-search", Map.of(), List.of("application/json")));
        operations.put("flashscore-tournament-events", new Operation("flashscore-tournament-events", "GET", "/flashscore/tournament-events", Map.ofEntries(Map.entry("path", new Param("path", "query", true, "string", List.of(), "csv")), Map.entry("page", new Param("page", "query", false, "integer", List.of(), "csv"))), List.of("application/json")));
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
    public Object matchH2h(Map<String, ?> params) { return request("flashscore-match-h2h", params); }
    public Object matchHighlights(Map<String, ?> params) { return request("flashscore-match-highlights", params); }
    public Object matchInfo(Map<String, ?> params) { return request("flashscore-match-info", params); }
    public Object matchLineups(Map<String, ?> params) { return request("flashscore-match-lineups", params); }
    public Object matchNews(Map<String, ?> params) { return request("flashscore-match-news", params); }
    public Object matchStandings(Map<String, ?> params) { return request("flashscore-match-standings", params); }
    public Object matchStats(Map<String, ?> params) { return request("flashscore-match-stats", params); }
    public Object navigation(Map<String, ?> params) { return request("flashscore-navigation", params); }
    public Object news(Map<String, ?> params) { return request("flashscore-news", params); }
    public Object newsArticle(Map<String, ?> params) { return request("flashscore-news-article", params); }
    public Object newsCategories(Map<String, ?> params) { return request("flashscore-news-categories", params); }
    public Object rankingCategories(Map<String, ?> params) { return request("flashscore-ranking-categories", params); }
    public Object rankings(Map<String, ?> params) { return request("flashscore-rankings", params); }
    public Object scores(Map<String, ?> params) { return request("flashscore-scores", params); }
    public Object search(Map<String, ?> params) { return request("flashscore-search", params); }
    public Object sports(Map<String, ?> params) { return request("flashscore-sports", params); }
    public Object topSearch(Map<String, ?> params) { return request("flashscore-top-search", params); }
    public Object tournamentEvents(Map<String, ?> params) { return request("flashscore-tournament-events", params); }
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
