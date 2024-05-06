from AzuracastPy import models

import unittest
from unittest import TestCase, mock
from requests import Response

from AzuracastPy.enums import GlobalPermissions, StationPermissions, AutoAssignValues

from .util import fake_data_generator

class TestStation(TestCase):
    def setUp(self) -> None:
        self.admin = fake_data_generator.return_fake_admin_instance()
        self.admin._request_handler = mock.MagicMock()
        self.response = Response()

    def test_station_returns_admin_station(self):
        response = fake_data_generator.return_fake_admin_station_json()

        self.admin._request_handler.get.return_value = response

        result = self.admin.station(1)

        self.assertIsInstance(result, models.administration.AdminStation)
        self.assertIsInstance(result.frontend_config, models.administration.admin_station.FrontendConfig)
        self.assertIsInstance(result.backend_config, models.administration.admin_station.BackendConfig)

    def test_stations_returns_admin_stations(self):
        response = [
            fake_data_generator.return_fake_admin_station_json(),
            fake_data_generator.return_fake_admin_station_json()
        ]
        self.admin._request_handler.get.return_value = response

        result = self.admin.stations()

        self.assertEqual(len(result), 2)
        for station in result:
            self.assertIsInstance(station, models.administration.AdminStation)
            self.assertIsInstance(station.frontend_config, models.administration.admin_station.FrontendConfig)
            self.assertIsInstance(station.backend_config, models.administration.admin_station.BackendConfig)

    def test_role_creation(self):
        self.admin._request_handler.post.return_value = fake_data_generator.return_fake_role_json()
        self.admin._request_handler.post.return_value['name'] = "New role"
        self.admin._request_handler.post.return_value['permissions']['global'] = [
            "view administration",
            "view system logs"
        ]
        self.admin._request_handler.post.return_value['permissions']['station'] = {
            "1": [
                "manage station automation",
                "manage station media"
            ]
        }

        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_role_json()

        station_permissions = {
            "1": [
                StationPermissions.MANAGE_STATION_AUTOMATION,
                StationPermissions.MANAGE_STATION_MEDIA
            ]
        }

        result = self.admin.role.create(
            name="yo ho",
            global_permissions=[
                GlobalPermissions.VIEW_ADMINISTRATION,
                GlobalPermissions.VIEW_SYSTEM_LOGS
            ],
            station_permissions=station_permissions
        )

        self.assertIsInstance(result, models.administration.Role)
        self.assertIsInstance(result.links, models.administration.role.Links)

        self.assertEqual(result.name, "yo ho")
        self.assertEqual(result.permissions.global_permissions, [
                "view administration",
                "view system logs"
            ]
        )
        self.assertEqual(result.permissions.station_permissions, {
                "1": [
                    "manage station automation",
                    "manage station media"
                ]
            }
        )

    def test_role_returns_role(self):
        id = 1
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_role_json()

        result = self.admin.role(id)

        self.assertIsInstance(result, models.administration.Role)
        self.assertIsInstance(result.links, models.administration.role.Links)

    def test_roles_returns_list_of_role(self):
        self.admin._request_handler.get.return_value = [
            fake_data_generator.return_fake_role_json(),
            fake_data_generator.return_fake_role_json(),
            fake_data_generator.return_fake_role_json()
        ]

        result = self.admin.roles()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.administration.Role)
            self.assertIsInstance(item.links, models.administration.role.Links)

    def test_custom_field_creation(self):
        self.admin._request_handler.post.return_value = fake_data_generator.return_fake_custom_field_json()

        result = self.admin.custom_field.create(
            name="bro thinks hes funny",
            auto_assign_value=AutoAssignValues.ALBUM
        )

        self.assertIsInstance(result, models.administration.CustomField)
        self.assertIsInstance(result.links, models.administration.custom_field.Links)

        self.assertEqual(result.name, "bro thinks hes funny")
        self.assertEqual(result.short_name, "bro_thinks_hes_funny")
        self.assertEqual(result.auto_assign, "album")

    def test_custom_field_returns_custom_field(self):
        id = 1
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_custom_field_json()

        result = self.admin.custom_field(id)

        self.assertIsInstance(result, models.administration.CustomField)
        self.assertIsInstance(result.links, models.administration.custom_field.Links)

    def test_custom_fields_returns_list_of_custom_field(self):
        self.admin._request_handler.get.return_value = [
            fake_data_generator.return_fake_custom_field_json(),
            fake_data_generator.return_fake_custom_field_json(),
            fake_data_generator.return_fake_custom_field_json()
        ]

        result = self.admin.custom_fields()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.administration.CustomField)
            self.assertIsInstance(item.links, models.administration.custom_field.Links)

    def test_storage_location_returns_storage_location(self):
        id = 1
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_storage_location_json()

        result = self.admin.storage_location(id)

        self.assertIsInstance(result, models.administration.StorageLocation)
        self.assertIsInstance(result.links, models.administration.storage_location.Links)

    def test_storage_locations_returns_list_of_storage_location(self):
        self.admin._request_handler.get.return_value = [
            fake_data_generator.return_fake_storage_location_json(),
            fake_data_generator.return_fake_storage_location_json(),
            fake_data_generator.return_fake_storage_location_json()
        ]

        result = self.admin.storage_locations()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.administration.StorageLocation)
            self.assertIsInstance(item.links, models.administration.storage_location.Links)

    def test_permissions_returns_permissions(self):
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_permissions_json()

        result = self.admin.permissions()

        self.assertIsInstance(result.global_permissions, list)
        for gp in result.global_permissions:
            self.assertIsInstance(gp, dict)

        self.assertIsInstance(result.station_permissions, list)
        for sp in result.station_permissions:
            self.assertIsInstance(sp, dict)

    def test_relays_returns_relays(self):
        self.admin._request_handler.get.return_value = [
            fake_data_generator.return_fake_relay_json(),
            fake_data_generator.return_fake_relay_json(),
            fake_data_generator.return_fake_relay_json()
        ]

        result = self.admin.relays()

        self.assertIsInstance(result, list)
        for item in result:
            self.assertIsInstance(item, models.administration.Relay)

            self.assertIsInstance(item.mounts, list)
            for mount in item.mounts:
                self.assertIsInstance(mount, models.Mount)

    def test_settings_returns_settings(self):
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_settings_json()

        result = self.admin.settings()

        self.assertIsInstance(result, models.administration.Settings)
        self.assertIsInstance(result.update_results, models.administration.settings.UpdateResults)

    def test_cpu_stats_returns_stats(self):
        self.admin._request_handler.get.return_value = fake_data_generator.return_fake_cpu_stats_json()

        result = self.admin.cpu_stats()

        self.assertIsInstance(result, dict)

        self.assertIsNotNone(result.get('cpu'))
        self.assertIsNotNone(result.get('memory'))
        self.assertIsNotNone(result.get('swap'))
        self.assertIsNotNone(result.get('disk'))
        self.assertIsNotNone(result.get('network'))

if __name__ == '__main__':
    unittest.main()