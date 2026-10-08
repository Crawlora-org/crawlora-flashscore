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
    'winners': NotRequired[list[ModelFlashscoreTournamentSeasonWinnerDoc]],
}, total=False)

ModelFlashscoreTournamentSeasonWinnerDoc = TypedDict('ModelFlashscoreTournamentSeasonWinnerDoc', {
    'name': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelFlashscoreTournamentOutrightOddsResponse = TypedDict('ModelFlashscoreTournamentOutrightOddsResponse', {
    'bookmakers': NotRequired[list[ModelFlashscoreOddsBookmaker]],
    'geo': NotRequired[str],
    'has_more': NotRequired[bool],
    'participants': NotRequired[list[ModelFlashscoreOutrightParticipant]],
    'source_url': NotRequired[str],
    'subdivision': NotRequired[str],
    'tournament_id': NotRequired[str],
}, total=False)

ModelFlashscoreOutrightParticipant = TypedDict('ModelFlashscoreOutrightParticipant', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'offers': NotRequired[list[ModelFlashscoreOutrightOffer]],
}, total=False)

ModelFlashscoreOutrightOffer = TypedDict('ModelFlashscoreOutrightOffer', {
    'active': NotRequired[bool],
    'best': NotRequired[bool],
    'bookmaker_id': NotRequired[int],
    'change': NotRequired[Literal['UP', 'DOWN']],
    'odds': NotRequired[float],
}, total=False)

ModelFlashscoreOddsBookmaker = TypedDict('ModelFlashscoreOddsBookmaker', {
    'id': NotRequired[int],
    'name': NotRequired[str],
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

ModelFlashscoreTournamentArchiveSeasonsResponse = TypedDict('ModelFlashscoreTournamentArchiveSeasonsResponse', {
    'league_key': NotRequired[str],
    'season_count': NotRequired[int],
    'seasons': NotRequired[list[ModelFlashscoreArchiveSeason]],
    'source_url': NotRequired[str],
    'stage': NotRequired[ModelFlashscoreArchiveStage],
    'stage_id': NotRequired[str],
    'tournament_template_id': NotRequired[str],
}, total=False)

ModelFlashscoreArchiveStage = TypedDict('ModelFlashscoreArchiveStage', {
    'country': NotRequired[str],
    'end_estimated': NotRequired[str],
    'group': NotRequired[str],
    'id': NotRequired[str],
    'is_final': NotRequired[bool],
    'name': NotRequired[str],
    'start_estimated': NotRequired[str],
    'tabs': NotRequired[list[ModelFlashscoreArchiveTab]],
    'tournament': NotRequired[str],
    'type_id': NotRequired[int],
}, total=False)

ModelFlashscoreArchiveTab = TypedDict('ModelFlashscoreArchiveTab', {
    'id': NotRequired[Literal['SU', 'OD', 'TA', 'RE', 'FI', 'DR', 'NF']],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreArchiveSeason = TypedDict('ModelFlashscoreArchiveSeason', {
    'end_year': NotRequired[str],
    'is_current': NotRequired[bool],
    'is_requested': NotRequired[bool],
    'season': NotRequired[str],
    'stage_ids': NotRequired[list[str]],
    'start_year': NotRequired[str],
    'tournament_id': NotRequired[str],
    'winners': NotRequired[list[ModelFlashscoreArchiveWinner]],
}, total=False)

ModelFlashscoreArchiveWinner = TypedDict('ModelFlashscoreArchiveWinner', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'slug': NotRequired[str],
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

ModelFlashscoreTeamTransfersResponse = TypedDict('ModelFlashscoreTeamTransfersResponse', {
    'page': NotRequired[int],
    'source_url': NotRequired[str],
    'team_id': NotRequired[str],
    'team_name': NotRequired[str],
    'transfer_count': NotRequired[int],
    'transfers': NotRequired[list[ModelFlashscoreTeamTransfer]],
    'type': NotRequired[str],
}, total=False)

ModelFlashscoreTeamTransfer = TypedDict('ModelFlashscoreTeamTransfer', {
    'date': NotRequired[str],
    'direction': NotRequired[str],
    'fee': NotRequired[str],
    'from': NotRequired[ModelFlashscoreTransferTeam],
    'player': NotRequired[ModelFlashscoreTransferPlayer],
    'to': NotRequired[ModelFlashscoreTransferTeam],
    'type': NotRequired[str],
}, total=False)

ModelFlashscoreTransferTeam = TypedDict('ModelFlashscoreTransferTeam', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreTransferPlayer = TypedDict('ModelFlashscoreTransferPlayer', {
    'country': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreTeamSquadResponse = TypedDict('ModelFlashscoreTeamSquadResponse', {
    'groups': NotRequired[list[ModelFlashscoreSquadGroup]],
    'scope': NotRequired[ModelFlashscoreSquadScope],
    'scopes': NotRequired[list[ModelFlashscoreSquadScope]],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelFlashscoreTeamProfile],
}, total=False)

ModelFlashscoreTeamProfile = TypedDict('ModelFlashscoreTeamProfile', {
    'country': NotRequired[str],
    'country_id': NotRequired[int],
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'sport_id': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreSquadScope = TypedDict('ModelFlashscoreSquadScope', {
    'key': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreSquadGroup = TypedDict('ModelFlashscoreSquadGroup', {
    'columns': NotRequired[list[ModelFlashscoreSquadColumn]],
    'name': NotRequired[str],
    'players': NotRequired[list[ModelFlashscoreSquadPlayer]],
}, total=False)

ModelFlashscoreSquadPlayer = TypedDict('ModelFlashscoreSquadPlayer', {
    'absence': NotRequired[str],
    'age': NotRequired[int],
    'club': NotRequired[str],
    'country': NotRequired[str],
    'jersey_number': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'player_id': NotRequired[str],
    'slug': NotRequired[str],
    'stats': NotRequired[dict[str, Any]],
}, total=False)

ModelFlashscoreSquadColumn = TypedDict('ModelFlashscoreSquadColumn', {
    'key': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelFlashscoreTeamEventsResponse = TypedDict('ModelFlashscoreTeamEventsResponse', {
    'event_count': NotRequired[int],
    'events': NotRequired[list[ModelFlashscoreTeamEvent]],
    'page': NotRequired[int],
    'section': NotRequired[str],
    'source_url': NotRequired[str],
    'team_id': NotRequired[str],
    'team_name': NotRequired[str],
}, total=False)

ModelFlashscoreTeamEvent = TypedDict('ModelFlashscoreTeamEvent', {
    'away': NotRequired[ModelFlashscoreEventSide],
    'away_score': NotRequired[int],
    'competition': NotRequired[ModelFlashscoreEventCompetition],
    'home': NotRequired[ModelFlashscoreEventSide],
    'home_score': NotRequired[int],
    'id': NotRequired[str],
    'stage': NotRequired[str],
    'stage_code': NotRequired[int],
    'start_time': NotRequired[int],
    'start_time_iso': NotRequired[str],
    'status_code': NotRequired[int],
}, total=False)

ModelFlashscoreEventSide = TypedDict('ModelFlashscoreEventSide', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreEventCompetition = TypedDict('ModelFlashscoreEventCompetition', {
    'country': NotRequired[str],
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'stage_id': NotRequired[str],
    'tournament_id': NotRequired[str],
    'tournament_stage_id': NotRequired[str],
}, total=False)

ModelFlashscoreTeamOutrightOddsResponse = TypedDict('ModelFlashscoreTeamOutrightOddsResponse', {
    'bookmakers': NotRequired[list[ModelFlashscoreOddsBookmaker]],
    'geo': NotRequired[str],
    'has_more': NotRequired[bool],
    'source_url': NotRequired[str],
    'subdivision': NotRequired[str],
    'team_id': NotRequired[str],
    'team_name': NotRequired[str],
    'tournaments': NotRequired[list[ModelFlashscoreOutrightTournament]],
}, total=False)

ModelFlashscoreOutrightTournament = TypedDict('ModelFlashscoreOutrightTournament', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'offers': NotRequired[list[ModelFlashscoreOutrightOffer]],
}, total=False)

ModelFlashscoreTeamNewsResponse = TypedDict('ModelFlashscoreTeamNewsResponse', {
    'item_count': NotRequired[int],
    'items': NotRequired[list[ModelFlashscoreTeamNewsItem]],
    'source_url': NotRequired[str],
    'team_id': NotRequired[str],
    'team_name': NotRequired[str],
}, total=False)

ModelFlashscoreTeamNewsItem = TypedDict('ModelFlashscoreTeamNewsItem', {
    'id': NotRequired[str],
    'image_url': NotRequired[str],
    'link': NotRequired[str],
    'published_at': NotRequired[int],
    'published_at_iso': NotRequired[str],
    'publisher': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreTeamResponse = TypedDict('ModelFlashscoreTeamResponse', {
    'competitions': NotRequired[list[ModelFlashscoreTeamCompetition]],
    'page_url': NotRequired[str],
    'source_url': NotRequired[str],
    'team': NotRequired[ModelFlashscoreTeamProfile],
    'venue': NotRequired[ModelFlashscoreTeamVenue],
}, total=False)

ModelFlashscoreTeamVenue = TypedDict('ModelFlashscoreTeamVenue', {
    'capacity': NotRequired[int],
    'city': NotRequired[str],
    'stadium': NotRequired[str],
}, total=False)

ModelFlashscoreTeamCompetition = TypedDict('ModelFlashscoreTeamCompetition', {
    'country': NotRequired[str],
    'full_name': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
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

ModelFlashscorePlayerTransfersResponse = TypedDict('ModelFlashscorePlayerTransfersResponse', {
    'page_url': NotRequired[str],
    'player': NotRequired[ModelFlashscorePlayerProfile],
    'source_url': NotRequired[str],
    'transfer_count': NotRequired[int],
    'transfers': NotRequired[list[ModelFlashscorePlayerTransfer]],
}, total=False)

ModelFlashscorePlayerTransfer = TypedDict('ModelFlashscorePlayerTransfer', {
    'date': NotRequired[str],
    'fee': NotRequired[str],
    'from': NotRequired[ModelFlashscoreTransferTeam],
    'to': NotRequired[ModelFlashscoreTransferTeam],
    'type': NotRequired[str],
}, total=False)

ModelFlashscorePlayerProfile = TypedDict('ModelFlashscorePlayerProfile', {
    'birth_date': NotRequired[str],
    'country': NotRequired[str],
    'country_id': NotRequired[int],
    'full_name': NotRequired[str],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'photo_url': NotRequired[str],
    'ranking': NotRequired[str],
    'slug': NotRequired[str],
    'sport': NotRequired[str],
    'sport_id': NotRequired[int],
    'team': NotRequired[ModelFlashscorePlayerTeam],
    'url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerTeam = TypedDict('ModelFlashscorePlayerTeam', {
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscorePlayerEventsResponse = TypedDict('ModelFlashscorePlayerEventsResponse', {
    'event_count': NotRequired[int],
    'events': NotRequired[list[ModelFlashscoreTeamEvent]],
    'page': NotRequired[int],
    'player_id': NotRequired[str],
    'player_name': NotRequired[str],
    'section': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerNewsResponse = TypedDict('ModelFlashscorePlayerNewsResponse', {
    'item_count': NotRequired[int],
    'items': NotRequired[list[ModelFlashscoreTeamNewsItem]],
    'player_id': NotRequired[str],
    'player_name': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchLogResponse = TypedDict('ModelFlashscorePlayerMatchLogResponse', {
    'has_more': NotRequired[bool],
    'page': NotRequired[int],
    'player': NotRequired[ModelFlashscorePlayerProfile],
    'row_count': NotRequired[int],
    'rows': NotRequired[list[ModelFlashscorePlayerMatchLogRow]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchLogRow = TypedDict('ModelFlashscorePlayerMatchLogRow', {
    'absence': NotRequired[ModelFlashscorePlayerMatchLogAbsence],
    'away': NotRequired[ModelFlashscorePlayerMatchLogSide],
    'date': NotRequired[str],
    'date_text': NotRequired[str],
    'event_id': NotRequired[str],
    'home': NotRequired[ModelFlashscorePlayerMatchLogSide],
    'rating': NotRequired[float],
    'rating_rank': NotRequired[int],
    'result': NotRequired[Literal['win', 'draw', 'loss']],
    'stage': NotRequired[Literal['finished', 'finished_after_extra_time', 'finished_after_penalties', 'other']],
    'stage_code': NotRequired[int],
    'stats': NotRequired[list[ModelFlashscorePlayerMatchLogStat]],
    'stats_available': NotRequired[bool],
    'tournament': NotRequired[ModelFlashscorePlayerMatchLogTournament],
}, total=False)

ModelFlashscorePlayerMatchLogTournament = TypedDict('ModelFlashscorePlayerMatchLogTournament', {
    'country': NotRequired[str],
    'country_id': NotRequired[int],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'season': NotRequired[str],
    'short_code': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchLogStat = TypedDict('ModelFlashscorePlayerMatchLogStat', {
    'id': NotRequired[int],
    'key': NotRequired[str],
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchLogSide = TypedDict('ModelFlashscorePlayerMatchLogSide', {
    'full_time_score': NotRequired[int],
    'id': NotRequired[str],
    'logo_url': NotRequired[str],
    'name': NotRequired[str],
    'penalties_score': NotRequired[int],
    'score': NotRequired[int],
    'score_after_extra_time': NotRequired[int],
    'short_name': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchLogAbsence = TypedDict('ModelFlashscorePlayerMatchLogAbsence', {
    'category': NotRequired[str],
    'detail': NotRequired[str],
}, total=False)

ModelFlashscorePlayerInjuriesResponse = TypedDict('ModelFlashscorePlayerInjuriesResponse', {
    'injuries': NotRequired[list[ModelFlashscorePlayerInjury]],
    'injury_count': NotRequired[int],
    'page_url': NotRequired[str],
    'player': NotRequired[ModelFlashscorePlayerProfile],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerInjury = TypedDict('ModelFlashscorePlayerInjury', {
    'from': NotRequired[str],
    'type': NotRequired[str],
    'until': NotRequired[str],
}, total=False)

ModelFlashscorePlayerResponse = TypedDict('ModelFlashscorePlayerResponse', {
    'age': NotRequired[int],
    'career': NotRequired[list[ModelFlashscoreCareerTab]],
    'contract_expires': NotRequired[str],
    'details': NotRequired[list[ModelFlashscorePlayerDetail]],
    'market_value': NotRequired[str],
    'page_url': NotRequired[str],
    'player': NotRequired[ModelFlashscorePlayerProfile],
    'position': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePlayerDetail = TypedDict('ModelFlashscorePlayerDetail', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelFlashscoreCareerTab = TypedDict('ModelFlashscoreCareerTab', {
    'columns': NotRequired[list[ModelFlashscoreSquadColumn]],
    'key': NotRequired[str],
    'name': NotRequired[str],
    'rows': NotRequired[list[ModelFlashscoreCareerRow]],
    'total': NotRequired[dict[str, Any]],
}, total=False)

ModelFlashscoreCareerRow = TypedDict('ModelFlashscoreCareerRow', {
    'competition': NotRequired[ModelFlashscoreCareerCompetition],
    'parts': NotRequired[list[ModelFlashscoreCareerPart]],
    'season': NotRequired[str],
    'stats': NotRequired[dict[str, Any]],
    'team': NotRequired[ModelFlashscoreCareerTeam],
}, total=False)

ModelFlashscoreCareerTeam = TypedDict('ModelFlashscoreCareerTeam', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreCareerPart = TypedDict('ModelFlashscoreCareerPart', {
    'stage': NotRequired[str],
    'stats': NotRequired[dict[str, Any]],
}, total=False)

ModelFlashscoreCareerCompetition = TypedDict('ModelFlashscoreCareerCompetition', {
    'name': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelFlashscoreOddsGeosResponseDoc = TypedDict('ModelFlashscoreOddsGeosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreOddsGeosDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreOddsGeosDataDoc = TypedDict('ModelFlashscoreOddsGeosDataDoc', {
    'betting_scopes': NotRequired[list[str]],
    'betting_types': NotRequired[list[str]],
    'default_geo': NotRequired[str],
    'geos': NotRequired[list[ModelFlashscoreOddsGeoDoc]],
    'handicap_types': NotRequired[list[str]],
    'subdivision_notes': NotRequired[str],
    'subdivisions': NotRequired[list[ModelFlashscoreOddsSubdivisionDoc]],
    'verified_on': NotRequired[str],
}, total=False)

ModelFlashscoreOddsSubdivisionDoc = TypedDict('ModelFlashscoreOddsSubdivisionDoc', {
    'code': NotRequired[str],
    'geo': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreOddsGeoDoc = TypedDict('ModelFlashscoreOddsGeoDoc', {
    'code': NotRequired[str],
    'has_bookmakers': NotRequired[bool],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreNewsMostReadResponse = TypedDict('ModelFlashscoreNewsMostReadResponse', {
    'article_count': NotRequired[int],
    'articles': NotRequired[list[ModelFlashscoreMostReadArticle]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreMostReadArticle = TypedDict('ModelFlashscoreMostReadArticle', {
    'edited_at': NotRequired[int],
    'id': NotRequired[str],
    'image_alt': NotRequired[str],
    'image_credit': NotRequired[str],
    'image_url': NotRequired[str],
    'path': NotRequired[str],
    'published_at': NotRequired[int],
    'published_at_iso': NotRequired[str],
    'slug': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
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
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[Literal['SPORT', 'TOURNAMENT_TEMPLATE', 'TAG']],
    'key': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleBodyResponse = TypedDict('ModelFlashscoreNewsArticleBodyResponse', {
    'article': NotRequired[ModelFlashscoreNewsArticleBody],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleBody = TypedDict('ModelFlashscoreNewsArticleBody', {
    'author': NotRequired[str],
    'block_count': NotRequired[int],
    'blocks': NotRequired[list[ModelFlashscoreNewsBodyBlock]],
    'credit': NotRequired[str],
    'edited_at': NotRequired[int],
    'edited_at_iso': NotRequired[str],
    'id': NotRequired[str],
    'image': NotRequired[ModelFlashscoreNewsCoverImage],
    'perex': NotRequired[str],
    'published_at': NotRequired[int],
    'published_at_iso': NotRequired[str],
    'slug': NotRequired[str],
    'tags': NotRequired[list[ModelFlashscoreNewsArticleTag]],
    'text': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsArticleTag = TypedDict('ModelFlashscoreNewsArticleTag', {
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[Literal['SPORT', 'PARTICIPANT', 'TOURNAMENT_TEMPLATE', 'TAG']],
    'label': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreNewsCoverImage = TypedDict('ModelFlashscoreNewsCoverImage', {
    'alt_text': NotRequired[str],
    'credit': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreNewsBodyBlock = TypedDict('ModelFlashscoreNewsBodyBlock', {
    'alt': NotRequired[str],
    'credit': NotRequired[str],
    'height': NotRequired[int],
    'id': NotRequired[str],
    'level': NotRequired[int],
    'links': NotRequired[list[ModelFlashscoreNewsBodyLink]],
    'provider': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[Literal['paragraph', 'heading', 'embed', 'image', 'infobox']],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelFlashscoreNewsBodyLink = TypedDict('ModelFlashscoreNewsBodyLink', {
    'id': NotRequired[str],
    'kind': NotRequired[Literal['link', 'participant', 'player', 'event', 'tournament', 'article']],
    'sport_id': NotRequired[int],
    'text': NotRequired[str],
    'url': NotRequired[str],
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

ModelFlashscoreMatchTvresponseDoc = TypedDict('ModelFlashscoreMatchTvresponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchTvdataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchTvdataDoc = TypedDict('ModelFlashscoreMatchTvdataDoc', {
    'broadcasters': NotRequired[list[ModelFlashscoreBroadcasterDoc]],
    'geo': NotRequired[str],
    'match_id': NotRequired[str],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreBroadcasterDoc = TypedDict('ModelFlashscoreBroadcasterDoc', {
    'affiliate': NotRequired[bool],
    'id': NotRequired[int],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreMatchReportResponseDoc = TypedDict('ModelFlashscoreMatchReportResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchReportDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchReportDataDoc = TypedDict('ModelFlashscoreMatchReportDataDoc', {
    'match_id': NotRequired[str],
    'report': NotRequired[ModelFlashscoreMatchReportDoc],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscoreMatchReportDoc = TypedDict('ModelFlashscoreMatchReportDoc', {
    'author': NotRequired[str],
    'content': NotRequired[list[ModelFlashscoreReportBlockDoc]],
    'edited_at': NotRequired[str],
    'id': NotRequired[str],
    'images': NotRequired[list[ModelFlashscoreReportImageDoc]],
    'published_at': NotRequired[str],
    'text': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreReportImageDoc = TypedDict('ModelFlashscoreReportImageDoc', {
    'alt': NotRequired[str],
    'credit': NotRequired[str],
    'thumbnail_url': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreReportBlockDoc = TypedDict('ModelFlashscoreReportBlockDoc', {
    'alt': NotRequired[str],
    'bold': NotRequired[bool],
    'credit': NotRequired[str],
    'height': NotRequired[int],
    'links': NotRequired[list[ModelFlashscoreReportLinkDoc]],
    'text': NotRequired[str],
    'type': NotRequired[Literal['paragraph', 'image']],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

ModelFlashscoreReportLinkDoc = TypedDict('ModelFlashscoreReportLinkDoc', {
    'id': NotRequired[str],
    'text': NotRequired[str],
    'type': NotRequired[Literal['team', 'player', 'competition', 'page']],
    'url': NotRequired[str],
}, total=False)

ModelFlashscoreMatchPredictedLineupsResponseDoc = TypedDict('ModelFlashscoreMatchPredictedLineupsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchPredictedLineupsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchPredictedLineupsDataDoc = TypedDict('ModelFlashscoreMatchPredictedLineupsDataDoc', {
    'match_id': NotRequired[str],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelFlashscorePredictedLineupTeamDoc]],
}, total=False)

ModelFlashscorePredictedLineupTeamDoc = TypedDict('ModelFlashscorePredictedLineupTeamDoc', {
    'aggregated_stats': NotRequired[ModelFlashscoreLineupAggregatedStatsDoc],
    'coaches': NotRequired[list[ModelFlashscoreLineupPlayerDoc]],
    'formation': NotRequired[ModelFlashscorePredictedFormationDoc],
    'groups': NotRequired[list[ModelFlashscoreLineupGroupDoc]],
    'name': NotRequired[str],
    'participant_id': NotRequired[str],
    'players': NotRequired[list[ModelFlashscoreLineupPlayerDoc]],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreLineupPlayerDoc = TypedDict('ModelFlashscoreLineupPlayerDoc', {
    'age': NotRequired[float],
    'average_rating': NotRequired[float],
    'country': NotRequired[str],
    'height_cm': NotRequired[float],
    'id': NotRequired[str],
    'list_name': NotRequired[str],
    'market_value': NotRequired[float],
    'name': NotRequired[str],
    'number': NotRequired[str],
    'roles': NotRequired[list[ModelFlashscoreLineupRoleDoc]],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreLineupRoleDoc = TypedDict('ModelFlashscoreLineupRoleDoc', {
    'suffix': NotRequired[str],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreLineupGroupDoc = TypedDict('ModelFlashscoreLineupGroupDoc', {
    'name': NotRequired[str],
    'player_ids': NotRequired[list[str]],
    'type': NotRequired[str],
}, total=False)

ModelFlashscorePredictedFormationDoc = TypedDict('ModelFlashscorePredictedFormationDoc', {
    'lines': NotRequired[list[ModelFlashscoreFormationLineDoc]],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreFormationLineDoc = TypedDict('ModelFlashscoreFormationLineDoc', {
    'number': NotRequired[int],
    'rows': NotRequired[list[ModelFlashscoreFormationRowDoc]],
}, total=False)

ModelFlashscoreFormationRowDoc = TypedDict('ModelFlashscoreFormationRowDoc', {
    'player_ids': NotRequired[list[str]],
    'sort_key': NotRequired[int],
}, total=False)

ModelFlashscoreLineupAggregatedStatsDoc = TypedDict('ModelFlashscoreLineupAggregatedStatsDoc', {
    'average_age': NotRequired[float],
    'average_height_cm': NotRequired[float],
    'average_rating': NotRequired[float],
    'sum_market_value': NotRequired[float],
}, total=False)

ModelFlashscoreMatchPointByPointResponseDoc = TypedDict('ModelFlashscoreMatchPointByPointResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchPointByPointDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchPointByPointDataDoc = TypedDict('ModelFlashscoreMatchPointByPointDataDoc', {
    'current_game': NotRequired[ModelFlashscorePointByPointCurrentGameDoc],
    'match_id': NotRequired[str],
    'periods': NotRequired[list[ModelFlashscorePointByPointPeriodDoc]],
    'source_url': NotRequired[str],
}, total=False)

ModelFlashscorePointByPointPeriodDoc = TypedDict('ModelFlashscorePointByPointPeriodDoc', {
    'sections': NotRequired[list[ModelFlashscorePointByPointSectionDoc]],
    'title': NotRequired[str],
}, total=False)

ModelFlashscorePointByPointSectionDoc = TypedDict('ModelFlashscorePointByPointSectionDoc', {
    'entries': NotRequired[list[ModelFlashscorePointByPointEntryDoc]],
    'title': NotRequired[str],
}, total=False)

ModelFlashscorePointByPointEntryDoc = TypedDict('ModelFlashscorePointByPointEntryDoc', {
    'away_score': NotRequired[int],
    'away_tiebreak_score': NotRequired[int],
    'home_score': NotRequired[int],
    'home_tiebreak_score': NotRequired[int],
    'lead': NotRequired[ModelFlashscorePointByPointLeadDoc],
    'markers': NotRequired[list[ModelFlashscorePointMarkerDoc]],
    'number': NotRequired[int],
    'points': NotRequired[list[ModelFlashscorePointScoreDoc]],
    'server': NotRequired[Literal['home', 'away']],
    'server_lost': NotRequired[bool],
    'winner': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscorePointScoreDoc = TypedDict('ModelFlashscorePointScoreDoc', {
    'away': NotRequired[str],
    'home': NotRequired[str],
    'markers': NotRequired[list[ModelFlashscorePointMarkerDoc]],
}, total=False)

ModelFlashscorePointMarkerDoc = TypedDict('ModelFlashscorePointMarkerDoc', {
    'side': NotRequired[Literal['home', 'away']],
    'type': NotRequired[Literal['break_point', 'set_point', 'match_point']],
}, total=False)

ModelFlashscorePointByPointLeadDoc = TypedDict('ModelFlashscorePointByPointLeadDoc', {
    'margin': NotRequired[int],
    'narrowed': NotRequired[bool],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscorePointByPointCurrentGameDoc = TypedDict('ModelFlashscorePointByPointCurrentGameDoc', {
    'points': NotRequired[list[ModelFlashscorePointScoreDoc]],
    'server': NotRequired[Literal['home', 'away']],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreMatchPlayerStatsResponseDoc = TypedDict('ModelFlashscoreMatchPlayerStatsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchPlayerStatsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchPlayerStatsDataDoc = TypedDict('ModelFlashscoreMatchPlayerStatsDataDoc', {
    'groups': NotRequired[list[ModelFlashscorePlayerStatGroupDoc]],
    'match_id': NotRequired[str],
    'players': NotRequired[list[ModelFlashscorePlayerMatchStatsDoc]],
    'source_url': NotRequired[str],
    'stat_types': NotRequired[list[ModelFlashscorePlayerStatTypeDoc]],
    'teams': NotRequired[list[ModelFlashscorePlayerStatTeamDoc]],
}, total=False)

ModelFlashscorePlayerStatTeamDoc = TypedDict('ModelFlashscorePlayerStatTeamDoc', {
    'id': NotRequired[str],
    'name': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscorePlayerStatTypeDoc = TypedDict('ModelFlashscorePlayerStatTypeDoc', {
    'combined': NotRequired[ModelFlashscorePlayerStatCombinedDoc],
    'format': NotRequired[Literal['count', 'percentage', 'count_two_decimal_places']],
    'groups': NotRequired[list[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']]],
    'key': NotRequired[str],
    'label': NotRequired[str],
    'sentiment': NotRequired[Literal['positive', 'negative']],
}, total=False)

ModelFlashscorePlayerStatCombinedDoc = TypedDict('ModelFlashscorePlayerStatCombinedDoc', {
    'stats': NotRequired[list[str]],
    'template': NotRequired[str],
}, total=False)

ModelFlashscorePlayerMatchStatsDoc = TypedDict('ModelFlashscorePlayerMatchStatsDoc', {
    'highlights': NotRequired[list[str]],
    'id': NotRequired[str],
    'name': NotRequired[str],
    'position': NotRequired[str],
    'rating': NotRequired[float],
    'short_name': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
    'slug': NotRequired[str],
    'starter': NotRequired[bool],
    'stats': NotRequired[dict[str, ModelFlashscorePlayerStatValueDoc]],
    'team_id': NotRequired[str],
    'top_rated': NotRequired[bool],
}, total=False)

ModelFlashscorePlayerStatValueDoc = TypedDict('ModelFlashscorePlayerStatValueDoc', {
    'rank': NotRequired[int],
    'raw': NotRequired[float],
    'value': NotRequired[str],
}, total=False)

ModelFlashscorePlayerStatGroupDoc = TypedDict('ModelFlashscorePlayerStatGroupDoc', {
    'goalkeeper_only': NotRequired[bool],
    'key': NotRequired[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']],
    'label': NotRequired[str],
    'stats': NotRequired[list[str]],
}, total=False)

ModelFlashscoreMatchOddsResponseDoc = TypedDict('ModelFlashscoreMatchOddsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchOddsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchOddsDataDoc = TypedDict('ModelFlashscoreMatchOddsDataDoc', {
    'bookmakers': NotRequired[list[ModelFlashscoreOddsBookmakerDoc]],
    'geo': NotRequired[str],
    'markets': NotRequired[list[ModelFlashscoreOddsMarketDoc]],
    'match_id': NotRequired[str],
    'participants': NotRequired[list[ModelFlashscoreOddsParticipantDoc]],
    'source_url': NotRequired[str],
    'subdivision': NotRequired[str],
}, total=False)

ModelFlashscoreOddsParticipantDoc = TypedDict('ModelFlashscoreOddsParticipantDoc', {
    'id': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreOddsMarketDoc = TypedDict('ModelFlashscoreOddsMarketDoc', {
    'betting_type': NotRequired[Literal['HOME_DRAW_AWAY', 'HOME_AWAY', 'DRAW_NO_BET', 'DOUBLE_CHANCE', 'ASIAN_HANDICAP', 'EUROPEAN_HANDICAP', 'OVER_UNDER', 'BOTH_TEAMS_TO_SCORE', 'CORRECT_SCORE', 'HALF_FULL_TIME', 'ODD_OR_EVEN', 'TO_QUALIFY', 'NEXT_GOAL', 'TOP_POSITION_MERGED', 'TO_WIN_AND_TOP_POSITION', 'WIN_EACH_WAY']],
    'offers': NotRequired[list[ModelFlashscoreOddsOfferDoc]],
    'scope': NotRequired[Literal['FULL_TIME', 'FULL_TIME_OVER_TIME', 'FIRST_HALF', 'SECOND_HALF', 'FIRST_PERIOD', 'FIRST_QUARTER', 'FIRST_SET', 'SECOND_SET']],
}, total=False)

ModelFlashscoreOddsOfferDoc = TypedDict('ModelFlashscoreOddsOfferDoc', {
    'bookmaker_id': NotRequired[int],
    'outcomes': NotRequired[list[ModelFlashscoreOddsOutcomeDoc]],
}, total=False)

ModelFlashscoreOddsOutcomeDoc = TypedDict('ModelFlashscoreOddsOutcomeDoc', {
    'active': NotRequired[bool],
    'half_full_time': NotRequired[str],
    'handicap': NotRequired[float],
    'handicap_type': NotRequired[Literal['UNKNOWN', 'GOALS', 'GAMES', 'SETS', 'POINTS', 'FRAMES', 'LEGS', 'RUNS']],
    'odds': NotRequired[float],
    'opening_odds': NotRequired[float],
    'participant_id': NotRequired[str],
    'score': NotRequired[str],
    'selection': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreOddsBookmakerDoc = TypedDict('ModelFlashscoreOddsBookmakerDoc', {
    'id': NotRequired[int],
    'name': NotRequired[str],
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

ModelFlashscoreMatchMomentumResponseDoc = TypedDict('ModelFlashscoreMatchMomentumResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchMomentumDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchMomentumDataDoc = TypedDict('ModelFlashscoreMatchMomentumDataDoc', {
    'event_types': NotRequired[list[ModelFlashscoreMomentumEventTypeDoc]],
    'events': NotRequired[list[ModelFlashscoreMomentumEventDoc]],
    'match_id': NotRequired[str],
    'momentum': NotRequired[list[ModelFlashscoreMomentumFrameDoc]],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelFlashscoreMomentumTeamDoc]],
}, total=False)

ModelFlashscoreMomentumTeamDoc = TypedDict('ModelFlashscoreMomentumTeamDoc', {
    'code': NotRequired[str],
    'id': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreMomentumFrameDoc = TypedDict('ModelFlashscoreMomentumFrameDoc', {
    'added_time': NotRequired[int],
    'elapsed_minute': NotRequired[int],
    'elapsed_second': NotRequired[int],
    'minute': NotRequired[str],
    'period': NotRequired[Literal['first_half', 'second_half', 'extra_time', 'first_extra_time', 'second_extra_time', 'unknown']],
    'stage_id': NotRequired[int],
    'value': NotRequired[float],
}, total=False)

ModelFlashscoreMomentumEventDoc = TypedDict('ModelFlashscoreMomentumEventDoc', {
    'id': NotRequired[str],
    'label': NotRequired[str],
    'minute': NotRequired[str],
    'period': NotRequired[Literal['first_half', 'second_half', 'extra_time', 'first_extra_time', 'second_extra_time', 'unknown']],
    'player_id': NotRequired[str],
    'player_name': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
    'stage_id': NotRequired[int],
    'team_id': NotRequired[str],
    'type': NotRequired[Literal['yellow_red_card', 'red_card', 'goal', 'own_goal', 'penalty_goal']],
}, total=False)

ModelFlashscoreMomentumEventTypeDoc = TypedDict('ModelFlashscoreMomentumEventTypeDoc', {
    'label': NotRequired[str],
    'type': NotRequired[Literal['yellow_red_card', 'red_card', 'goal', 'own_goal', 'penalty_goal']],
}, total=False)

ModelFlashscoreMatchMissingPlayersResponseDoc = TypedDict('ModelFlashscoreMatchMissingPlayersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchMissingPlayersDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchMissingPlayersDataDoc = TypedDict('ModelFlashscoreMatchMissingPlayersDataDoc', {
    'match_id': NotRequired[str],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelFlashscoreMissingPlayersTeamDoc]],
}, total=False)

ModelFlashscoreMissingPlayersTeamDoc = TypedDict('ModelFlashscoreMissingPlayersTeamDoc', {
    'doubtful': NotRequired[list[ModelFlashscoreMissingPlayerDoc]],
    'missing': NotRequired[list[ModelFlashscoreMissingPlayerDoc]],
    'participant_id': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreMissingPlayerDoc = TypedDict('ModelFlashscoreMissingPlayerDoc', {
    'country': NotRequired[str],
    'list_name': NotRequired[str],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'reason': NotRequired[str],
    'slug': NotRequired[str],
}, total=False)

ModelFlashscoreMatchDartsResponseDoc = TypedDict('ModelFlashscoreMatchDartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchDartsDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchDartsDataDoc = TypedDict('ModelFlashscoreMatchDartsDataDoc', {
    'legs': NotRequired[list[ModelFlashscoreDartsLegDoc]],
    'match_id': NotRequired[str],
    'source_url': NotRequired[str],
    'statistics': NotRequired[list[ModelFlashscoreDartsStatisticDoc]],
    'statistics_url': NotRequired[str],
}, total=False)

ModelFlashscoreDartsStatisticDoc = TypedDict('ModelFlashscoreDartsStatisticDoc', {
    'away': NotRequired[str],
    'home': NotRequired[str],
    'id': NotRequired[str],
    'key': NotRequired[Literal['average_3_darts', '180_thrown', '140_plus_thrown', '100_plus_thrown', 'checkouts', 'checkouts_100_plus', 'highest_checkout']],
    'name': NotRequired[str],
}, total=False)

ModelFlashscoreDartsLegDoc = TypedDict('ModelFlashscoreDartsLegDoc', {
    'away_legs': NotRequired[int],
    'checkout': NotRequired[int],
    'home_legs': NotRequired[int],
    'number': NotRequired[int],
    'start_score': NotRequired[int],
    'starter': NotRequired[Literal['home', 'away']],
    'visits': NotRequired[list[ModelFlashscoreDartsVisitDoc]],
    'winner': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreDartsVisitDoc = TypedDict('ModelFlashscoreDartsVisitDoc', {
    'highlight': NotRequired[Literal['180', '140_plus']],
    'number': NotRequired[int],
    'remaining': NotRequired[int],
    'scored': NotRequired[int],
    'side': NotRequired[Literal['home', 'away']],
}, total=False)

ModelFlashscoreMatchBoxScoreResponseDoc = TypedDict('ModelFlashscoreMatchBoxScoreResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelFlashscoreMatchBoxScoreDataDoc],
    'msg': NotRequired[str],
}, total=False)

ModelFlashscoreMatchBoxScoreDataDoc = TypedDict('ModelFlashscoreMatchBoxScoreDataDoc', {
    'match_id': NotRequired[str],
    'source_url': NotRequired[str],
    'teams': NotRequired[list[ModelFlashscoreMatchBoxScoreTeamDoc]],
}, total=False)

ModelFlashscoreMatchBoxScoreTeamDoc = TypedDict('ModelFlashscoreMatchBoxScoreTeamDoc', {
    'name': NotRequired[str],
    'side': NotRequired[Literal['home', 'away']],
    'tables': NotRequired[list[ModelFlashscoreMatchBoxScoreTableDoc]],
}, total=False)

ModelFlashscoreMatchBoxScoreTableDoc = TypedDict('ModelFlashscoreMatchBoxScoreTableDoc', {
    'columns': NotRequired[list[ModelFlashscoreMatchBoxScoreColumnDoc]],
    'player_label': NotRequired[str],
    'players': NotRequired[list[ModelFlashscoreMatchBoxScorePlayerDoc]],
    'type': NotRequired[Literal['player', 'goalkeeper', 'pitcher']],
}, total=False)

ModelFlashscoreMatchBoxScorePlayerDoc = TypedDict('ModelFlashscoreMatchBoxScorePlayerDoc', {
    'country': NotRequired[str],
    'name': NotRequired[str],
    'player_id': NotRequired[str],
    'slug': NotRequired[str],
    'stats': NotRequired[dict[str, str]],
    'status': NotRequired[str],
}, total=False)

ModelFlashscoreMatchBoxScoreColumnDoc = TypedDict('ModelFlashscoreMatchBoxScoreColumnDoc', {
    'format': NotRequired[Literal['num', 'time', 'fg']],
    'key': NotRequired[str],
    'label': NotRequired[str],
}, total=False)

ModelFlashscoreEntityNewsResponse = TypedDict('ModelFlashscoreEntityNewsResponse', {
    'article_count': NotRequired[int],
    'entity': NotRequired[ModelFlashscoreEntityNewsTag],
    'id': NotRequired[str],
    'sections': NotRequired[list[ModelFlashscoreEntityNewsSection]],
    'source_url': NotRequired[str],
    'title': NotRequired[str],
    'type': NotRequired[Literal['team', 'player', 'tournament', 'sport']],
}, total=False)

ModelFlashscoreEntityNewsSection = TypedDict('ModelFlashscoreEntityNewsSection', {
    'article_count': NotRequired[int],
    'article_ids': NotRequired[list[str]],
    'section_type': NotRequired[Literal['MOST_RECENT', 'TOPPED']],
    'title': NotRequired[str],
}, total=False)

ModelFlashscoreEntityNewsTag = TypedDict('ModelFlashscoreEntityNewsTag', {
    'entity_id': NotRequired[str],
    'entity_type': NotRequired[Literal['PARTICIPANT', 'TOURNAMENT_TEMPLATE', 'SPORT']],
    'label': NotRequired[str],
    'slug': NotRequired[str],
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
    'country': NotRequired[str],
    'date': NotRequired[str],
    'end_time': NotRequired[str],
    'month': NotRequired[str],
    'name': NotRequired[str],
    'path': NotRequired[str],
    'start_time': NotRequired[str],
    'winner': NotRequired[str],
    'winner_path': NotRequired[str],
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
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreEntityNewsResponse = Any
FlashscoreEntityNewsParams = TypedDict('FlashscoreEntityNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'type': Required[Literal['team', 'player', 'tournament', 'sport']],
    'id': Required[str],
}, total=False)

FlashscoreMatchBoxScoreResponse = ModelFlashscoreMatchBoxScoreResponseDoc
FlashscoreMatchBoxScoreParams = TypedDict('FlashscoreMatchBoxScoreParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchDartsResponse = ModelFlashscoreMatchDartsResponseDoc
FlashscoreMatchDartsParams = TypedDict('FlashscoreMatchDartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
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

FlashscoreMatchMissingPlayersResponse = ModelFlashscoreMatchMissingPlayersResponseDoc
FlashscoreMatchMissingPlayersParams = TypedDict('FlashscoreMatchMissingPlayersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMomentumResponse = ModelFlashscoreMatchMomentumResponseDoc
FlashscoreMatchMomentumParams = TypedDict('FlashscoreMatchMomentumParams', {
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

FlashscoreMatchOddsResponse = ModelFlashscoreMatchOddsResponseDoc
FlashscoreMatchOddsParams = TypedDict('FlashscoreMatchOddsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
    'betting_type': NotRequired[Literal['HOME_DRAW_AWAY', 'HOME_AWAY', 'DRAW_NO_BET', 'DOUBLE_CHANCE', 'ASIAN_HANDICAP', 'EUROPEAN_HANDICAP', 'OVER_UNDER', 'BOTH_TEAMS_TO_SCORE', 'CORRECT_SCORE', 'HALF_FULL_TIME', 'ODD_OR_EVEN', 'TO_QUALIFY', 'NEXT_GOAL', 'TOP_POSITION_MERGED', 'TO_WIN_AND_TOP_POSITION', 'WIN_EACH_WAY']],
    'scope': NotRequired[Literal['FULL_TIME', 'FULL_TIME_OVER_TIME', 'FIRST_HALF', 'SECOND_HALF', 'FIRST_PERIOD', 'FIRST_QUARTER', 'FIRST_SET', 'SECOND_SET']],
}, total=False)

FlashscoreMatchPlayerStatsResponse = ModelFlashscoreMatchPlayerStatsResponseDoc
FlashscoreMatchPlayerStatsParams = TypedDict('FlashscoreMatchPlayerStatsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'player_id': NotRequired[str],
    'group': NotRequired[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']],
}, total=False)

FlashscoreMatchPointByPointResponse = ModelFlashscoreMatchPointByPointResponseDoc
FlashscoreMatchPointByPointParams = TypedDict('FlashscoreMatchPointByPointParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPredictedLineupsResponse = ModelFlashscoreMatchPredictedLineupsResponseDoc
FlashscoreMatchPredictedLineupsParams = TypedDict('FlashscoreMatchPredictedLineupsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreMatchReportResponse = ModelFlashscoreMatchReportResponseDoc
FlashscoreMatchReportParams = TypedDict('FlashscoreMatchReportParams', {
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

FlashscoreMatchTvResponse = ModelFlashscoreMatchTvresponseDoc
FlashscoreMatchTvParams = TypedDict('FlashscoreMatchTvParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
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

FlashscoreNewsArticleBodyResponse = Any
FlashscoreNewsArticleBodyParams = TypedDict('FlashscoreNewsArticleBodyParams', {
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

FlashscoreNewsMostReadResponse = Any
FlashscoreNewsMostReadParams = TypedDict('FlashscoreNewsMostReadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreOddsGeosResponse = ModelFlashscoreOddsGeosResponseDoc
FlashscoreOddsGeosParams = TypedDict('FlashscoreOddsGeosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscorePlayerResponse = Any
FlashscorePlayerParams = TypedDict('FlashscorePlayerParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerFixturesResponse = Any
FlashscorePlayerFixturesParams = TypedDict('FlashscorePlayerFixturesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerInjuriesResponse = Any
FlashscorePlayerInjuriesParams = TypedDict('FlashscorePlayerInjuriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerMatchLogResponse = Any
FlashscorePlayerMatchLogParams = TypedDict('FlashscorePlayerMatchLogParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerNewsResponse = Any
FlashscorePlayerNewsParams = TypedDict('FlashscorePlayerNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscorePlayerResultsResponse = Any
FlashscorePlayerResultsParams = TypedDict('FlashscorePlayerResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerTransfersResponse = Any
FlashscorePlayerTransfersParams = TypedDict('FlashscorePlayerTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'slug': NotRequired[str],
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
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
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

FlashscoreTeamResponse = Any
FlashscoreTeamParams = TypedDict('FlashscoreTeamParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreTeamFixturesResponse = Any
FlashscoreTeamFixturesParams = TypedDict('FlashscoreTeamFixturesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamNewsResponse = Any
FlashscoreTeamNewsParams = TypedDict('FlashscoreTeamNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
}, total=False)

FlashscoreTeamOutrightOddsResponse = Any
FlashscoreTeamOutrightOddsParams = TypedDict('FlashscoreTeamOutrightOddsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTeamResultsResponse = Any
FlashscoreTeamResultsParams = TypedDict('FlashscoreTeamResultsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamSquadResponse = Any
FlashscoreTeamSquadParams = TypedDict('FlashscoreTeamSquadParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'slug': NotRequired[str],
    'scope': NotRequired[str],
}, total=False)

FlashscoreTeamTransfersResponse = Any
FlashscoreTeamTransfersParams = TypedDict('FlashscoreTeamTransfersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'id': Required[str],
    'type': NotRequired[Literal['all', 'arrivals', 'departures']],
    'page': NotRequired[int],
}, total=False)

FlashscoreTopSearchResponse = ModelFlashscoreTopSearchResponseDoc
FlashscoreTopSearchParams = TypedDict('FlashscoreTopSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

FlashscoreTournamentArchiveSeasonsResponse = Any
FlashscoreTournamentArchiveSeasonsParams = TypedDict('FlashscoreTournamentArchiveSeasonsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'stage_id': Required[str],
}, total=False)

FlashscoreTournamentEventsResponse = ModelFlashscoreTournamentEventsResponseDoc
FlashscoreTournamentEventsParams = TypedDict('FlashscoreTournamentEventsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentOutrightOddsResponse = Any
FlashscoreTournamentOutrightOddsParams = TypedDict('FlashscoreTournamentOutrightOddsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'tournament_id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
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
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarDefaultParams]) -> FlashscoreCalendarResponse: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesDefaultParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsDefaultParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsStreamParams]) -> BinaryIO: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsTextResponseParams]) -> str: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsDefaultParams]) -> FlashscoreEntityNewsResponse: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreTextResponseParams]) -> str: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreDefaultParams]) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsStreamParams]) -> BinaryIO: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsTextResponseParams]) -> str: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsDefaultParams]) -> FlashscoreMatchDartsResponse: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hDefaultParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsDefaultParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoDefaultParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsDefaultParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersTextResponseParams]) -> str: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersDefaultParams]) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumStreamParams]) -> BinaryIO: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumTextResponseParams]) -> str: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumDefaultParams]) -> FlashscoreMatchMomentumResponse: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsDefaultParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsStreamParams]) -> BinaryIO: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsTextResponseParams]) -> str: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsDefaultParams]) -> FlashscoreMatchOddsResponse: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsDefaultParams]) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointTextResponseParams]) -> str: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointDefaultParams]) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsTextResponseParams]) -> str: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsDefaultParams]) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportStreamParams]) -> BinaryIO: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportTextResponseParams]) -> str: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportDefaultParams]) -> FlashscoreMatchReportResponse: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsDefaultParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsDefaultParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvStreamParams]) -> BinaryIO: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvTextResponseParams]) -> str: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvDefaultParams]) -> FlashscoreMatchTvResponse: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationDefaultParams]) -> FlashscoreNavigationResponse: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsDefaultParams]) -> FlashscoreNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleDefaultParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyStreamParams]) -> BinaryIO: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyTextResponseParams]) -> str: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyDefaultParams]) -> FlashscoreNewsArticleBodyResponse: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesDefaultParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadStreamParams]) -> BinaryIO: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadTextResponseParams]) -> str: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadDefaultParams]) -> FlashscoreNewsMostReadResponse: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosStreamParams]) -> BinaryIO: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosTextResponseParams]) -> str: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosDefaultParams]) -> FlashscoreOddsGeosResponse: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerDefaultParams]) -> FlashscorePlayerResponse: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesTextResponseParams]) -> str: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesDefaultParams]) -> FlashscorePlayerFixturesResponse: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesStreamParams]) -> BinaryIO: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesTextResponseParams]) -> str: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesDefaultParams]) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogStreamParams]) -> BinaryIO: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogTextResponseParams]) -> str: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogDefaultParams]) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsTextResponseParams]) -> str: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsDefaultParams]) -> FlashscorePlayerNewsResponse: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsStreamParams]) -> BinaryIO: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsTextResponseParams]) -> str: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsDefaultParams]) -> FlashscorePlayerResultsResponse: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersDefaultParams]) -> FlashscorePlayerTransfersResponse: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesDefaultParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsDefaultParams]) -> FlashscoreRankingsResponse: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresDefaultParams]) -> FlashscoreScoresResponse: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchDefaultParams]) -> FlashscoreSearchResponse: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsDefaultParams]) -> FlashscoreSportsResponse: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamDefaultParams]) -> FlashscoreTeamResponse: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesTextResponseParams]) -> str: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesDefaultParams]) -> FlashscoreTeamFixturesResponse: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsTextResponseParams]) -> str: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsDefaultParams]) -> FlashscoreTeamNewsResponse: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsTextResponseParams]) -> str: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsDefaultParams]) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsTextResponseParams]) -> str: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsDefaultParams]) -> FlashscoreTeamResultsResponse: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadTextResponseParams]) -> str: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadDefaultParams]) -> FlashscoreTeamSquadResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersDefaultParams]) -> FlashscoreTeamTransfersResponse: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchDefaultParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsDefaultParams]) -> FlashscoreTournamentArchiveSeasonsResponse: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsDefaultParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsTextResponseParams]) -> str: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsDefaultParams]) -> FlashscoreTournamentOutrightOddsResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsDefaultParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsDefaultParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsDefaultParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

OperationId = Literal[
    'flashscore-calendar',
    'flashscore-calendar-categories',
    'flashscore-competitions',
    'flashscore-entity-news',
    'flashscore-match-box-score',
    'flashscore-match-darts',
    'flashscore-match-h2h',
    'flashscore-match-highlights',
    'flashscore-match-info',
    'flashscore-match-lineups',
    'flashscore-match-missing-players',
    'flashscore-match-momentum',
    'flashscore-match-news',
    'flashscore-match-odds',
    'flashscore-match-player-stats',
    'flashscore-match-point-by-point',
    'flashscore-match-predicted-lineups',
    'flashscore-match-report',
    'flashscore-match-standings',
    'flashscore-match-stats',
    'flashscore-match-tv',
    'flashscore-navigation',
    'flashscore-news',
    'flashscore-news-article',
    'flashscore-news-article-body',
    'flashscore-news-categories',
    'flashscore-news-most-read',
    'flashscore-odds-geos',
    'flashscore-player',
    'flashscore-player-fixtures',
    'flashscore-player-injuries',
    'flashscore-player-match-log',
    'flashscore-player-news',
    'flashscore-player-results',
    'flashscore-player-transfers',
    'flashscore-ranking-categories',
    'flashscore-rankings',
    'flashscore-scores',
    'flashscore-search',
    'flashscore-sports',
    'flashscore-team',
    'flashscore-team-fixtures',
    'flashscore-team-news',
    'flashscore-team-outright-odds',
    'flashscore-team-results',
    'flashscore-team-squad',
    'flashscore-team-transfers',
    'flashscore-top-search',
    'flashscore-tournament-archive-seasons',
    'flashscore-tournament-events',
    'flashscore-tournament-outright-odds',
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
        operation_id: Literal['flashscore-entity-news'],
        params: FlashscoreEntityNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreEntityNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-box-score'],
        params: FlashscoreMatchBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-darts'],
        params: FlashscoreMatchDartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchDartsResponse: ...
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
        operation_id: Literal['flashscore-match-missing-players'],
        params: FlashscoreMatchMissingPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-momentum'],
        params: FlashscoreMatchMomentumParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchMomentumResponse: ...
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
        operation_id: Literal['flashscore-match-odds'],
        params: FlashscoreMatchOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchOddsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-player-stats'],
        params: FlashscoreMatchPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-point-by-point'],
        params: FlashscoreMatchPointByPointParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-predicted-lineups'],
        params: FlashscoreMatchPredictedLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-match-report'],
        params: FlashscoreMatchReportParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchReportResponse: ...
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
        operation_id: Literal['flashscore-match-tv'],
        params: FlashscoreMatchTvParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchTvResponse: ...
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
        operation_id: Literal['flashscore-news-article-body'],
        params: FlashscoreNewsArticleBodyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsArticleBodyResponse: ...
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
        operation_id: Literal['flashscore-news-most-read'],
        params: FlashscoreNewsMostReadParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsMostReadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-odds-geos'],
        params: FlashscoreOddsGeosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreOddsGeosResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player'],
        params: FlashscorePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-fixtures'],
        params: FlashscorePlayerFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerFixturesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-injuries'],
        params: FlashscorePlayerInjuriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-match-log'],
        params: FlashscorePlayerMatchLogParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-news'],
        params: FlashscorePlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-results'],
        params: FlashscorePlayerResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-player-transfers'],
        params: FlashscorePlayerTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerTransfersResponse: ...
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
        operation_id: Literal['flashscore-team'],
        params: FlashscoreTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-fixtures'],
        params: FlashscoreTeamFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamFixturesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-news'],
        params: FlashscoreTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-outright-odds'],
        params: FlashscoreTeamOutrightOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-results'],
        params: FlashscoreTeamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamResultsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-squad'],
        params: FlashscoreTeamSquadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamSquadResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['flashscore-team-transfers'],
        params: FlashscoreTeamTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamTransfersResponse: ...
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
        operation_id: Literal['flashscore-tournament-archive-seasons'],
        params: FlashscoreTournamentArchiveSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentArchiveSeasonsResponse: ...
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
        operation_id: Literal['flashscore-tournament-outright-odds'],
        params: FlashscoreTournamentOutrightOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentOutrightOddsResponse: ...
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
        operation_id: Literal['flashscore-entity-news'],
        params: FlashscoreEntityNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreEntityNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-box-score'],
        params: FlashscoreMatchBoxScoreParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-darts'],
        params: FlashscoreMatchDartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchDartsResponse: ...
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
        operation_id: Literal['flashscore-match-missing-players'],
        params: FlashscoreMatchMissingPlayersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-momentum'],
        params: FlashscoreMatchMomentumParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchMomentumResponse: ...
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
        operation_id: Literal['flashscore-match-odds'],
        params: FlashscoreMatchOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchOddsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-player-stats'],
        params: FlashscoreMatchPlayerStatsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-point-by-point'],
        params: FlashscoreMatchPointByPointParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-predicted-lineups'],
        params: FlashscoreMatchPredictedLineupsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-match-report'],
        params: FlashscoreMatchReportParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchReportResponse: ...
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
        operation_id: Literal['flashscore-match-tv'],
        params: FlashscoreMatchTvParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreMatchTvResponse: ...
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
        operation_id: Literal['flashscore-news-article-body'],
        params: FlashscoreNewsArticleBodyParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsArticleBodyResponse: ...
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
        operation_id: Literal['flashscore-news-most-read'],
        params: FlashscoreNewsMostReadParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreNewsMostReadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-odds-geos'],
        params: FlashscoreOddsGeosParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreOddsGeosResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player'],
        params: FlashscorePlayerParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-fixtures'],
        params: FlashscorePlayerFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerFixturesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-injuries'],
        params: FlashscorePlayerInjuriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-match-log'],
        params: FlashscorePlayerMatchLogParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-news'],
        params: FlashscorePlayerNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-results'],
        params: FlashscorePlayerResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-player-transfers'],
        params: FlashscorePlayerTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscorePlayerTransfersResponse: ...
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
        operation_id: Literal['flashscore-team'],
        params: FlashscoreTeamParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-fixtures'],
        params: FlashscoreTeamFixturesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamFixturesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-news'],
        params: FlashscoreTeamNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-outright-odds'],
        params: FlashscoreTeamOutrightOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-results'],
        params: FlashscoreTeamResultsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamResultsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-squad'],
        params: FlashscoreTeamSquadParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamSquadResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['flashscore-team-transfers'],
        params: FlashscoreTeamTransfersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTeamTransfersResponse: ...
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
        operation_id: Literal['flashscore-tournament-archive-seasons'],
        params: FlashscoreTournamentArchiveSeasonsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentArchiveSeasonsResponse: ...
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
        operation_id: Literal['flashscore-tournament-outright-odds'],
        params: FlashscoreTournamentOutrightOddsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> FlashscoreTournamentOutrightOddsResponse: ...
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
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    def calendar(self, **params: Unpack[FlashscoreCalendarDefaultParams]) -> FlashscoreCalendarResponse: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesDefaultParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    def competitions(self, **params: Unpack[FlashscoreCompetitionsDefaultParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsStreamParams]) -> BinaryIO: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsTextResponseParams]) -> str: ...
    @overload
    def entity_news(self, **params: Unpack[FlashscoreEntityNewsDefaultParams]) -> FlashscoreEntityNewsResponse: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreTextResponseParams]) -> str: ...
    @overload
    def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreDefaultParams]) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsStreamParams]) -> BinaryIO: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsTextResponseParams]) -> str: ...
    @overload
    def match_darts(self, **params: Unpack[FlashscoreMatchDartsDefaultParams]) -> FlashscoreMatchDartsResponse: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    def match_h2h(self, **params: Unpack[FlashscoreMatchH2hDefaultParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsDefaultParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    def match_info(self, **params: Unpack[FlashscoreMatchInfoDefaultParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsDefaultParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersTextResponseParams]) -> str: ...
    @overload
    def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersDefaultParams]) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumStreamParams]) -> BinaryIO: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumTextResponseParams]) -> str: ...
    @overload
    def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumDefaultParams]) -> FlashscoreMatchMomentumResponse: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    def match_news(self, **params: Unpack[FlashscoreMatchNewsDefaultParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsStreamParams]) -> BinaryIO: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsTextResponseParams]) -> str: ...
    @overload
    def match_odds(self, **params: Unpack[FlashscoreMatchOddsDefaultParams]) -> FlashscoreMatchOddsResponse: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsTextResponseParams]) -> str: ...
    @overload
    def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsDefaultParams]) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointTextResponseParams]) -> str: ...
    @overload
    def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointDefaultParams]) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsStreamParams]) -> BinaryIO: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsTextResponseParams]) -> str: ...
    @overload
    def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsDefaultParams]) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportStreamParams]) -> BinaryIO: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportTextResponseParams]) -> str: ...
    @overload
    def match_report(self, **params: Unpack[FlashscoreMatchReportDefaultParams]) -> FlashscoreMatchReportResponse: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    def match_standings(self, **params: Unpack[FlashscoreMatchStandingsDefaultParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    def match_stats(self, **params: Unpack[FlashscoreMatchStatsDefaultParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvStreamParams]) -> BinaryIO: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvTextResponseParams]) -> str: ...
    @overload
    def match_tv(self, **params: Unpack[FlashscoreMatchTvDefaultParams]) -> FlashscoreMatchTvResponse: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    def navigation(self, **params: Unpack[FlashscoreNavigationDefaultParams]) -> FlashscoreNavigationResponse: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[FlashscoreNewsDefaultParams]) -> FlashscoreNewsResponse: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    def news_article(self, **params: Unpack[FlashscoreNewsArticleDefaultParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyStreamParams]) -> BinaryIO: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyTextResponseParams]) -> str: ...
    @overload
    def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyDefaultParams]) -> FlashscoreNewsArticleBodyResponse: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesDefaultParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadStreamParams]) -> BinaryIO: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadTextResponseParams]) -> str: ...
    @overload
    def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadDefaultParams]) -> FlashscoreNewsMostReadResponse: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosStreamParams]) -> BinaryIO: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosTextResponseParams]) -> str: ...
    @overload
    def odds_geos(self, **params: Unpack[FlashscoreOddsGeosDefaultParams]) -> FlashscoreOddsGeosResponse: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerTextResponseParams]) -> str: ...
    @overload
    def player(self, **params: Unpack[FlashscorePlayerDefaultParams]) -> FlashscorePlayerResponse: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesTextResponseParams]) -> str: ...
    @overload
    def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesDefaultParams]) -> FlashscorePlayerFixturesResponse: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesStreamParams]) -> BinaryIO: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesTextResponseParams]) -> str: ...
    @overload
    def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesDefaultParams]) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogStreamParams]) -> BinaryIO: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogTextResponseParams]) -> str: ...
    @overload
    def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogDefaultParams]) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsTextResponseParams]) -> str: ...
    @overload
    def player_news(self, **params: Unpack[FlashscorePlayerNewsDefaultParams]) -> FlashscorePlayerNewsResponse: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsStreamParams]) -> BinaryIO: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsTextResponseParams]) -> str: ...
    @overload
    def player_results(self, **params: Unpack[FlashscorePlayerResultsDefaultParams]) -> FlashscorePlayerResultsResponse: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersDefaultParams]) -> FlashscorePlayerTransfersResponse: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesDefaultParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    def rankings(self, **params: Unpack[FlashscoreRankingsDefaultParams]) -> FlashscoreRankingsResponse: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    def scores(self, **params: Unpack[FlashscoreScoresDefaultParams]) -> FlashscoreScoresResponse: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[FlashscoreSearchDefaultParams]) -> FlashscoreSearchResponse: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    def sports(self, **params: Unpack[FlashscoreSportsDefaultParams]) -> FlashscoreSportsResponse: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamTextResponseParams]) -> str: ...
    @overload
    def team(self, **params: Unpack[FlashscoreTeamDefaultParams]) -> FlashscoreTeamResponse: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesTextResponseParams]) -> str: ...
    @overload
    def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesDefaultParams]) -> FlashscoreTeamFixturesResponse: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsTextResponseParams]) -> str: ...
    @overload
    def team_news(self, **params: Unpack[FlashscoreTeamNewsDefaultParams]) -> FlashscoreTeamNewsResponse: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsTextResponseParams]) -> str: ...
    @overload
    def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsDefaultParams]) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsTextResponseParams]) -> str: ...
    @overload
    def team_results(self, **params: Unpack[FlashscoreTeamResultsDefaultParams]) -> FlashscoreTeamResultsResponse: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadTextResponseParams]) -> str: ...
    @overload
    def team_squad(self, **params: Unpack[FlashscoreTeamSquadDefaultParams]) -> FlashscoreTeamSquadResponse: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersDefaultParams]) -> FlashscoreTeamTransfersResponse: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    def top_search(self, **params: Unpack[FlashscoreTopSearchDefaultParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsDefaultParams]) -> FlashscoreTournamentArchiveSeasonsResponse: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsDefaultParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsTextResponseParams]) -> str: ...
    @overload
    def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsDefaultParams]) -> FlashscoreTournamentOutrightOddsResponse: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsDefaultParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsDefaultParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsDefaultParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

class AsyncFlashscoreClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncFlashscoreClient: ...
    flashscore: _AsyncFlashscoreGroup
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarDefaultParams]) -> FlashscoreCalendarResponse: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesDefaultParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsDefaultParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsTextResponseParams]) -> str: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsDefaultParams]) -> FlashscoreEntityNewsResponse: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreDefaultParams]) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsTextResponseParams]) -> str: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsDefaultParams]) -> FlashscoreMatchDartsResponse: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hDefaultParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsDefaultParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoDefaultParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsDefaultParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersTextResponseParams]) -> str: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersDefaultParams]) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumStreamParams]) -> BinaryIO: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumTextResponseParams]) -> str: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumDefaultParams]) -> FlashscoreMatchMomentumResponse: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsDefaultParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsTextResponseParams]) -> str: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsDefaultParams]) -> FlashscoreMatchOddsResponse: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsDefaultParams]) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointTextResponseParams]) -> str: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointDefaultParams]) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsDefaultParams]) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportStreamParams]) -> BinaryIO: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportTextResponseParams]) -> str: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportDefaultParams]) -> FlashscoreMatchReportResponse: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsDefaultParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsDefaultParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvStreamParams]) -> BinaryIO: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvTextResponseParams]) -> str: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvDefaultParams]) -> FlashscoreMatchTvResponse: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationDefaultParams]) -> FlashscoreNavigationResponse: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsDefaultParams]) -> FlashscoreNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleDefaultParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyTextResponseParams]) -> str: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyDefaultParams]) -> FlashscoreNewsArticleBodyResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesDefaultParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadStreamParams]) -> BinaryIO: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadTextResponseParams]) -> str: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadDefaultParams]) -> FlashscoreNewsMostReadResponse: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosTextResponseParams]) -> str: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosDefaultParams]) -> FlashscoreOddsGeosResponse: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerDefaultParams]) -> FlashscorePlayerResponse: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesTextResponseParams]) -> str: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesDefaultParams]) -> FlashscorePlayerFixturesResponse: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesTextResponseParams]) -> str: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesDefaultParams]) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogTextResponseParams]) -> str: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogDefaultParams]) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsDefaultParams]) -> FlashscorePlayerNewsResponse: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsTextResponseParams]) -> str: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsDefaultParams]) -> FlashscorePlayerResultsResponse: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersDefaultParams]) -> FlashscorePlayerTransfersResponse: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesDefaultParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsDefaultParams]) -> FlashscoreRankingsResponse: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresDefaultParams]) -> FlashscoreScoresResponse: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchDefaultParams]) -> FlashscoreSearchResponse: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsDefaultParams]) -> FlashscoreSportsResponse: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamDefaultParams]) -> FlashscoreTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesDefaultParams]) -> FlashscoreTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsDefaultParams]) -> FlashscoreTeamNewsResponse: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsTextResponseParams]) -> str: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsDefaultParams]) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsTextResponseParams]) -> str: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsDefaultParams]) -> FlashscoreTeamResultsResponse: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadTextResponseParams]) -> str: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadDefaultParams]) -> FlashscoreTeamSquadResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersDefaultParams]) -> FlashscoreTeamTransfersResponse: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchDefaultParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsDefaultParams]) -> FlashscoreTournamentArchiveSeasonsResponse: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsDefaultParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsTextResponseParams]) -> str: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsDefaultParams]) -> FlashscoreTournamentOutrightOddsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsDefaultParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsDefaultParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsDefaultParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

class _AsyncFlashscoreGroup:
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarTextResponseParams]) -> str: ...
    @overload
    async def calendar(self, **params: Unpack[FlashscoreCalendarDefaultParams]) -> FlashscoreCalendarResponse: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesTextResponseParams]) -> str: ...
    @overload
    async def calendar_categories(self, **params: Unpack[FlashscoreCalendarCategoriesDefaultParams]) -> FlashscoreCalendarCategoriesResponse: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsStreamParams]) -> BinaryIO: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsTextResponseParams]) -> str: ...
    @overload
    async def competitions(self, **params: Unpack[FlashscoreCompetitionsDefaultParams]) -> FlashscoreCompetitionsResponse: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsTextResponseParams]) -> str: ...
    @overload
    async def entity_news(self, **params: Unpack[FlashscoreEntityNewsDefaultParams]) -> FlashscoreEntityNewsResponse: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreStreamParams]) -> BinaryIO: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreTextResponseParams]) -> str: ...
    @overload
    async def match_box_score(self, **params: Unpack[FlashscoreMatchBoxScoreDefaultParams]) -> FlashscoreMatchBoxScoreResponse: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsTextResponseParams]) -> str: ...
    @overload
    async def match_darts(self, **params: Unpack[FlashscoreMatchDartsDefaultParams]) -> FlashscoreMatchDartsResponse: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hStreamParams]) -> BinaryIO: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hTextResponseParams]) -> str: ...
    @overload
    async def match_h2h(self, **params: Unpack[FlashscoreMatchH2hDefaultParams]) -> FlashscoreMatchH2hResponse: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsTextResponseParams]) -> str: ...
    @overload
    async def match_highlights(self, **params: Unpack[FlashscoreMatchHighlightsDefaultParams]) -> FlashscoreMatchHighlightsResponse: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoStreamParams]) -> BinaryIO: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoTextResponseParams]) -> str: ...
    @overload
    async def match_info(self, **params: Unpack[FlashscoreMatchInfoDefaultParams]) -> FlashscoreMatchInfoResponse: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_lineups(self, **params: Unpack[FlashscoreMatchLineupsDefaultParams]) -> FlashscoreMatchLineupsResponse: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersStreamParams]) -> BinaryIO: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersTextResponseParams]) -> str: ...
    @overload
    async def match_missing_players(self, **params: Unpack[FlashscoreMatchMissingPlayersDefaultParams]) -> FlashscoreMatchMissingPlayersResponse: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumStreamParams]) -> BinaryIO: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumTextResponseParams]) -> str: ...
    @overload
    async def match_momentum(self, **params: Unpack[FlashscoreMatchMomentumDefaultParams]) -> FlashscoreMatchMomentumResponse: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsTextResponseParams]) -> str: ...
    @overload
    async def match_news(self, **params: Unpack[FlashscoreMatchNewsDefaultParams]) -> FlashscoreMatchNewsResponse: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsTextResponseParams]) -> str: ...
    @overload
    async def match_odds(self, **params: Unpack[FlashscoreMatchOddsDefaultParams]) -> FlashscoreMatchOddsResponse: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsTextResponseParams]) -> str: ...
    @overload
    async def match_player_stats(self, **params: Unpack[FlashscoreMatchPlayerStatsDefaultParams]) -> FlashscoreMatchPlayerStatsResponse: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointStreamParams]) -> BinaryIO: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointTextResponseParams]) -> str: ...
    @overload
    async def match_point_by_point(self, **params: Unpack[FlashscoreMatchPointByPointDefaultParams]) -> FlashscoreMatchPointByPointResponse: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsTextResponseParams]) -> str: ...
    @overload
    async def match_predicted_lineups(self, **params: Unpack[FlashscoreMatchPredictedLineupsDefaultParams]) -> FlashscoreMatchPredictedLineupsResponse: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportStreamParams]) -> BinaryIO: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportTextResponseParams]) -> str: ...
    @overload
    async def match_report(self, **params: Unpack[FlashscoreMatchReportDefaultParams]) -> FlashscoreMatchReportResponse: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsTextResponseParams]) -> str: ...
    @overload
    async def match_standings(self, **params: Unpack[FlashscoreMatchStandingsDefaultParams]) -> FlashscoreMatchStandingsResponse: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsStreamParams]) -> BinaryIO: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsTextResponseParams]) -> str: ...
    @overload
    async def match_stats(self, **params: Unpack[FlashscoreMatchStatsDefaultParams]) -> FlashscoreMatchStatsResponse: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvStreamParams]) -> BinaryIO: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvTextResponseParams]) -> str: ...
    @overload
    async def match_tv(self, **params: Unpack[FlashscoreMatchTvDefaultParams]) -> FlashscoreMatchTvResponse: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationStreamParams]) -> BinaryIO: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationTextResponseParams]) -> str: ...
    @overload
    async def navigation(self, **params: Unpack[FlashscoreNavigationDefaultParams]) -> FlashscoreNavigationResponse: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[FlashscoreNewsDefaultParams]) -> FlashscoreNewsResponse: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleTextResponseParams]) -> str: ...
    @overload
    async def news_article(self, **params: Unpack[FlashscoreNewsArticleDefaultParams]) -> FlashscoreNewsArticleResponse: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyStreamParams]) -> BinaryIO: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyTextResponseParams]) -> str: ...
    @overload
    async def news_article_body(self, **params: Unpack[FlashscoreNewsArticleBodyDefaultParams]) -> FlashscoreNewsArticleBodyResponse: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesTextResponseParams]) -> str: ...
    @overload
    async def news_categories(self, **params: Unpack[FlashscoreNewsCategoriesDefaultParams]) -> FlashscoreNewsCategoriesResponse: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadStreamParams]) -> BinaryIO: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadTextResponseParams]) -> str: ...
    @overload
    async def news_most_read(self, **params: Unpack[FlashscoreNewsMostReadDefaultParams]) -> FlashscoreNewsMostReadResponse: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosStreamParams]) -> BinaryIO: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosTextResponseParams]) -> str: ...
    @overload
    async def odds_geos(self, **params: Unpack[FlashscoreOddsGeosDefaultParams]) -> FlashscoreOddsGeosResponse: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerStreamParams]) -> BinaryIO: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerTextResponseParams]) -> str: ...
    @overload
    async def player(self, **params: Unpack[FlashscorePlayerDefaultParams]) -> FlashscorePlayerResponse: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesTextResponseParams]) -> str: ...
    @overload
    async def player_fixtures(self, **params: Unpack[FlashscorePlayerFixturesDefaultParams]) -> FlashscorePlayerFixturesResponse: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesStreamParams]) -> BinaryIO: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesTextResponseParams]) -> str: ...
    @overload
    async def player_injuries(self, **params: Unpack[FlashscorePlayerInjuriesDefaultParams]) -> FlashscorePlayerInjuriesResponse: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogStreamParams]) -> BinaryIO: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogTextResponseParams]) -> str: ...
    @overload
    async def player_match_log(self, **params: Unpack[FlashscorePlayerMatchLogDefaultParams]) -> FlashscorePlayerMatchLogResponse: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsTextResponseParams]) -> str: ...
    @overload
    async def player_news(self, **params: Unpack[FlashscorePlayerNewsDefaultParams]) -> FlashscorePlayerNewsResponse: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsTextResponseParams]) -> str: ...
    @overload
    async def player_results(self, **params: Unpack[FlashscorePlayerResultsDefaultParams]) -> FlashscorePlayerResultsResponse: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersTextResponseParams]) -> str: ...
    @overload
    async def player_transfers(self, **params: Unpack[FlashscorePlayerTransfersDefaultParams]) -> FlashscorePlayerTransfersResponse: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesTextResponseParams]) -> str: ...
    @overload
    async def ranking_categories(self, **params: Unpack[FlashscoreRankingCategoriesDefaultParams]) -> FlashscoreRankingCategoriesResponse: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsStreamParams]) -> BinaryIO: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsTextResponseParams]) -> str: ...
    @overload
    async def rankings(self, **params: Unpack[FlashscoreRankingsDefaultParams]) -> FlashscoreRankingsResponse: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresStreamParams]) -> BinaryIO: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresTextResponseParams]) -> str: ...
    @overload
    async def scores(self, **params: Unpack[FlashscoreScoresDefaultParams]) -> FlashscoreScoresResponse: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[FlashscoreSearchDefaultParams]) -> FlashscoreSearchResponse: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsStreamParams]) -> BinaryIO: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsTextResponseParams]) -> str: ...
    @overload
    async def sports(self, **params: Unpack[FlashscoreSportsDefaultParams]) -> FlashscoreSportsResponse: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamStreamParams]) -> BinaryIO: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamTextResponseParams]) -> str: ...
    @overload
    async def team(self, **params: Unpack[FlashscoreTeamDefaultParams]) -> FlashscoreTeamResponse: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesStreamParams]) -> BinaryIO: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesTextResponseParams]) -> str: ...
    @overload
    async def team_fixtures(self, **params: Unpack[FlashscoreTeamFixturesDefaultParams]) -> FlashscoreTeamFixturesResponse: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsTextResponseParams]) -> str: ...
    @overload
    async def team_news(self, **params: Unpack[FlashscoreTeamNewsDefaultParams]) -> FlashscoreTeamNewsResponse: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsTextResponseParams]) -> str: ...
    @overload
    async def team_outright_odds(self, **params: Unpack[FlashscoreTeamOutrightOddsDefaultParams]) -> FlashscoreTeamOutrightOddsResponse: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsStreamParams]) -> BinaryIO: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsTextResponseParams]) -> str: ...
    @overload
    async def team_results(self, **params: Unpack[FlashscoreTeamResultsDefaultParams]) -> FlashscoreTeamResultsResponse: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadStreamParams]) -> BinaryIO: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadTextResponseParams]) -> str: ...
    @overload
    async def team_squad(self, **params: Unpack[FlashscoreTeamSquadDefaultParams]) -> FlashscoreTeamSquadResponse: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersStreamParams]) -> BinaryIO: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersTextResponseParams]) -> str: ...
    @overload
    async def team_transfers(self, **params: Unpack[FlashscoreTeamTransfersDefaultParams]) -> FlashscoreTeamTransfersResponse: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchTextResponseParams]) -> str: ...
    @overload
    async def top_search(self, **params: Unpack[FlashscoreTopSearchDefaultParams]) -> FlashscoreTopSearchResponse: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_archive_seasons(self, **params: Unpack[FlashscoreTournamentArchiveSeasonsDefaultParams]) -> FlashscoreTournamentArchiveSeasonsResponse: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsTextResponseParams]) -> str: ...
    @overload
    async def tournament_events(self, **params: Unpack[FlashscoreTournamentEventsDefaultParams]) -> FlashscoreTournamentEventsResponse: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsTextResponseParams]) -> str: ...
    @overload
    async def tournament_outright_odds(self, **params: Unpack[FlashscoreTournamentOutrightOddsDefaultParams]) -> FlashscoreTournamentOutrightOddsResponse: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsTextResponseParams]) -> str: ...
    @overload
    async def tournament_seasons(self, **params: Unpack[FlashscoreTournamentSeasonsDefaultParams]) -> FlashscoreTournamentSeasonsResponse: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings(self, **params: Unpack[FlashscoreTournamentStandingsDefaultParams]) -> FlashscoreTournamentStandingsResponse: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsStreamParams]) -> BinaryIO: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsTextResponseParams]) -> str: ...
    @overload
    async def tournament_standings_views(self, **params: Unpack[FlashscoreTournamentStandingsViewsDefaultParams]) -> FlashscoreTournamentStandingsViewsResponse: ...

FlashscoreCalendarDefaultParams = TypedDict('FlashscoreCalendarDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarTextResponseParams = TypedDict('FlashscoreCalendarTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarStreamParams = TypedDict('FlashscoreCalendarStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': Required[Literal['tennis-atp', 'tennis-wta', 'golf-pga', 'golf-dp-world', 'badminton-bwf', 'motorsport-f1']],
}, total=False)

FlashscoreCalendarCategoriesDefaultParams = TypedDict('FlashscoreCalendarCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreCalendarCategoriesTextResponseParams = TypedDict('FlashscoreCalendarCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreCalendarCategoriesStreamParams = TypedDict('FlashscoreCalendarCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreCompetitionsDefaultParams = TypedDict('FlashscoreCompetitionsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreCompetitionsTextResponseParams = TypedDict('FlashscoreCompetitionsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreCompetitionsStreamParams = TypedDict('FlashscoreCompetitionsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreEntityNewsDefaultParams = TypedDict('FlashscoreEntityNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'type': Required[Literal['team', 'player', 'tournament', 'sport']],
    'id': Required[str],
}, total=False)

FlashscoreEntityNewsTextResponseParams = TypedDict('FlashscoreEntityNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'type': Required[Literal['team', 'player', 'tournament', 'sport']],
    'id': Required[str],
}, total=False)

FlashscoreEntityNewsStreamParams = TypedDict('FlashscoreEntityNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'type': Required[Literal['team', 'player', 'tournament', 'sport']],
    'id': Required[str],
}, total=False)

FlashscoreMatchBoxScoreDefaultParams = TypedDict('FlashscoreMatchBoxScoreDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchBoxScoreTextResponseParams = TypedDict('FlashscoreMatchBoxScoreTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchBoxScoreStreamParams = TypedDict('FlashscoreMatchBoxScoreStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchDartsDefaultParams = TypedDict('FlashscoreMatchDartsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchDartsTextResponseParams = TypedDict('FlashscoreMatchDartsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchDartsStreamParams = TypedDict('FlashscoreMatchDartsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchH2hDefaultParams = TypedDict('FlashscoreMatchH2hDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchH2hTextResponseParams = TypedDict('FlashscoreMatchH2hTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchH2hStreamParams = TypedDict('FlashscoreMatchH2hStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsDefaultParams = TypedDict('FlashscoreMatchHighlightsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsTextResponseParams = TypedDict('FlashscoreMatchHighlightsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchHighlightsStreamParams = TypedDict('FlashscoreMatchHighlightsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoDefaultParams = TypedDict('FlashscoreMatchInfoDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoTextResponseParams = TypedDict('FlashscoreMatchInfoTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchInfoStreamParams = TypedDict('FlashscoreMatchInfoStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsDefaultParams = TypedDict('FlashscoreMatchLineupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsTextResponseParams = TypedDict('FlashscoreMatchLineupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchLineupsStreamParams = TypedDict('FlashscoreMatchLineupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMissingPlayersDefaultParams = TypedDict('FlashscoreMatchMissingPlayersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMissingPlayersTextResponseParams = TypedDict('FlashscoreMatchMissingPlayersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMissingPlayersStreamParams = TypedDict('FlashscoreMatchMissingPlayersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMomentumDefaultParams = TypedDict('FlashscoreMatchMomentumDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMomentumTextResponseParams = TypedDict('FlashscoreMatchMomentumTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchMomentumStreamParams = TypedDict('FlashscoreMatchMomentumStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsDefaultParams = TypedDict('FlashscoreMatchNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsTextResponseParams = TypedDict('FlashscoreMatchNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchNewsStreamParams = TypedDict('FlashscoreMatchNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchOddsDefaultParams = TypedDict('FlashscoreMatchOddsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
    'betting_type': NotRequired[Literal['HOME_DRAW_AWAY', 'HOME_AWAY', 'DRAW_NO_BET', 'DOUBLE_CHANCE', 'ASIAN_HANDICAP', 'EUROPEAN_HANDICAP', 'OVER_UNDER', 'BOTH_TEAMS_TO_SCORE', 'CORRECT_SCORE', 'HALF_FULL_TIME', 'ODD_OR_EVEN', 'TO_QUALIFY', 'NEXT_GOAL', 'TOP_POSITION_MERGED', 'TO_WIN_AND_TOP_POSITION', 'WIN_EACH_WAY']],
    'scope': NotRequired[Literal['FULL_TIME', 'FULL_TIME_OVER_TIME', 'FIRST_HALF', 'SECOND_HALF', 'FIRST_PERIOD', 'FIRST_QUARTER', 'FIRST_SET', 'SECOND_SET']],
}, total=False)

FlashscoreMatchOddsTextResponseParams = TypedDict('FlashscoreMatchOddsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
    'betting_type': NotRequired[Literal['HOME_DRAW_AWAY', 'HOME_AWAY', 'DRAW_NO_BET', 'DOUBLE_CHANCE', 'ASIAN_HANDICAP', 'EUROPEAN_HANDICAP', 'OVER_UNDER', 'BOTH_TEAMS_TO_SCORE', 'CORRECT_SCORE', 'HALF_FULL_TIME', 'ODD_OR_EVEN', 'TO_QUALIFY', 'NEXT_GOAL', 'TOP_POSITION_MERGED', 'TO_WIN_AND_TOP_POSITION', 'WIN_EACH_WAY']],
    'scope': NotRequired[Literal['FULL_TIME', 'FULL_TIME_OVER_TIME', 'FIRST_HALF', 'SECOND_HALF', 'FIRST_PERIOD', 'FIRST_QUARTER', 'FIRST_SET', 'SECOND_SET']],
}, total=False)

FlashscoreMatchOddsStreamParams = TypedDict('FlashscoreMatchOddsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
    'betting_type': NotRequired[Literal['HOME_DRAW_AWAY', 'HOME_AWAY', 'DRAW_NO_BET', 'DOUBLE_CHANCE', 'ASIAN_HANDICAP', 'EUROPEAN_HANDICAP', 'OVER_UNDER', 'BOTH_TEAMS_TO_SCORE', 'CORRECT_SCORE', 'HALF_FULL_TIME', 'ODD_OR_EVEN', 'TO_QUALIFY', 'NEXT_GOAL', 'TOP_POSITION_MERGED', 'TO_WIN_AND_TOP_POSITION', 'WIN_EACH_WAY']],
    'scope': NotRequired[Literal['FULL_TIME', 'FULL_TIME_OVER_TIME', 'FIRST_HALF', 'SECOND_HALF', 'FIRST_PERIOD', 'FIRST_QUARTER', 'FIRST_SET', 'SECOND_SET']],
}, total=False)

FlashscoreMatchPlayerStatsDefaultParams = TypedDict('FlashscoreMatchPlayerStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'player_id': NotRequired[str],
    'group': NotRequired[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']],
}, total=False)

FlashscoreMatchPlayerStatsTextResponseParams = TypedDict('FlashscoreMatchPlayerStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'player_id': NotRequired[str],
    'group': NotRequired[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']],
}, total=False)

FlashscoreMatchPlayerStatsStreamParams = TypedDict('FlashscoreMatchPlayerStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'player_id': NotRequired[str],
    'group': NotRequired[Literal['top_stats', 'shots', 'attack', 'passes', 'defense', 'goalkeeping', 'general']],
}, total=False)

FlashscoreMatchPointByPointDefaultParams = TypedDict('FlashscoreMatchPointByPointDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPointByPointTextResponseParams = TypedDict('FlashscoreMatchPointByPointTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPointByPointStreamParams = TypedDict('FlashscoreMatchPointByPointStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPredictedLineupsDefaultParams = TypedDict('FlashscoreMatchPredictedLineupsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPredictedLineupsTextResponseParams = TypedDict('FlashscoreMatchPredictedLineupsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchPredictedLineupsStreamParams = TypedDict('FlashscoreMatchPredictedLineupsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchReportDefaultParams = TypedDict('FlashscoreMatchReportDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchReportTextResponseParams = TypedDict('FlashscoreMatchReportTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchReportStreamParams = TypedDict('FlashscoreMatchReportStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStandingsDefaultParams = TypedDict('FlashscoreMatchStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStandingsTextResponseParams = TypedDict('FlashscoreMatchStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStandingsStreamParams = TypedDict('FlashscoreMatchStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'overunder_overall', 'form_home', 'form_away', 'top_scorers', 'htft_overall', 'htft_home', 'htft_away', 'live_overall', 'overunder_home', 'overunder_away']],
}, total=False)

FlashscoreMatchStatsDefaultParams = TypedDict('FlashscoreMatchStatsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStatsTextResponseParams = TypedDict('FlashscoreMatchStatsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchStatsStreamParams = TypedDict('FlashscoreMatchStatsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreMatchTvDefaultParams = TypedDict('FlashscoreMatchTvDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
}, total=False)

FlashscoreMatchTvTextResponseParams = TypedDict('FlashscoreMatchTvTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
}, total=False)

FlashscoreMatchTvStreamParams = TypedDict('FlashscoreMatchTvStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
}, total=False)

FlashscoreNavigationDefaultParams = TypedDict('FlashscoreNavigationDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNavigationTextResponseParams = TypedDict('FlashscoreNavigationTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNavigationStreamParams = TypedDict('FlashscoreNavigationStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'path': NotRequired[str],
}, total=False)

FlashscoreNewsDefaultParams = TypedDict('FlashscoreNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsTextResponseParams = TypedDict('FlashscoreNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsStreamParams = TypedDict('FlashscoreNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': NotRequired[Literal['all', 'football', 'uefa-nations-league', 'tennis', 'features', 'premier-league', 'nfl', 'mlb', 'nba', 'nhl', 'formula-1', 'champions-league', 'europa-league', 'conference-league', 'darts', 'snooker', 'golf', 'road-cycling', 'laliga', 'bundesliga', 'serie-a', 'ligue-1', 'badminton', 'handball', 'hockey', 'basketball', 'cricket', 'rugby-union', 'athletics', 'baseball', 'fifa', 'rugby-league', 'motorsport', 'aussie-rules', 'flashscore-ratings', 'american-sports', 'african-football', 'combat-sports', 'winter-sports', 'transfer-news']],
    'page': NotRequired[int],
}, total=False)

FlashscoreNewsArticleDefaultParams = TypedDict('FlashscoreNewsArticleDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleTextResponseParams = TypedDict('FlashscoreNewsArticleTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleStreamParams = TypedDict('FlashscoreNewsArticleStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleBodyDefaultParams = TypedDict('FlashscoreNewsArticleBodyDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleBodyTextResponseParams = TypedDict('FlashscoreNewsArticleBodyTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsArticleBodyStreamParams = TypedDict('FlashscoreNewsArticleBodyStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreNewsCategoriesDefaultParams = TypedDict('FlashscoreNewsCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreNewsCategoriesTextResponseParams = TypedDict('FlashscoreNewsCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreNewsCategoriesStreamParams = TypedDict('FlashscoreNewsCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreNewsMostReadDefaultParams = TypedDict('FlashscoreNewsMostReadDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreNewsMostReadTextResponseParams = TypedDict('FlashscoreNewsMostReadTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreNewsMostReadStreamParams = TypedDict('FlashscoreNewsMostReadStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreOddsGeosDefaultParams = TypedDict('FlashscoreOddsGeosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreOddsGeosTextResponseParams = TypedDict('FlashscoreOddsGeosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreOddsGeosStreamParams = TypedDict('FlashscoreOddsGeosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscorePlayerDefaultParams = TypedDict('FlashscorePlayerDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerTextResponseParams = TypedDict('FlashscorePlayerTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerStreamParams = TypedDict('FlashscorePlayerStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerFixturesDefaultParams = TypedDict('FlashscorePlayerFixturesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerFixturesTextResponseParams = TypedDict('FlashscorePlayerFixturesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerFixturesStreamParams = TypedDict('FlashscorePlayerFixturesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerInjuriesDefaultParams = TypedDict('FlashscorePlayerInjuriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerInjuriesTextResponseParams = TypedDict('FlashscorePlayerInjuriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerInjuriesStreamParams = TypedDict('FlashscorePlayerInjuriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerMatchLogDefaultParams = TypedDict('FlashscorePlayerMatchLogDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerMatchLogTextResponseParams = TypedDict('FlashscorePlayerMatchLogTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerMatchLogStreamParams = TypedDict('FlashscorePlayerMatchLogStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerNewsDefaultParams = TypedDict('FlashscorePlayerNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscorePlayerNewsTextResponseParams = TypedDict('FlashscorePlayerNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscorePlayerNewsStreamParams = TypedDict('FlashscorePlayerNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscorePlayerResultsDefaultParams = TypedDict('FlashscorePlayerResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerResultsTextResponseParams = TypedDict('FlashscorePlayerResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerResultsStreamParams = TypedDict('FlashscorePlayerResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscorePlayerTransfersDefaultParams = TypedDict('FlashscorePlayerTransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerTransfersTextResponseParams = TypedDict('FlashscorePlayerTransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscorePlayerTransfersStreamParams = TypedDict('FlashscorePlayerTransfersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'slug': NotRequired[str],
}, total=False)

FlashscoreRankingCategoriesDefaultParams = TypedDict('FlashscoreRankingCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreRankingCategoriesTextResponseParams = TypedDict('FlashscoreRankingCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreRankingCategoriesStreamParams = TypedDict('FlashscoreRankingCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreRankingsDefaultParams = TypedDict('FlashscoreRankingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreRankingsTextResponseParams = TypedDict('FlashscoreRankingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreRankingsStreamParams = TypedDict('FlashscoreRankingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'category': Required[Literal['fifa', 'tennis-atp', 'tennis-wta', 'tennis-atp-race', 'tennis-wta-race', 'tennis-atp-doubles', 'tennis-wta-doubles', 'tennis-atp-doubles-race', 'tennis-wta-doubles-race', 'badminton-bwf-singles-men', 'badminton-bwf-singles-women', 'badminton-bwf-doubles-men', 'badminton-bwf-doubles-women', 'badminton-bwf-mixed-doubles', 'golf-owgr', 'golf-wwgr', 'golf-pga-fedexcup', 'golf-pga-money', 'golf-dp-world-tour', 'golf-lpga', 'golf-asian-tour', 'golf-japan-tour', 'golf-sunshine-tour', 'golf-korn-ferry', 'golf-champions-tour', 'darts-world-ranking', 'snooker-world-ranking', 'tennis-atp-live', 'tennis-wta-live', 'tennis-atp-race-live', 'tennis-wta-race-live', 'tennis-atp-doubles-live', 'tennis-wta-doubles-live', 'tennis-atp-doubles-race-live', 'tennis-wta-doubles-race-live']],
}, total=False)

FlashscoreScoresDefaultParams = TypedDict('FlashscoreScoresDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreScoresTextResponseParams = TypedDict('FlashscoreScoresTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreScoresStreamParams = TypedDict('FlashscoreScoresStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'sport': Required[Literal['football', 'tennis', 'basketball', 'hockey', 'golf', 'formula-1', 'baseball', 'snooker', 'american-football', 'aussie-rules', 'badminton', 'bandy', 'beach-soccer', 'beach-volleyball', 'boxing', 'cricket', 'cycling', 'darts', 'esports', 'field-hockey', 'floorball', 'futsal', 'handball', 'horse-racing', 'kabaddi', 'mma', 'motorsport', 'netball', 'pesapallo', 'rugby-league', 'rugby-union', 'table-tennis', 'volleyball', 'water-polo', 'winter-sports', 'moto-racing', 'ski-jumping', 'alpine-skiing', 'cross-country-skiing', 'biathlon']],
    'day_offset': NotRequired[int],
}, total=False)

FlashscoreSearchDefaultParams = TypedDict('FlashscoreSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
}, total=False)

FlashscoreSearchTextResponseParams = TypedDict('FlashscoreSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
}, total=False)

FlashscoreSearchStreamParams = TypedDict('FlashscoreSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
}, total=False)

FlashscoreSportsDefaultParams = TypedDict('FlashscoreSportsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreSportsTextResponseParams = TypedDict('FlashscoreSportsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreSportsStreamParams = TypedDict('FlashscoreSportsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreTeamDefaultParams = TypedDict('FlashscoreTeamDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamTextResponseParams = TypedDict('FlashscoreTeamTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamStreamParams = TypedDict('FlashscoreTeamStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamFixturesDefaultParams = TypedDict('FlashscoreTeamFixturesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamFixturesTextResponseParams = TypedDict('FlashscoreTeamFixturesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamFixturesStreamParams = TypedDict('FlashscoreTeamFixturesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamNewsDefaultParams = TypedDict('FlashscoreTeamNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamNewsTextResponseParams = TypedDict('FlashscoreTeamNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamNewsStreamParams = TypedDict('FlashscoreTeamNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
}, total=False)

FlashscoreTeamOutrightOddsDefaultParams = TypedDict('FlashscoreTeamOutrightOddsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTeamOutrightOddsTextResponseParams = TypedDict('FlashscoreTeamOutrightOddsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTeamOutrightOddsStreamParams = TypedDict('FlashscoreTeamOutrightOddsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTeamResultsDefaultParams = TypedDict('FlashscoreTeamResultsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamResultsTextResponseParams = TypedDict('FlashscoreTeamResultsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamResultsStreamParams = TypedDict('FlashscoreTeamResultsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamSquadDefaultParams = TypedDict('FlashscoreTeamSquadDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'slug': NotRequired[str],
    'scope': NotRequired[str],
}, total=False)

FlashscoreTeamSquadTextResponseParams = TypedDict('FlashscoreTeamSquadTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'slug': NotRequired[str],
    'scope': NotRequired[str],
}, total=False)

FlashscoreTeamSquadStreamParams = TypedDict('FlashscoreTeamSquadStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'slug': NotRequired[str],
    'scope': NotRequired[str],
}, total=False)

FlashscoreTeamTransfersDefaultParams = TypedDict('FlashscoreTeamTransfersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'id': Required[str],
    'type': NotRequired[Literal['all', 'arrivals', 'departures']],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamTransfersTextResponseParams = TypedDict('FlashscoreTeamTransfersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'id': Required[str],
    'type': NotRequired[Literal['all', 'arrivals', 'departures']],
    'page': NotRequired[int],
}, total=False)

FlashscoreTeamTransfersStreamParams = TypedDict('FlashscoreTeamTransfersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'id': Required[str],
    'type': NotRequired[Literal['all', 'arrivals', 'departures']],
    'page': NotRequired[int],
}, total=False)

FlashscoreTopSearchDefaultParams = TypedDict('FlashscoreTopSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

FlashscoreTopSearchTextResponseParams = TypedDict('FlashscoreTopSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

FlashscoreTopSearchStreamParams = TypedDict('FlashscoreTopSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

FlashscoreTournamentArchiveSeasonsDefaultParams = TypedDict('FlashscoreTournamentArchiveSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'stage_id': Required[str],
}, total=False)

FlashscoreTournamentArchiveSeasonsTextResponseParams = TypedDict('FlashscoreTournamentArchiveSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'stage_id': Required[str],
}, total=False)

FlashscoreTournamentArchiveSeasonsStreamParams = TypedDict('FlashscoreTournamentArchiveSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'stage_id': Required[str],
}, total=False)

FlashscoreTournamentEventsDefaultParams = TypedDict('FlashscoreTournamentEventsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentEventsTextResponseParams = TypedDict('FlashscoreTournamentEventsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentEventsStreamParams = TypedDict('FlashscoreTournamentEventsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'path': Required[str],
    'page': NotRequired[int],
}, total=False)

FlashscoreTournamentOutrightOddsDefaultParams = TypedDict('FlashscoreTournamentOutrightOddsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'tournament_id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTournamentOutrightOddsTextResponseParams = TypedDict('FlashscoreTournamentOutrightOddsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'tournament_id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTournamentOutrightOddsStreamParams = TypedDict('FlashscoreTournamentOutrightOddsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'tournament_id': Required[str],
    'geo': NotRequired[Literal['AE', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BD', 'BE', 'BG', 'BO', 'BR', 'BY', 'CA', 'CH', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FR', 'GB', 'GE', 'GH', 'GR', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IR', 'IS', 'IT', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LK', 'LT', 'LU', 'LV', 'LY', 'MA', 'MD', 'ME', 'MK', 'MM', 'MN', 'MT', 'MX', 'MY', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'PA', 'PE', 'PH', 'PK', 'PL', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'SA', 'SD', 'SE', 'SG', 'SI', 'SK', 'SN', 'SV', 'TH', 'TN', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VE', 'VN', 'XK', 'ZA', 'ZM', 'ZW']],
    'subdivision': NotRequired[Literal['AB', 'AK', 'AL', 'AR', 'AZ', 'BC', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MB', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NB', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NL', 'NM', 'NS', 'NT', 'NU', 'NV', 'NY', 'OH', 'OK', 'ON', 'OR', 'PA', 'PE', 'QC', 'RI', 'SC', 'SD', 'SK', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY', 'YT']],
}, total=False)

FlashscoreTournamentSeasonsDefaultParams = TypedDict('FlashscoreTournamentSeasonsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentSeasonsTextResponseParams = TypedDict('FlashscoreTournamentSeasonsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentSeasonsStreamParams = TypedDict('FlashscoreTournamentSeasonsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsDefaultParams = TypedDict('FlashscoreTournamentStandingsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsTextResponseParams = TypedDict('FlashscoreTournamentStandingsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsStreamParams = TypedDict('FlashscoreTournamentStandingsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'path': Required[str],
    'view': NotRequired[Literal['overall', 'home', 'away', 'form_overall', 'form_home', 'form_away', 'overunder_overall', 'overunder_home', 'overunder_away', 'htft_overall', 'htft_home', 'htft_away', 'top_scorers']],
}, total=False)

FlashscoreTournamentStandingsViewsDefaultParams = TypedDict('FlashscoreTournamentStandingsViewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsViewsTextResponseParams = TypedDict('FlashscoreTournamentStandingsViewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'path': Required[str],
}, total=False)

FlashscoreTournamentStandingsViewsStreamParams = TypedDict('FlashscoreTournamentStandingsViewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'path': Required[str],
}, total=False)
