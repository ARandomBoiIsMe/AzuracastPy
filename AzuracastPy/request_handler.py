"""Handles all requests made by the library."""

from typing import Optional, Tuple, Dict, Any
from json.decoder import JSONDecodeError
from lxml import html # A HTML parser is needed to extract some errors

import requests

from .exceptions import (
    AccessDeniedException,
    AzuracastAPIException,
    UnexpectedErrorException,
    ClientException
)

class RequestHandler:
    def __init__(
        self,
        radio_url: str,
        x_api_key: Optional[str] = None
    ):
        self.radio_url = radio_url
        self._x_api_key = x_api_key
        self._headers = self._set_headers()

    def post(
        self,
        url: str,
        body: Optional[Dict[str, Any]] = None
    ):
        return self._send_request(method='POST', url=url, body=body)

    def get(
        self,
        url: str
    ):
        return self._send_request(method='GET', url=url)

    def put(
        self,
        url: str,
        body: Dict[str, Any]
    ):
        return self._send_request(method='PUT', url=url, body=body)

    def delete(
        self,
        url: str
    ):
        return self._send_request(method='DELETE', url=url)

    # -----------------------------------
    # When testing the API, I ran into multiple instances of NotLoggedIn errors returning a code of
    # 200, as well as some errors returning a code of 500. In addition to this, some errors
    # returned HTML instead of JSON.
    # This behaviour seems to be random. As a result, on top of the normal error logic, I added
    # logic to check for these occurences, just incase. Better safe than sorry I guess.
    # -----------------------------------
    def _send_request(
        self,
        method: str,
        url: str,
        body: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        with requests.request(
            method=method,
            url=url,
            json=body,
            headers=self._headers,
            timeout=10
        ) as response:
            if response.status_code == 500:
                self._handle_500_error(url=url, response=response)

            if response.status_code == 404:
                raise ClientException("Requested resource not found.")

            if response.status_code == 405:
                raise AzuracastAPIException(
                    f"The '{method}' method is not allowed on this endpoint ({url})."
                )

            if response.status_code == 403:
                self._raise_access_denied_exception()

            if response.status_code == 200:
                try:
                    return response.json()
                except (ValueError, KeyError, JSONDecodeError):
                    if self._confirm_login_error(response.text) is True:
                        self._raise_access_denied_exception()

                    self._raise_unexpected_error_exception(url, response.text)

            else:
                self._raise_unexpected_error_exception(url, response.text)

    def _set_headers(self) -> Dict[str, str]:
        return {'accept': 'application/json', 'X-API-Key': self._x_api_key}

    def _handle_500_error(
        self,
        url: str,
        response: requests.Response
    ):
        # Attempts to parse error json response for details.
        try:
            error = response.json()
            self._raise_request_exception(error['type'], error['message'])
        except (ValueError, KeyError, JSONDecodeError):
            pass

        # Error is not valid JSON.
        # Assumes response is error HTML response and tries to parse it to get details.
        try:
            error = self._get_specific_error(response.text)
            self._raise_request_exception(error[0], error[1])
        except:
            # Error is neither JSON nor expected HTML. Unexpected error found.
            self._raise_unexpected_error_exception(url, response.text)

    def _get_specific_error(
        self,
        text: str
    ) -> Tuple:
        doc = html.fromstring(text)
        error_title = doc.xpath(".//p[@class='text-muted card-text']")[0].text
        error_description = doc.find('.//h4').text.strip()

        error_title = error_title.split('/')[2].split('.')[0]

        return (error_title, error_description)

    def _confirm_login_error(
        self,
        text: str
    ) -> bool:
        try:
            doc = html.fromstring(text)
            title = doc.find('.//title')

            return title.text.strip() == 'Log In - AzuraCast'
        except:
            return False

    def _raise_request_exception(
        self,
        error_type: str,
        error_message: str
    ):
        raise AzuracastAPIException(f"Encountered request error: {error_type} - {error_message}")

    def _raise_access_denied_exception(self):
        raise AccessDeniedException(
            "You silly goose. You need a valid x-api-key to perform this action. Provide a valid "
            "key and try again."
        )

    def _raise_unexpected_error_exception(
        self,
        url: str,
        text: str
    ):
        raise UnexpectedErrorException(
            f"Unexpected error occured while trying to access this url: {url}."
            f"\nError details: {text}"
        )
