import requests
from requests.exceptions import JSONDecodeError

from exceptions import ClientException, AccessDeniedException, AzuracastException

from lxml import html # A HTML parser is needed to extract the errors

from typing import Optional, Tuple

def send_request(method: str, url: str, body: Optional[str] = None, headers: Optional[str] = None):
    method = method.upper()

    # Due to the nature of the API:
    # - Log In errors return a response code of 200
    # - Most of the other errors return a response code of 500
    # - Both of these error types return HTML instead of JSON
    # These events are checked for in this code block
    with requests.request(method=method, url=url, data=body, headers=headers) as response:
        if response.status_code == 500:
            error = _get_specific_error(response.text)
            raise AzuracastException(f"Encountered request error: {error[0]} - {error[1]}")

        if response.status_code == 404:
            raise ClientException("Requested resource not found.")

        if response.status_code == 200:
            try:
                return response.json()
            except (ValueError, JSONDecodeError):
                if _confirm_login_error(response.text) is True:
                    raise AccessDeniedException("You silly goose. Your x-api-key value seems to be invalid. Correct any mistakes and try again.")

def _get_specific_error(text: str) -> Tuple:
    doc = html.fromstring(text)
    error_title = doc.xpath(".//p[@class='text-muted card-text']")[0].text
    error_description = doc.find('.//h4').text.strip()

    error_title = error_title.split('/')[2].split('.')[0]

    return (error_title, error_description)

def _confirm_login_error(text: str) -> bool:
    doc = html.fromstring(text)
    title = doc.find('.//title')

    return title.text.strip() == 'Log In - AzuraCast'