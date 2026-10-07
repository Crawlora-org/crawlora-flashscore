"""Typed Flashscore client for the Crawlora hosted API."""

from .platform import FlashscoreClient, AsyncFlashscoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FlashscoreClient
AsyncClient = AsyncFlashscoreClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Flashscore'
PLATFORM = 'flashscore'
CONTRACT_REVISION = 'sha256:fcaf7e58d82dcbe73e54cddcffc79511b5d01e2c25d511531656862dfe91fb3e'

__all__ = [
    "FlashscoreClient", "AsyncFlashscoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
