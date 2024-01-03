class AzuracastException(Exception):
    """The base Azuracast Exception class that all other exceptions will extend"""

class AccessDeniedException(AzuracastException):
    """Indicates unauthorized access to certain endpoints."""

class AzuracastAPIException(AzuracastException):
    """Indicates errors encountered from the Azuracast API."""

class ClientException(AzuracastException):
    """Indicates errors made by the user of the API."""