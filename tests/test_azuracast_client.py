from AzuracastPy.models.station import Station

import unittest
from unittest import TestCase, mock

from AzuracastPy import AzuracastClient
from AzuracastPy.exceptions import (
    AccessDeniedException, AzuracastAPIException, UnexpectedErrorException, ClientException
)

class TestAzuracastClient(TestCase):
    def setUp(self) -> None:
        self.client = AzuracastClient('')
        self.client._request_handler = mock.MagicMock()

    def test_station_incorrect_id_data_type_raises_type_error(self):
        incorrect_ids = ['', True, 2.0]

        for id in incorrect_ids:
            with self.assertRaises(TypeError):
                self.client.station(id)

    def test_station_negative_id_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.client.station(-2)

    def test_station_returns_station(self):
        self.client._request_handler.get.return_value = {
            "id":1,"name":"my radio","shortcode":"my_radio","description":"","frontend":"icecast",
            "backend":"liquidsoap","listen_url":"http://localhost:8000/radio.mp3","url":"",
            "public_player_url":"http://localhost/public/my_radio","playlist_pls_url":"http://localhost/public/my_radio/playlist.pls",
            "playlist_m3u_url":"http://localhost/public/my_radio/playlist.m3u","is_public":True,
            "mounts":[{"id":1,"name":"/radio.mp3 (128kbps MP3)","url":"http://localhost:8000/radio.mp3",
                       "bitrate":128,"format":"mp3","listeners":{"total":0,"unique":0,"current":0},
                       "path":"/radio.mp3","is_default":True}],"remotes":[],"hls_enabled":False,
            "hls_is_default":False,"hls_url":None,"hls_listeners":0}
        
        result = self.client.station(1)
        self.assertIsInstance(result, Station)

    def test_stations_returns_list_of_station(self):
        self.client._request_handler.get.return_value = [
            {
                "id":1,"name":"my radio","shortcode":"my_radio","description":"","frontend":"icecast",
                "backend":"liquidsoap","listen_url":"http://localhost:8000/radio.mp3","url":"",
                "public_player_url":"http://localhost/public/my_radio","playlist_pls_url":"http://localhost/public/my_radio/playlist.pls",
                "playlist_m3u_url":"http://localhost/public/my_radio/playlist.m3u","is_public":True,
                "mounts":[{"id":1,"name":"/radio.mp3 (128kbps MP3)","url":"http://localhost:8000/radio.mp3",
                        "bitrate":128,"format":"mp3","listeners":{"total":0,"unique":0,"current":0},
                        "path":"/radio.mp3","is_default":True}],"remotes":[],"hls_enabled":False,
                "hls_is_default":False,"hls_url":None,"hls_listeners":0
            },
            {
                "id":1,"name":"my radio","shortcode":"my_radio","description":"","frontend":"icecast",
                "backend":"liquidsoap","listen_url":"http://localhost:8000/radio.mp3","url":"",
                "public_player_url":"http://localhost/public/my_radio","playlist_pls_url":"http://localhost/public/my_radio/playlist.pls",
                "playlist_m3u_url":"http://localhost/public/my_radio/playlist.m3u","is_public":True,
                "mounts":[{"id":1,"name":"/radio.mp3 (128kbps MP3)","url":"http://localhost:8000/radio.mp3",
                        "bitrate":128,"format":"mp3","listeners":{"total":0,"unique":0,"current":0},
                        "path":"/radio.mp3","is_default":True}],"remotes":[],"hls_enabled":False,
                "hls_is_default":False,"hls_url":None,"hls_listeners":0
            }
        ]
        
        result = self.client.stations()
        self.assertIsInstance(result, list)

        for item in result:
            self.assertIsInstance(item, Station)

if __name__ == '__main__':
    unittest.main()