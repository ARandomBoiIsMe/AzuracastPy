from AzuracastPy.models.station import Station

import unittest
from unittest import TestCase, mock

from AzuracastPy import AzuracastClient

from .util import fake_data_generator

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
        id = 1
        self.client._request_handler.get.return_value = fake_data_generator.return_fake_station_json(id)
        
        result = self.client.station(id)

        self.assertIsInstance(result, Station)

    def test_stations_returns_list_of_station(self):
        self.client._request_handler.get.return_value = [
            fake_data_generator.return_fake_station_json(1),
            fake_data_generator.return_fake_station_json(2),
            fake_data_generator.return_fake_station_json(19)
        ]
        
        result = self.client.stations()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, Station)

if __name__ == '__main__':
    unittest.main()