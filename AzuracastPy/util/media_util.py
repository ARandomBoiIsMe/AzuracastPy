import base64
import os
import requests

from ..constants import API_ENDPOINTS
from ..exceptions import UnexpectedErrorException

def generate_file_upload_structure(path: str, file: str):
    if not os.path.isfile(file):
        raise ValueError(f"File does not exist: {file}")

    contents = None
    with open(file, 'rb') as f:
        contents = f.read()

    contents = base64.b64encode(contents).decode('ascii')

    return {
        "path": path,
        "file": contents
    }

def get_resource_art(self) -> bytes:
    # Had to make a raw request here because the request_handler only returns valid JSON.
    # It doesn't handle bytes. Not yet anyway.
    with requests.get(self.art) as response:
        if response.status_code != 200:
            raise UnexpectedErrorException(
                "Unexpected error occured while trying to retrieve this resource's art. "
               f"\nError details: {response.text}"
            )

        return response.content

def get_media_file_art(self) -> bytes:
    url = API_ENDPOINTS["song_art"].format(
        radio_url=self._station._request_handler.radio_url,
        station_id=self._station.id,
        media_id=self.unique_id
    )

    with requests.get(url) as response:
        if response.status_code != 200:
            raise UnexpectedErrorException(
                "Unexpected error occured while trying to retrieve this file's art. "
               f"\nError details: {response.text}"
            )

        return response.content