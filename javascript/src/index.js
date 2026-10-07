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
    super({ ...options, userAgent: options.userAgent ?? "crawlora-flashscore-js/0.1.3" });
    this["calendar"] = (...args) => this.request("flashscore-calendar", ...args);
    this["calendarCategories"] = (...args) => this.request("flashscore-calendar-categories", ...args);
    this["competitions"] = (...args) => this.request("flashscore-competitions", ...args);
    this["matchH2h"] = (...args) => this.request("flashscore-match-h2h", ...args);
    this["matchHighlights"] = (...args) => this.request("flashscore-match-highlights", ...args);
    this["matchInfo"] = (...args) => this.request("flashscore-match-info", ...args);
    this["matchLineups"] = (...args) => this.request("flashscore-match-lineups", ...args);
    this["matchNews"] = (...args) => this.request("flashscore-match-news", ...args);
    this["matchStandings"] = (...args) => this.request("flashscore-match-standings", ...args);
    this["matchStats"] = (...args) => this.request("flashscore-match-stats", ...args);
    this["navigation"] = (...args) => this.request("flashscore-navigation", ...args);
    this["news"] = (...args) => this.request("flashscore-news", ...args);
    this["newsArticle"] = (...args) => this.request("flashscore-news-article", ...args);
    this["newsCategories"] = (...args) => this.request("flashscore-news-categories", ...args);
    this["rankingCategories"] = (...args) => this.request("flashscore-ranking-categories", ...args);
    this["rankings"] = (...args) => this.request("flashscore-rankings", ...args);
    this["scores"] = (...args) => this.request("flashscore-scores", ...args);
    this["search"] = (...args) => this.request("flashscore-search", ...args);
    this["sports"] = (...args) => this.request("flashscore-sports", ...args);
    this["topSearch"] = (...args) => this.request("flashscore-top-search", ...args);
    this["tournamentEvents"] = (...args) => this.request("flashscore-tournament-events", ...args);
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
export const VERSION = "0.1.3";
export default FlashscoreClient;
