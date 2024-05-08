Requesting a Song From a Station
================================

As an example scenario, let's assume you want to request a song from your favorite online radio station.

.. note::

    You won't need an X-API-Key here, because this is a public action that anyone can perform.

For this example, `AzuraCast's demo radio <https://www.azuracast.com/docs/live-demo/>`_ will be used.

The radio lives on ``https://demo.azuracast.com/``. This is the radio url we will use
when initializing :class:`.AzuracastClient`:

.. code-block:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        radio_url="https://demo.azuracast.com/"
    )

Using the client object, we can query the radio for all its hosted stations:

.. code-block:: python

    stations = client.stations()

We can then either get a station by retrieving it from the station list:

.. code-block:: python

    station = stations[0]

or we can get it directly from its ``id``:

.. code-block:: python

    station = client.station(1)

.. note::

    Make sure the station with that ``id`` actually exists before trying to
    fetch it, or an error will be thrown.

Now that we have the station, we can query it for the songs that are available to be requested:

.. code-block:: python

    requestable_songs = station.requestable_songs()

We can now move through this list and request a song if it matches a certain condition, while
making sure to catch any errors we might experience:

.. code-block:: python

    for rs in requestable_songs:
        if rs.song.title == 'Press Start':
            try:
                station.request_song(rs.request_id)
                print("Song requested.")
            except:
                print("Error requesting song.")

            break

The code above will carry out the task of requesting a specific song from a radio station.

The complete code is shown below:

.. code:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        radio_url="https://demo.azuracast.com/"
    )

    station = client.station(1)

    requestable_songs = station.requestable_songs()

    for rs in requestable_songs:
        if rs.song.title == 'Press Start':
            try:
                station.request_song(rs.request_id)
                print("Song requested.")
            except:
                print("Error requesting song.")

            break