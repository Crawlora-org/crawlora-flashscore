"""Typed Flashscore client for the Crawlora hosted API."""

from .platform import FlashscoreClient, AsyncFlashscoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FlashscoreClient
AsyncClient = AsyncFlashscoreClient
__version__ = '0.4.0'
DISPLAY_NAME = 'Flashscore'
PLATFORM = 'flashscore'
CONTRACT_REVISION = 'sha256:5b6ce781b90a431c7e295bd02964a902982e33385cf7e458c77ef01a338facbb'

__all__ = [
    "FlashscoreClient", "AsyncFlashscoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
