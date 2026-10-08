"""Typed Flashscore client for the Crawlora hosted API."""

from .platform import FlashscoreClient, AsyncFlashscoreClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FlashscoreClient
AsyncClient = AsyncFlashscoreClient
__version__ = '0.3.0'
DISPLAY_NAME = 'Flashscore'
PLATFORM = 'flashscore'
CONTRACT_REVISION = 'sha256:1ade3db4148f310594a6b4f738e69dea677015e4a98ee2945cdb6ee380fa9630'

__all__ = [
    "FlashscoreClient", "AsyncFlashscoreClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
