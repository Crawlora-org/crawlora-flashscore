"""Typed Flashscore client for the Crawlora hosted API."""

from .platform import FlashscoreClient, AsyncFlashscoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FlashscoreClient
AsyncClient = AsyncFlashscoreClient
__version__ = '0.3.6'
DISPLAY_NAME = 'Flashscore'
PLATFORM = 'flashscore'
CONTRACT_REVISION = 'sha256:fd1c70a1b050d86c9e738a62dd14cde04b8a3ce00eb3e281b1d248c1ccdb2e92'

__all__ = [
    "FlashscoreClient", "AsyncFlashscoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
