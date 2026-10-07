"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class FlashscoreClient(CrawloraClient):
    """Synchronous Flashscore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-flashscore-python/0.1.0')
        super().__init__(*args, **kwargs)

    def calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    def calendar_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-calendar-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def competitions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-competitions', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_h2h(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-h2h', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-info', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def match_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-match-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    def navigation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-navigation', params, response_type=response_type, timeout=timeout, headers=headers)

    def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-news', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    def news_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-news-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def ranking_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-ranking-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    def scores(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-scores', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    def top_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-top-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-tournament-events', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-tournament-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    def tournament_standings_views(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('flashscore-tournament-standings-views', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncFlashscoreClient(AsyncCrawloraClient):
    """Asynchronous Flashscore API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-flashscore-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def calendar(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-calendar', params, response_type=response_type, timeout=timeout, headers=headers)

    async def calendar_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-calendar-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def competitions(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-competitions', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_h2h(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-h2h', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_highlights(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-highlights', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_info(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-info', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_lineups(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-lineups', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def match_stats(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-match-stats', params, response_type=response_type, timeout=timeout, headers=headers)

    async def navigation(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-navigation', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-news', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_article(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-news-article', params, response_type=response_type, timeout=timeout, headers=headers)

    async def news_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-news-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def ranking_categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-ranking-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def rankings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-rankings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def scores(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-scores', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def sports(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-sports', params, response_type=response_type, timeout=timeout, headers=headers)

    async def top_search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-top-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_events(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-tournament-events', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_seasons(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-tournament-seasons', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_standings(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-tournament-standings', params, response_type=response_type, timeout=timeout, headers=headers)

    async def tournament_standings_views(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('flashscore-tournament-standings-views', params, response_type=response_type, timeout=timeout, headers=headers)
