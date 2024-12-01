"""A client library for accessing Student-Teacher Meeting Scheduler API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
