"""Custom exceptions used in the library."""

class AzuracastException(Exception):
    """The base Azuracast Exception class that all other exceptions will extend"""

class AzuracastAPIException(AzuracastException):
    """Indicates API errors"""

class AccessDeniedException(AzuracastException):
    """Indicates unauthorized access to certain endpoints."""

class UnexpectedErrorException(AzuracastException):
    """Indicates unexpected errors encountered from the Azuracast API."""

class ClientException(AzuracastException):
    """Indicates errors made by the user of the API."""
