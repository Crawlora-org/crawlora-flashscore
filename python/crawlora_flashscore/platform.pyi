from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelFlashscoreTournamentStandingsViewsResponseDoc = TypedDict('ModelFlashscoreTournamentStandingsViewsResponseDoc', {
    'path': NotRequired[str],
    'source_url': NotRequired[str],
    'views': NotRequired[list[str]],
}, total=False)

ModelFlashscoreTournamentStandingsResponseDoc = TypedDict('ModelFlashscoreTournamentStandingsResponseDoc', {
    'data': NotRequired[str],
    'path': NotRequired[str],
    'source_url': NotRequired[str],
    'view': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentSeasonsResponseDoc = TypedDict('ModelFlashscoreTournamentSeasonsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreTournamentSeasonsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentSeasonsDataDoc = TypedDict('ModelFlashscoreTournamentSeasonsDataDoc', {
    'path': NotRequired[str],
    'seasons': NotRequired[list[ModelFlashscoreTournamentSeasonDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentSeasonDoc = TypedDict('ModelFlashscoreTournamentSeasonDoc', {
    'fixtures_path': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'results_path': NotRequired[str],
    'season': NotRequired[str],
    'winner': NotRequired[str],
    'winner_path': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentEventsResponseDoc = TypedDict('ModelFlashscoreTournamentEventsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreTournamentEventsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentEventsDataDoc = TypedDict('ModelFlashscoreTournamentEventsDataDoc', {
    'data': NotRequired[str],
    'event_count': NotRequired[int],
    'page': NotRequired[int],
    'path': NotRequired[str],
    'section': NotRequired[str],
    'source_url': NotRequired[str],
    'total_events': NotRequired[int],
}, total=False)

ModelFlashscoreTopSearchResponseDoc = TypedDict('ModelFlashscoreTopSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreTopSearchDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreTopSearchDataDoc = TypedDict('ModelFlashscoreTopSearchDataDoc', {
    'results': NotRequired[list[ModelFlashscoreSearchResultDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreSearchResultDoc = TypedDict('ModelFlashscoreSearchResultDoc', {
    'defaultCountry': NotRequired[dict[str, Any]],
    'defaultTournament': NotRequired[dict[str, Any]],
    'gender': NotRequired[ModelFlashscoreSearchNamedIddoc],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelFlashscoreSearchImageDoc]],
    'name': NotRequired[str],
    'participantTypes': NotRequired[list[ModelFlashscoreSearchNamedIddoc]],
    'sport': NotRequired[ModelFlashscoreSearchNamedIddoc],
    'superTemplate': NotRequired[dict[str, Any]],
    'teams': NotRequired[list[dict[str, Any]]],
    'type': NotRequired[ModelFlashscoreSearchNamedIddoc],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreSearchNamedIddoc = TypedDict('ModelFlashscoreSearchNamedIddoc', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreSearchImageDoc = TypedDict('ModelFlashscoreSearchImageDoc', {
    'path': NotRequired[str],
    'usageId': NotRequired[int],
    'variantTypeId': NotRequired[int],
}, total=False)

ModelFlashscoreSportsResponseDoc = TypedDict('ModelFlashscoreSportsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreSportsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreSportsDataDoc = TypedDict('ModelFlashscoreSportsDataDoc', {
    'source_url': NotRequired[str],
    'sports': NotRequired[list[ModelFlashscoreSportItemDoc]],
}, total=False)

ModelFlashscoreSportItemDoc = TypedDict('ModelFlashscoreSportItemDoc', {
    'event_count': NotRequired[int],
    'id': NotRequired[int],
    'key': NotRequired[str],
    'league_count': NotRequired[int],
    'name': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelFlashscoreSearchResponseDoc = TypedDict('ModelFlashscoreSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreSearchDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreSearchDataDoc = TypedDict('ModelFlashscoreSearchDataDoc', {
    'query': NotRequired[str],
    'results': NotRequired[list[ModelFlashscoreSearchResultDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreResponseDoc = TypedDict('ModelFlashscoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreSourceDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreSourceDataDoc = TypedDict('ModelFlashscoreSourceDataDoc', {
    'data': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreRankingResponseDoc = TypedDict('ModelFlashscoreRankingResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreRankingDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreRankingDataDoc = TypedDict('ModelFlashscoreRankingDataDoc', {
    'category': NotRequired[ModelFlashscoreRankingCategoryDoc],
    'pages': NotRequired[list[ModelFlashscoreRankingPageDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreRankingPageDoc = TypedDict('ModelFlashscoreRankingPageDoc', {
    'data': NotRequired[str],
    'feed_url': NotRequired[str],
    'page': NotRequired[int],
    'rows': NotRequired[int],
}, total=False)

ModelFlashscoreRankingCategoryDoc = TypedDict('ModelFlashscoreRankingCategoryDoc', {
    'key': NotRequired[str],
    'live': NotRequired[bool],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelFlashscoreRankingCategoriesResponseDoc = TypedDict('ModelFlashscoreRankingCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreRankingCategoriesDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreRankingCategoriesDataDoc = TypedDict('ModelFlashscoreRankingCategoriesDataDoc', {
    'categories': NotRequired[list[ModelFlashscoreRankingCategoryDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsCategoriesResponseDoc = TypedDict('ModelFlashscoreNewsCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreNewsCategoriesDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreNewsCategoriesDataDoc = TypedDict('ModelFlashscoreNewsCategoriesDataDoc', {
    'categories': NotRequired[list[ModelFlashscoreNewsCategoryDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsCategoryDoc = TypedDict('ModelFlashscoreNewsCategoryDoc', {
    'key': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleResponseDoc = TypedDict('ModelFlashscoreNewsArticleResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreNewsArticleDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleDataDoc = TypedDict('ModelFlashscoreNewsArticleDataDoc', {
    'article': NotRequired[ModelFlashscoreNewsArticleDoc],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleDoc = TypedDict('ModelFlashscoreNewsArticleDoc', {
    'edited_at': NotRequired[int],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelFlashscoreNewsImageDoc]],
    'published_at': NotRequired[int],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
}, total=False)

ModelFlashscoreNewsImageDoc = TypedDict('ModelFlashscoreNewsImageDoc', {
    'alt_text': NotRequired[str],
    'credit': NotRequired[str],
    'url': NotRequired[str],
    'variant_type_id': NotRequired[int],
}, total=False)

ModelFlashscoreNewsListResponseDoc = TypedDict('ModelFlashscoreNewsListResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreNewsListDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreNewsListDataDoc = TypedDict('ModelFlashscoreNewsListDataDoc', {
    'articles': NotRequired[list[ModelFlashscoreNewsPreviewDoc]],
    'category': NotRequired[ModelFlashscoreNewsCategoryDoc],
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsPreviewDoc = TypedDict('ModelFlashscoreNewsPreviewDoc', {
    'date': NotRequired[str],
    'id': NotRequired[str],
    'image_alt': NotRequired[str],
    'image_url': NotRequired[str],
    'path': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreNavigationResponseDoc = TypedDict('ModelFlashscoreNavigationResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreNavigationDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreNavigationDataDoc = TypedDict('ModelFlashscoreNavigationDataDoc', {
    'groups': NotRequired[list[ModelFlashscoreNavigationGroupDoc]],
    'path': NotRequired[str],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreNavigationGroupDoc = TypedDict('ModelFlashscoreNavigationGroupDoc', {
    'items': NotRequired[list[ModelFlashscoreNavigationItemDoc]],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreNavigationItemDoc = TypedDict('ModelFlashscoreNavigationItemDoc', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'sport_id': NotRequired[int],
}, total=False)

ModelFlashscoreMatchNewsResponseDoc = TypedDict('ModelFlashscoreMatchNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchNewsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchNewsDataDoc = TypedDict('ModelFlashscoreMatchNewsDataDoc', {
    'layout_id': NotRequired[int],
    'match_id': NotRequired[str],
    'name': NotRequired[str],
    'sections': NotRequired[list[ModelFlashscoreMatchNewsSectionDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreMatchNewsSectionDoc = TypedDict('ModelFlashscoreMatchNewsSectionDoc', {
    'articles': NotRequired[list[ModelFlashscoreMatchNewsArticleRefDoc]],
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreMatchNewsArticleRefDoc = TypedDict('ModelFlashscoreMatchNewsArticleRefDoc', {
    'article': NotRequired[ModelFlashscoreMatchNewsArticleSortKeyDoc],
    'id': NotRequired[str],
}, total=False)

ModelFlashscoreMatchNewsArticleSortKeyDoc = TypedDict('ModelFlashscoreMatchNewsArticleSortKeyDoc', {
    'sort_key': NotRequired[int],
}, total=False)

ModelFlashscoreCompetitionsResponseDoc = TypedDict('ModelFlashscoreCompetitionsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreCompetitionsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreCompetitionsDataDoc = TypedDict('ModelFlashscoreCompetitionsDataDoc', {
    'competitions': NotRequired[list[ModelFlashscoreCompetitionDoc]],
    'day_offset': NotRequired[int],
    'source_url': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelFlashscoreCompetitionDoc = TypedDict('ModelFlashscoreCompetitionDoc', {
    'event_count': NotRequired[int],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'region': NotRequired[str],
}, total=False)

ModelFlashscoreCalendarCategoriesResponseDoc = TypedDict('ModelFlashscoreCalendarCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreCalendarCategoriesDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreCalendarCategoriesDataDoc = TypedDict('ModelFlashscoreCalendarCategoriesDataDoc', {
    'categories': NotRequired[list[ModelFlashscoreCalendarCategoryDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreCalendarCategoryDoc = TypedDict('ModelFlashscoreCalendarCategoryDoc', {
    'key': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'sport': NotRequired[str],
}, total=False)

ModelFlashscoreCalendarResponseDoc = TypedDict('ModelFlashscoreCalendarResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreCalendarDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreCalendarDataDoc = TypedDict('ModelFlashscoreCalendarDataDoc', {
    'category': NotRequired[ModelFlashscoreCalendarCategoryDoc],
    'events': NotRequired[list[ModelFlashscoreCalendarEventDoc]],
    'source_url': NotRequired[str],
    'year': NotRequired[int],
}, total=False)

ModelFlashscoreCalendarEventDoc = TypedDict('ModelFlashscoreCalendarEventDoc', {
    'date': NotRequired[str],
    'month': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'winner': NotRequired[str],
}, total=False)

FlashscoreCalendarResponse = ModelFlashscoreCalendarResponseDoc
FlashscoreCalendarParams = TypedDict('FlashscoreCalendarParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarCategoriesResponse = ModelFlashscoreCalendarCategoriesResponseDoc
FlashscoreCalendarCategoriesParams = TypedDict('FlashscoreCalendarCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreCompetitionsResponse = ModelFlashscoreCompetitionsResponseDoc
FlashscoreCompetitionsParams = TypedDict('FlashscoreCompetitionsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreMatchH2hResponse = ModelFlashscoreResponseDoc
FlashscoreMatchH2hParams = TypedDict('FlashscoreMatchH2hParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsResponse = ModelFlashscoreResponseDoc
FlashscoreMatchHighlightsParams = TypedDict('FlashscoreMatchHighlightsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoResponse = ModelFlashscoreResponseDoc
FlashscoreMatchInfoParams = TypedDict('FlashscoreMatchInfoParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsResponse = ModelFlashscoreResponseDoc
FlashscoreMatchLineupsParams = TypedDict('FlashscoreMatchLineupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsResponse = ModelFlashscoreMatchNewsResponseDoc
FlashscoreMatchNewsParams = TypedDict('FlashscoreMatchNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStandingsResponse = ModelFlashscoreResponseDoc
FlashscoreMatchStandingsParams = TypedDict('FlashscoreMatchStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStatsResponse = ModelFlashscoreResponseDoc
FlashscoreMatchStatsParams = TypedDict('FlashscoreMatchStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreNavigationResponse = ModelFlashscoreNavigationResponseDoc
FlashscoreNavigationParams = TypedDict('FlashscoreNavigationParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNewsResponse = ModelFlashscoreNewsListResponseDoc
FlashscoreNewsParams = TypedDict('FlashscoreNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsArticleResponse = ModelFlashscoreNewsArticleResponseDoc
FlashscoreNewsArticleParams = TypedDict('FlashscoreNewsArticleParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreNewsCategoriesResponse = ModelFlashscoreNewsCategoriesResponseDoc
FlashscoreNewsCategoriesParams = TypedDict('FlashscoreNewsCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreRankingCategoriesResponse = ModelFlashscoreRankingCategoriesResponseDoc
FlashscoreRankingCategoriesParams = TypedDict('FlashscoreRankingCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreRankingsResponse = ModelFlashscoreRankingResponseDoc
FlashscoreRankingsParams = TypedDict('FlashscoreRankingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreScoresResponse = ModelFlashscoreResponseDoc
FlashscoreScoresParams = TypedDict('FlashscoreScoresParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreSearchResponse = ModelFlashscoreSearchResponseDoc
FlashscoreSearchParams = TypedDict('FlashscoreSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

FlashscoreSportsResponse = ModelFlashscoreSportsResponseDoc
FlashscoreSportsParams = TypedDict('FlashscoreSportsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTopSearchResponse = ModelFlashscoreTopSearchResponseDoc
FlashscoreTopSearchParams = TypedDict('FlashscoreTopSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTournamentEventsResponse = ModelFlashscoreTournamentEventsResponseDoc
FlashscoreTournamentEventsParams = TypedDict('FlashscoreTournamentEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentSeasonsResponse = ModelFlashscoreTournamentSeasonsResponseDoc
FlashscoreTournamentSeasonsParams = TypedDict('FlashscoreTournamentSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsResponse = ModelFlashscoreTournamentStandingsResponseDoc
FlashscoreTournamentStandingsParams = TypedDict('FlashscoreTournamentStandingsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsViewsResponse = ModelFlashscoreTournamentStandingsViewsResponseDoc
FlashscoreTournamentStandingsViewsParams = TypedDict('FlashscoreTournamentStandingsViewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)

class FlashscoreGroup:
    def calendar(self, **params: Unpack[FlashscoreCalendarParams]) -> FlashscoreCalendarResponse: ...
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesParams]) -> FlashscoreCalendarCategoriesResponse: ...
    def competitions(self, **params: Unpack[FlashscoreCompetitionsParams]) -> FlashscoreCompetitionsResponse: ...
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hParams]) -> FlashscoreMatchH2hResponse: ...
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsParams]) -> FlashscoreMatchHighlightsResponse: ...
    def match_info(self, **params: Unpack[FlashscoreMatchInfoParams]) -> FlashscoreMatchInfoResponse: ...
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsParams]) -> FlashscoreMatchLineupsResponse: ...
    def match_news(self, **params: Unpack[FlashscoreMatchNewsParams]) -> FlashscoreMatchNewsResponse: ...
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsParams]) -> FlashscoreMatchStandingsResponse: ...
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsParams]) -> FlashscoreMatchStatsResponse: ...
    def navigation(self, **params: Unpack[FlashscoreNavigationParams]) -> FlashscoreNavigationResponse: ...
    def news(self, **params: Unpack[FlashscoreNewsParams]) -> FlashscoreNewsResponse: ...
    def news_article(self, **params: Unpack[FlashscoreNewsArticleParams]) -> FlashscoreNewsArticleResponse: ...
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesParams]) -> FlashscoreNewsCategoriesResponse: ...
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesParams]) -> FlashscoreRankingCategoriesResponse: ...
    def rankings(self, **params: Unpack[FlashscoreRankingsParams]) -> FlashscoreRankingsResponse: ...
    def scores(self, **params: Unpack[FlashscoreScoresParams]) -> FlashscoreScoresResponse: ...
    def search(self, **params: Unpack[FlashscoreSearchParams]) -> FlashscoreSearchResponse: ...
    def sports(self, **params: Unpack[FlashscoreSportsParams]) -> FlashscoreSportsResponse: ...
    def top_search(self, **params: Unpack[FlashscoreTopSearchParams]) -> FlashscoreTopSearchResponse: ...
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsParams]) -> FlashscoreTournamentEventsResponse: ...
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsParams]) -> FlashscoreTournamentSeasonsResponse: ...
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsParams]) -> FlashscoreTournamentStandingsResponse: ...
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

OperationId = Literal[
    'flashscore-calendar',
    'flashscore-calendar-categories',
    'flashscore-competitions',
    'flashscore-match-h2h',
    'flashscore-match-highlights',
    'flashscore-match-info',
    'flashscore-match-lineups',
    'flashscore-match-news',
    'flashscore-match-standings',
    'flashscore-match-stats',
    'flashscore-navigation',
    'flashscore-news',
    'flashscore-news-article',
    'flashscore-news-categories',
    'flashscore-ranking-categories',
    'flashscore-rankings',
    'flashscore-scores',
    'flashscore-search',
    'flashscore-sports',
    'flashscore-top-search',
    'flashscore-tournament-events',
    'flashscore-tournament-seasons',
    'flashscore-tournament-standings',
    'flashscore-tournament-standings-views',
]

class CrawloraClient:
    flashscore: FlashscoreGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-calendar'],
        params: FlashscoreCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCalendarResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-calendar-categories'],
        params: FlashscoreCalendarCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-competitions'],
        params: FlashscoreCompetitionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCompetitionsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-h2h'],
        params: FlashscoreMatchH2hParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchH2hResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-highlights'],
        params: FlashscoreMatchHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-info'],
        params: FlashscoreMatchInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchInfoResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-lineups'],
        params: FlashscoreMatchLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchLineupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-news'],
        params: FlashscoreMatchNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-standings'],
        params: FlashscoreMatchStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-stats'],
        params: FlashscoreMatchStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-navigation'],
        params: FlashscoreNavigationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNavigationResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-news'],
        params: FlashscoreNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-news-article'],
        params: FlashscoreNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsArticleResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-news-categories'],
        params: FlashscoreNewsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-ranking-categories'],
        params: FlashscoreRankingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-rankings'],
        params: FlashscoreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreRankingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-scores'],
        params: FlashscoreScoresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreScoresResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-search'],
        params: FlashscoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-sports'],
        params: FlashscoreSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreSportsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-top-search'],
        params: FlashscoreTopSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTopSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-tournament-events'],
        params: FlashscoreTournamentEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentEventsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-tournament-seasons'],
        params: FlashscoreTournamentSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-tournament-standings'],
        params: FlashscoreTournamentStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-tournament-standings-views'],
        params: FlashscoreTournamentStandingsViewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentStandingsViewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-calendar'],
        params: FlashscoreCalendarParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCalendarResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-calendar-categories'],
        params: FlashscoreCalendarCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-competitions'],
        params: FlashscoreCompetitionsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreCompetitionsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-h2h'],
        params: FlashscoreMatchH2hParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchH2hResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-highlights'],
        params: FlashscoreMatchHighlightsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-info'],
        params: FlashscoreMatchInfoParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchInfoResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-lineups'],
        params: FlashscoreMatchLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchLineupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-news'],
        params: FlashscoreMatchNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-standings'],
        params: FlashscoreMatchStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-stats'],
        params: FlashscoreMatchStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-navigation'],
        params: FlashscoreNavigationParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNavigationResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-news'],
        params: FlashscoreNewsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-news-article'],
        params: FlashscoreNewsArticleParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsArticleResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-news-categories'],
        params: FlashscoreNewsCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-ranking-categories'],
        params: FlashscoreRankingCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-rankings'],
        params: FlashscoreRankingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreRankingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-scores'],
        params: FlashscoreScoresParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreScoresResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-search'],
        params: FlashscoreSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-sports'],
        params: FlashscoreSportsParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreSportsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-top-search'],
        params: FlashscoreTopSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTopSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-tournament-events'],
        params: FlashscoreTournamentEventsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentEventsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-tournament-seasons'],
        params: FlashscoreTournamentSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-tournament-standings'],
        params: FlashscoreTournamentStandingsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-tournament-standings-views'],
        params: FlashscoreTournamentStandingsViewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentStandingsViewsResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class FlashscoreClient(CrawloraClient):
    def __enter__(self) -> FlashscoreClient: ...
    flashscore: FlashscoreGroup
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarParams]) -> FlashscoreCalendarResponse: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationParams]) -> FlashscoreNavigationResponse: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsParams]) -> FlashscoreNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsParams]) -> FlashscoreRankingsResponse: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresParams]) -> FlashscoreScoresResponse: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchParams]) -> FlashscoreSearchResponse: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsParams]) -> FlashscoreSportsResponse: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

class AsyncFlashscoreClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFlashscoreClient: ...
    flashscore: _AsyncFlashscoreGroup
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarParams]) -> FlashscoreCalendarResponse: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationParams]) -> FlashscoreNavigationResponse: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsParams]) -> FlashscoreNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsParams]) -> FlashscoreRankingsResponse: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresParams]) -> FlashscoreScoresResponse: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchParams]) -> FlashscoreSearchResponse: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsParams]) -> FlashscoreSportsResponse: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

class _AsyncFlashscoreGroup:
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarParams]) -> FlashscoreCalendarResponse: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationParams]) -> FlashscoreNavigationResponse: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsParams]) -> FlashscoreNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsParams]) -> FlashscoreRankingsResponse: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresParams]) -> FlashscoreScoresResponse: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchParams]) -> FlashscoreSearchResponse: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsParams]) -> FlashscoreSportsResponse: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

FlashscoreCalendarTextResponseParams = TypedDict('FlashscoreCalendarTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarStreamParams = TypedDict('FlashscoreCalendarStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarCategoriesTextResponseParams = TypedDict('FlashscoreCalendarCategoriesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreCalendarCategoriesStreamParams = TypedDict('FlashscoreCalendarCategoriesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreCompetitionsTextResponseParams = TypedDict('FlashscoreCompetitionsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreCompetitionsStreamParams = TypedDict('FlashscoreCompetitionsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreMatchH2hTextResponseParams = TypedDict('FlashscoreMatchH2hTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchH2hStreamParams = TypedDict('FlashscoreMatchH2hStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsTextResponseParams = TypedDict('FlashscoreMatchHighlightsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsStreamParams = TypedDict('FlashscoreMatchHighlightsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoTextResponseParams = TypedDict('FlashscoreMatchInfoTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoStreamParams = TypedDict('FlashscoreMatchInfoStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsTextResponseParams = TypedDict('FlashscoreMatchLineupsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsStreamParams = TypedDict('FlashscoreMatchLineupsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsTextResponseParams = TypedDict('FlashscoreMatchNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsStreamParams = TypedDict('FlashscoreMatchNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStandingsTextResponseParams = TypedDict('FlashscoreMatchStandingsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStandingsStreamParams = TypedDict('FlashscoreMatchStandingsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStatsTextResponseParams = TypedDict('FlashscoreMatchStatsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStatsStreamParams = TypedDict('FlashscoreMatchStatsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreNavigationTextResponseParams = TypedDict('FlashscoreNavigationTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNavigationStreamParams = TypedDict('FlashscoreNavigationStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNewsTextResponseParams = TypedDict('FlashscoreNewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsStreamParams = TypedDict('FlashscoreNewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsArticleTextResponseParams = TypedDict('FlashscoreNewsArticleTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleStreamParams = TypedDict('FlashscoreNewsArticleStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreNewsCategoriesTextResponseParams = TypedDict('FlashscoreNewsCategoriesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreNewsCategoriesStreamParams = TypedDict('FlashscoreNewsCategoriesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreRankingCategoriesTextResponseParams = TypedDict('FlashscoreRankingCategoriesTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreRankingCategoriesStreamParams = TypedDict('FlashscoreRankingCategoriesStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreRankingsTextResponseParams = TypedDict('FlashscoreRankingsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreRankingsStreamParams = TypedDict('FlashscoreRankingsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreScoresTextResponseParams = TypedDict('FlashscoreScoresTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreScoresStreamParams = TypedDict('FlashscoreScoresStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreSearchTextResponseParams = TypedDict('FlashscoreSearchTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

FlashscoreSearchStreamParams = TypedDict('FlashscoreSearchStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
}, total=False)

FlashscoreSportsTextResponseParams = TypedDict('FlashscoreSportsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreSportsStreamParams = TypedDict('FlashscoreSportsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTopSearchTextResponseParams = TypedDict('FlashscoreTopSearchTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTopSearchStreamParams = TypedDict('FlashscoreTopSearchStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTournamentEventsTextResponseParams = TypedDict('FlashscoreTournamentEventsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentEventsStreamParams = TypedDict('FlashscoreTournamentEventsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentSeasonsTextResponseParams = TypedDict('FlashscoreTournamentSeasonsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentSeasonsStreamParams = TypedDict('FlashscoreTournamentSeasonsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsTextResponseParams = TypedDict('FlashscoreTournamentStandingsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsStreamParams = TypedDict('FlashscoreTournamentStandingsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsViewsTextResponseParams = TypedDict('FlashscoreTournamentStandingsViewsTextResponseParams', {
    '_response_type': Required[Literal['text']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsViewsStreamParams = TypedDict('FlashscoreTournamentStandingsViewsStreamParams', {
    '_response_type': Required[Literal['stream']],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
}, total=False)
