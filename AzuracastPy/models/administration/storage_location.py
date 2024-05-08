from ...util.general_util import generate_repr_string

from .util.admin_resource_operations import delete_admin_resource

from typing import Dict, Any

class Links:
    """Represents the link associated with a storage location."""
    def __init__(
        self_,
        self
    ):
        """
        Initializes a :class:`Links` object for a storage location.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: ``storage_location.links``.
        """
        self_.self = self

    def __repr__(self) -> str:
        return generate_repr_string(self)

class StorageLocation:
    """Represents a storage location on a radio."""
    def __init__(
        self,
        id,
        type,
        adapter,
        path,
        s3_credential_key,
        s3_credential_secret,
        s3_region,
        s3_version,
        s3_bucket,
        s3_endpoint,
        dropbox_app_key,
        dropbox_app_secret,
        dropbox_auth_token,
        sftp_host,
        sftp_username,
        sftp_password,
        sftp_port,
        sftp_private_key,
        sftp_private_key_pass_phrase,
        storage_quota,
        storage_quota_bytes,
        storage_used,
        storage_used_bytes,
        storage_available,
        storage_available_bytes,
        storage_used_percent,
        is_full,
        uri,
        stations,
        links,
        _admin
    ):
        """
        Initializes a :class:`StorageLocation` object.

        .. note::

            This class should not be initialized directly. Instead, obtain an instance
            via: :meth:`~.administration.helpers.StorageLocationHelper.__call__` or
            :meth:`~.Admin.storage_locations`.
        """
        self.id = id
        self.type = type
        self.adapter = adapter
        self.path = path
        self.s3_credential_key = s3_credential_key
        self.s3_credential_secret = s3_credential_secret
        self.s3_region = s3_region
        self.s3_version = s3_version
        self.s3_bucket = s3_bucket
        self.s3_endpoint = s3_endpoint
        self.dropbox_app_key = dropbox_app_key
        self.dropbox_app_secret = dropbox_app_secret
        self.dropbox_auth_token = dropbox_auth_token
        self.sftp_host = sftp_host
        self.sftp_username = sftp_username
        self.sftp_password = sftp_password
        self.sftp_port = sftp_port
        self.sftp_private_key = sftp_private_key
        self.sftp_private_key_pass_phrase = sftp_private_key_pass_phrase
        self.storage_quota = storage_quota
        self.storage_quota_bytes = storage_quota_bytes
        self.storage_used = storage_used
        self.storage_used_bytes = storage_used_bytes
        self.storage_available = storage_available
        self.storage_available_bytes = storage_available_bytes
        self.storage_used_percent = storage_used_percent
        self.is_full = is_full
        self.uri = uri
        self.stations = stations
        self.links = Links(**links)
        self._admin = _admin

    @classmethod
    def from_dict(
        cls,
        storage_location_dict: Dict[str, Any],
        _admin
    ):
        return cls(
            id=storage_location_dict.get("id"),
            type=storage_location_dict.get("type"),
            adapter=storage_location_dict.get("adapter"),
            path=storage_location_dict.get("path"),
            s3_credential_key=storage_location_dict.get("s3CredentialKey"),
            s3_credential_secret=storage_location_dict.get("s3CredentialSecret"),
            s3_region=storage_location_dict.get("s3Region"),
            s3_version=storage_location_dict.get("s3Version"),
            s3_bucket=storage_location_dict.get("s3Bucket"),
            s3_endpoint=storage_location_dict.get("s3Endpoint"),
            dropbox_app_key=storage_location_dict.get("dropboxAppKey"),
            dropbox_app_secret=storage_location_dict.get("dropboxAppSecret"),
            dropbox_auth_token=storage_location_dict.get("dropboxAuthToken"),
            sftp_host=storage_location_dict.get("sftpHost"),
            sftp_username=storage_location_dict.get("sftpUsername"),
            sftp_password=storage_location_dict.get("sftpPassword"),
            sftp_port=storage_location_dict.get("sftpPort"),
            sftp_private_key=storage_location_dict.get("sftpPrivateKey"),
            sftp_private_key_pass_phrase=storage_location_dict.get("sftpPrivateKeyPassPhrase"),
            storage_quota=storage_location_dict.get("storageQuota"),
            storage_quota_bytes=storage_location_dict.get("storageQuotaBytes"),
            storage_used=storage_location_dict.get("storageUsed"),
            storage_used_bytes=storage_location_dict.get("storageUsedBytes"),
            storage_available=storage_location_dict.get("storageAvailable"),
            storage_available_bytes=storage_location_dict.get("storageAvailableBytes"),
            storage_used_percent=storage_location_dict.get("storageUsedPercent"),
            is_full=storage_location_dict.get("isFull"),
            uri=storage_location_dict.get("uri"),
            stations=storage_location_dict.get("stations"),
            links=storage_location_dict.get("links"),
            _admin=_admin
        )

    def __repr__(self) -> str:
        return generate_repr_string(self)

    def delete(self):
        """
        Deletes the storage location from the radio.

        Sets all attributes of the current :class:`StorageLocation` object to ``None``.

        Usage:

        .. code-block:: python

            storage_location.delete()
        """
        return delete_admin_resource(self, "storage_location")

    def _clear_properties(self):
        self.id = None
        self.type = None
        self.adapter = None
        self.path = None
        self.s3_credential_key = None
        self.s3_credential_secret = None
        self.s3_region = None
        self.s3_version = None
        self.s3_bucket = None
        self.s3_endpoint = None
        self.dropbox_app_key = None
        self.dropbox_app_secret = None
        self.dropbox_auth_token = None
        self.sftp_host = None
        self.sftp_username = None
        self.sftp_password = None
        self.sftp_port = None
        self.sftp_private_key = None
        self.sftp_private_key_pass_phrase = None
        self.storage_quota = None
        self.storage_quota_bytes = None
        self.storage_used = None
        self.storage_used_bytes = None
        self.storage_available = None
        self.storage_available_bytes = None
        self.storage_used_percent = None
        self.is_full = None
        self.uri = None
        self.stations = None
        self.links = None
        self._admin = None
