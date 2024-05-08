Keyword Arguments to :class:`.AzuracastClient`
==============================================

If you prefer to explicitly pass the configuration information into the
:class:`.AzuracastClient` class, then the code below would be used:

.. code-block:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        radio_url="public_radio_url",
        x_api_key="api_key"
    )

This configuration method has lower priority than the :doc:`ini` method.