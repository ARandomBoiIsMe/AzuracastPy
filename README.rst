AzuracastPy: The Unofficial Python Wrapper for the Azuracast API
================================================================

AzuracastPy is a Python package that allows for straightforward access
to `AzuraCast <https://www.azuracast.com/>`_'s API.

Installation
------------

AzuracastPy can be installed using `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: console

    pip install AzuracastPy

Quickstart
----------

With the url of a radio hosted on AzuraCast, an instance of the AzuracastClient
class can be created like so (`An API Key <https://www.azuracast.com/docs/developers/apis/>`_
is needed for more sensitive requests):

.. code-block:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        radio_url="radio_url",
        api_key="(Optional) api_key"
    )

With this instance, radio stations can be interacted with and queried:

.. code-block:: python

    # Get all stations served from the hosted radio.
    stations = client.stations()
    print(stations)

    # Get data of a specific station.
    station = client.station(1)
    print(station.name, station.description, station.requestable_songs())

    # Create a podcast on a station (API Key required).
    from AzuracastPy.enums import Languages, PodcastCategories

    station = client.station(1)

    new_podcast = station.podcast.create(
        title="New podcast",
        description="This is a random description",
        language=Languages.ARABIC,
        categories=[
            PodcastCategories.Arts.DESIGN,
            PodcastCategories.Comedy.COMEDY_INTERVIEWS
        ]
    )

Documentation
-------------

AzuracastPy's documentation is located at https://praw.readthedocs.io/.