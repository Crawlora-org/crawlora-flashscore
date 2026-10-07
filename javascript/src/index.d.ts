import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class FlashscoreClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  calendar(params: OperationParamsMap["flashscore-calendar"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  calendarCategories(params?: OperationParamsMap["flashscore-calendar-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  competitions(params: OperationParamsMap["flashscore-competitions"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchH2h(params: OperationParamsMap["flashscore-match-h2h"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchHighlights(params: OperationParamsMap["flashscore-match-highlights"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchInfo(params: OperationParamsMap["flashscore-match-info"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchLineups(params: OperationParamsMap["flashscore-match-lineups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchMissingPlayers(params: OperationParamsMap["flashscore-match-missing-players"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchNews(params: OperationParamsMap["flashscore-match-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchOdds(params: OperationParamsMap["flashscore-match-odds"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchPredictedLineups(params: OperationParamsMap["flashscore-match-predicted-lineups"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchStandings(params: OperationParamsMap["flashscore-match-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchStats(params: OperationParamsMap["flashscore-match-stats"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  matchTv(params: OperationParamsMap["flashscore-match-tv"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  navigation(params?: OperationParamsMap["flashscore-navigation"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  news(params?: OperationParamsMap["flashscore-news"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsArticle(params: OperationParamsMap["flashscore-news-article"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  newsCategories(params?: OperationParamsMap["flashscore-news-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  oddsGeos(params?: OperationParamsMap["flashscore-odds-geos"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  player(params: OperationParamsMap["flashscore-player"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerInjuries(params: OperationParamsMap["flashscore-player-injuries"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  playerTransfers(params: OperationParamsMap["flashscore-player-transfers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankingCategories(params?: OperationParamsMap["flashscore-ranking-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  rankings(params: OperationParamsMap["flashscore-rankings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  scores(params: OperationParamsMap["flashscore-scores"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params: OperationParamsMap["flashscore-search"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  sports(params?: OperationParamsMap["flashscore-sports"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  team(params: OperationParamsMap["flashscore-team"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamFixtures(params: OperationParamsMap["flashscore-team-fixtures"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamNews(params: OperationParamsMap["flashscore-team-news"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamResults(params: OperationParamsMap["flashscore-team-results"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamSquad(params: OperationParamsMap["flashscore-team-squad"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  teamTransfers(params: OperationParamsMap["flashscore-team-transfers"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  topSearch(params?: OperationParamsMap["flashscore-top-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentEvents(params: OperationParamsMap["flashscore-tournament-events"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentSeasons(params: OperationParamsMap["flashscore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentStandings(params: OperationParamsMap["flashscore-tournament-standings"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  tournamentStandingsViews(params: OperationParamsMap["flashscore-tournament-standings-views"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  calendar(params: OperationParamsMap["flashscore-calendar"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  calendarCategories(params?: OperationParamsMap["flashscore-calendar-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  competitions(params: OperationParamsMap["flashscore-competitions"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchH2h(params: OperationParamsMap["flashscore-match-h2h"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchHighlights(params: OperationParamsMap["flashscore-match-highlights"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchInfo(params: OperationParamsMap["flashscore-match-info"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchLineups(params: OperationParamsMap["flashscore-match-lineups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchMissingPlayers(params: OperationParamsMap["flashscore-match-missing-players"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchNews(params: OperationParamsMap["flashscore-match-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchOdds(params: OperationParamsMap["flashscore-match-odds"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchPredictedLineups(params: OperationParamsMap["flashscore-match-predicted-lineups"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchStandings(params: OperationParamsMap["flashscore-match-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchStats(params: OperationParamsMap["flashscore-match-stats"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  matchTv(params: OperationParamsMap["flashscore-match-tv"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  navigation(params?: OperationParamsMap["flashscore-navigation"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  news(params?: OperationParamsMap["flashscore-news"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsArticle(params: OperationParamsMap["flashscore-news-article"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  newsCategories(params?: OperationParamsMap["flashscore-news-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  oddsGeos(params?: OperationParamsMap["flashscore-odds-geos"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  player(params: OperationParamsMap["flashscore-player"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerInjuries(params: OperationParamsMap["flashscore-player-injuries"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  playerTransfers(params: OperationParamsMap["flashscore-player-transfers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankingCategories(params?: OperationParamsMap["flashscore-ranking-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  rankings(params: OperationParamsMap["flashscore-rankings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  scores(params: OperationParamsMap["flashscore-scores"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params: OperationParamsMap["flashscore-search"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  sports(params?: OperationParamsMap["flashscore-sports"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  team(params: OperationParamsMap["flashscore-team"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamFixtures(params: OperationParamsMap["flashscore-team-fixtures"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamNews(params: OperationParamsMap["flashscore-team-news"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamResults(params: OperationParamsMap["flashscore-team-results"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamSquad(params: OperationParamsMap["flashscore-team-squad"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  teamTransfers(params: OperationParamsMap["flashscore-team-transfers"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  topSearch(params?: OperationParamsMap["flashscore-top-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentEvents(params: OperationParamsMap["flashscore-tournament-events"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentSeasons(params: OperationParamsMap["flashscore-tournament-seasons"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentStandings(params: OperationParamsMap["flashscore-tournament-standings"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  tournamentStandingsViews(params: OperationParamsMap["flashscore-tournament-standings-views"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  calendar(...args: OperationRequestArgs<"flashscore-calendar">): Promise<OperationResponseMap["flashscore-calendar"]>;
  calendarCategories(...args: OperationRequestArgs<"flashscore-calendar-categories">): Promise<OperationResponseMap["flashscore-calendar-categories"]>;
  competitions(...args: OperationRequestArgs<"flashscore-competitions">): Promise<OperationResponseMap["flashscore-competitions"]>;
  matchH2h(...args: OperationRequestArgs<"flashscore-match-h2h">): Promise<OperationResponseMap["flashscore-match-h2h"]>;
  matchHighlights(...args: OperationRequestArgs<"flashscore-match-highlights">): Promise<OperationResponseMap["flashscore-match-highlights"]>;
  matchInfo(...args: OperationRequestArgs<"flashscore-match-info">): Promise<OperationResponseMap["flashscore-match-info"]>;
  matchLineups(...args: OperationRequestArgs<"flashscore-match-lineups">): Promise<OperationResponseMap["flashscore-match-lineups"]>;
  matchMissingPlayers(...args: OperationRequestArgs<"flashscore-match-missing-players">): Promise<OperationResponseMap["flashscore-match-missing-players"]>;
  matchNews(...args: OperationRequestArgs<"flashscore-match-news">): Promise<OperationResponseMap["flashscore-match-news"]>;
  matchOdds(...args: OperationRequestArgs<"flashscore-match-odds">): Promise<OperationResponseMap["flashscore-match-odds"]>;
  matchPredictedLineups(...args: OperationRequestArgs<"flashscore-match-predicted-lineups">): Promise<OperationResponseMap["flashscore-match-predicted-lineups"]>;
  matchStandings(...args: OperationRequestArgs<"flashscore-match-standings">): Promise<OperationResponseMap["flashscore-match-standings"]>;
  matchStats(...args: OperationRequestArgs<"flashscore-match-stats">): Promise<OperationResponseMap["flashscore-match-stats"]>;
  matchTv(...args: OperationRequestArgs<"flashscore-match-tv">): Promise<OperationResponseMap["flashscore-match-tv"]>;
  navigation(...args: OperationRequestArgs<"flashscore-navigation">): Promise<OperationResponseMap["flashscore-navigation"]>;
  news(...args: OperationRequestArgs<"flashscore-news">): Promise<OperationResponseMap["flashscore-news"]>;
  newsArticle(...args: OperationRequestArgs<"flashscore-news-article">): Promise<OperationResponseMap["flashscore-news-article"]>;
  newsCategories(...args: OperationRequestArgs<"flashscore-news-categories">): Promise<OperationResponseMap["flashscore-news-categories"]>;
  oddsGeos(...args: OperationRequestArgs<"flashscore-odds-geos">): Promise<OperationResponseMap["flashscore-odds-geos"]>;
  player(...args: OperationRequestArgs<"flashscore-player">): Promise<OperationResponseMap["flashscore-player"]>;
  playerInjuries(...args: OperationRequestArgs<"flashscore-player-injuries">): Promise<OperationResponseMap["flashscore-player-injuries"]>;
  playerTransfers(...args: OperationRequestArgs<"flashscore-player-transfers">): Promise<OperationResponseMap["flashscore-player-transfers"]>;
  rankingCategories(...args: OperationRequestArgs<"flashscore-ranking-categories">): Promise<OperationResponseMap["flashscore-ranking-categories"]>;
  rankings(...args: OperationRequestArgs<"flashscore-rankings">): Promise<OperationResponseMap["flashscore-rankings"]>;
  scores(...args: OperationRequestArgs<"flashscore-scores">): Promise<OperationResponseMap["flashscore-scores"]>;
  search(...args: OperationRequestArgs<"flashscore-search">): Promise<OperationResponseMap["flashscore-search"]>;
  sports(...args: OperationRequestArgs<"flashscore-sports">): Promise<OperationResponseMap["flashscore-sports"]>;
  team(...args: OperationRequestArgs<"flashscore-team">): Promise<OperationResponseMap["flashscore-team"]>;
  teamFixtures(...args: OperationRequestArgs<"flashscore-team-fixtures">): Promise<OperationResponseMap["flashscore-team-fixtures"]>;
  teamNews(...args: OperationRequestArgs<"flashscore-team-news">): Promise<OperationResponseMap["flashscore-team-news"]>;
  teamResults(...args: OperationRequestArgs<"flashscore-team-results">): Promise<OperationResponseMap["flashscore-team-results"]>;
  teamSquad(...args: OperationRequestArgs<"flashscore-team-squad">): Promise<OperationResponseMap["flashscore-team-squad"]>;
  teamTransfers(...args: OperationRequestArgs<"flashscore-team-transfers">): Promise<OperationResponseMap["flashscore-team-transfers"]>;
  topSearch(...args: OperationRequestArgs<"flashscore-top-search">): Promise<OperationResponseMap["flashscore-top-search"]>;
  tournamentEvents(...args: OperationRequestArgs<"flashscore-tournament-events">): Promise<OperationResponseMap["flashscore-tournament-events"]>;
  tournamentSeasons(...args: OperationRequestArgs<"flashscore-tournament-seasons">): Promise<OperationResponseMap["flashscore-tournament-seasons"]>;
  tournamentStandings(...args: OperationRequestArgs<"flashscore-tournament-standings">): Promise<OperationResponseMap["flashscore-tournament-standings"]>;
  tournamentStandingsViews(...args: OperationRequestArgs<"flashscore-tournament-standings-views">): Promise<OperationResponseMap["flashscore-tournament-standings-views"]>;
}
export { FlashscoreClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default FlashscoreClient;
