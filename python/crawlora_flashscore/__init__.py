"""Typed Flashscore client for the Crawlora hosted API."""

from .platform import FlashscoreClient, AsyncFlashscoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FlashscoreClient
AsyncClient = AsyncFlashscoreClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Flashscore'
PLATFORM = 'flashscore'
CONTRACT_REVISION = 'sha256:380bb303ffcb6ff808a1db512dcc3bd90c9b7d20d62e64d1b368f37c9a6771bd'

__all__ = [
    "FlashscoreClient", "AsyncFlashscoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
