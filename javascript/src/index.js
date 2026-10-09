import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class FlashscoreClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-flashscore-js/0.3.4" });
    this["calendar"] = (...args) => this.request("flashscore-calendar", ...args);
    this["calendarCategories"] = (...args) => this.request("flashscore-calendar-categories", ...args);
    this["competitions"] = (...args) => this.request("flashscore-competitions", ...args);
    this["entityNews"] = (...args) => this.request("flashscore-entity-news", ...args);
    this["matchBoxScore"] = (...args) => this.request("flashscore-match-box-score", ...args);
    this["matchDarts"] = (...args) => this.request("flashscore-match-darts", ...args);
    this["matchH2h"] = (...args) => this.request("flashscore-match-h2h", ...args);
    this["matchHighlights"] = (...args) => this.request("flashscore-match-highlights", ...args);
    this["matchInfo"] = (...args) => this.request("flashscore-match-info", ...args);
    this["matchLineups"] = (...args) => this.request("flashscore-match-lineups", ...args);
    this["matchMissingPlayers"] = (...args) => this.request("flashscore-match-missing-players", ...args);
    this["matchMomentum"] = (...args) => this.request("flashscore-match-momentum", ...args);
    this["matchNews"] = (...args) => this.request("flashscore-match-news", ...args);
    this["matchOdds"] = (...args) => this.request("flashscore-match-odds", ...args);
    this["matchPlayerStats"] = (...args) => this.request("flashscore-match-player-stats", ...args);
    this["matchPointByPoint"] = (...args) => this.request("flashscore-match-point-by-point", ...args);
    this["matchPredictedLineups"] = (...args) => this.request("flashscore-match-predicted-lineups", ...args);
    this["matchReport"] = (...args) => this.request("flashscore-match-report", ...args);
    this["matchStandings"] = (...args) => this.request("flashscore-match-standings", ...args);
    this["matchStats"] = (...args) => this.request("flashscore-match-stats", ...args);
    this["matchTv"] = (...args) => this.request("flashscore-match-tv", ...args);
    this["navigation"] = (...args) => this.request("flashscore-navigation", ...args);
    this["news"] = (...args) => this.request("flashscore-news", ...args);
    this["newsArticle"] = (...args) => this.request("flashscore-news-article", ...args);
    this["newsArticleBody"] = (...args) => this.request("flashscore-news-article-body", ...args);
    this["newsCategories"] = (...args) => this.request("flashscore-news-categories", ...args);
    this["newsMostRead"] = (...args) => this.request("flashscore-news-most-read", ...args);
    this["oddsGeos"] = (...args) => this.request("flashscore-odds-geos", ...args);
    this["player"] = (...args) => this.request("flashscore-player", ...args);
    this["playerFixtures"] = (...args) => this.request("flashscore-player-fixtures", ...args);
    this["playerInjuries"] = (...args) => this.request("flashscore-player-injuries", ...args);
    this["playerMatchLog"] = (...args) => this.request("flashscore-player-match-log", ...args);
    this["playerNews"] = (...args) => this.request("flashscore-player-news", ...args);
    this["playerResults"] = (...args) => this.request("flashscore-player-results", ...args);
    this["playerTransfers"] = (...args) => this.request("flashscore-player-transfers", ...args);
    this["rankingCategories"] = (...args) => this.request("flashscore-ranking-categories", ...args);
    this["rankings"] = (...args) => this.request("flashscore-rankings", ...args);
    this["scores"] = (...args) => this.request("flashscore-scores", ...args);
    this["search"] = (...args) => this.request("flashscore-search", ...args);
    this["sports"] = (...args) => this.request("flashscore-sports", ...args);
    this["team"] = (...args) => this.request("flashscore-team", ...args);
    this["teamFixtures"] = (...args) => this.request("flashscore-team-fixtures", ...args);
    this["teamNews"] = (...args) => this.request("flashscore-team-news", ...args);
    this["teamOutrightOdds"] = (...args) => this.request("flashscore-team-outright-odds", ...args);
    this["teamResults"] = (...args) => this.request("flashscore-team-results", ...args);
    this["teamSquad"] = (...args) => this.request("flashscore-team-squad", ...args);
    this["teamTransfers"] = (...args) => this.request("flashscore-team-transfers", ...args);
    this["topSearch"] = (...args) => this.request("flashscore-top-search", ...args);
    this["tournamentArchiveSeasons"] = (...args) => this.request("flashscore-tournament-archive-seasons", ...args);
    this["tournamentEvents"] = (...args) => this.request("flashscore-tournament-events", ...args);
    this["tournamentOutrightOdds"] = (...args) => this.request("flashscore-tournament-outright-odds", ...args);
    this["tournamentSeasons"] = (...args) => this.request("flashscore-tournament-seasons", ...args);
    this["tournamentStandings"] = (...args) => this.request("flashscore-tournament-standings", ...args);
    this["tournamentStandingsViews"] = (...args) => this.request("flashscore-tournament-standings-views", ...args);
  }
}

export { FlashscoreClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.3.4";
export default FlashscoreClient;
