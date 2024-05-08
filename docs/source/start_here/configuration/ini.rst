``*.ini`` files
===============

Files with the ``.ini`` extension can be created and used
to store configuration details for the creation of an
AzuracastClient instance.

Format of ``*.ini`` files
-------------------------

This configuration method uses the `INI file format <https://en.wikipedia.org/wiki/INI_file>`_ to
define settings for the AzuracastClient instance.
For a ``*.ini`` file to be recognized as a valid configuration file, its contents must follow
the following format:

.. code-block:: ini

    [PARAM]
    # The valid public URL of the hosted radio.
    RADIO_URL=public_radio_url

    # Your valid AzuraCast API Key.
    X_API_KEY=api_key

This file can then be used to initialize an :class:`.AzuracastClient` instance like so:

.. code-block:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        config="path/to/file.ini"
    )

This configuration method has higher priority than the :doc:`keyword_args` method.