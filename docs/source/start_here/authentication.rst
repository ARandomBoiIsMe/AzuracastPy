Authentication via API Key
==========================

While AzuraCast does provide some endpoints that can be accessed by the general
public, a huge majority of the API routes can only be used with proper
authentication.

This authentication comes in the form of an API Key, which can be generated from
your profile on the AzuraCast web interface.

`Read the 'API Authentication' section
for instructions on how to generate your API Key <https://www.azuracast.com/docs/developers/apis/>`_.

This generated key can then be used to authenticate yourself when initializing :class:`.AzuracastClient`,
allowing you to make sensitive requests. Read the :doc:`configuration` page for more info on this.