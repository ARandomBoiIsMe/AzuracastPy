Getting The Current Song On A Radio
===================================

A song is currently playing on the radio, and you want to know what it is.
Here's how you can do that.

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

Using the client object, we can get a list of all the currently playing songs across
all the stations on the radio:

.. code-block:: python

    current_songs = client.now_playing()

We can then either get the currently playing song of a station by retrieving it from the
returned list:

.. code-block:: python

    current_song = current_songs[0]

or we can get it directly by passing the stations's ``id`` into the
:meth:`~.AzuracastClient.now_playing` function:

.. code-block:: python

    current_song = client.now_playing(1)

.. note::

    Make sure the station with that ``id`` actually exists before trying to
    fetch it, or an error will be thrown.

Now that we have the song, we can extract its various details:

.. code-block:: python

    print(
        f"Artist: {current_song.now_playing.song.artist}\n"\
        f"Title: {current_song.now_playing.song.title}\n"\
        f"Album: {current_song.now_playing.song.album}"
    )

The code above will carry out the task of getting the currently playing
song from a radio station.

The complete code is shown below:

.. code:: python

    from AzuracastPy import AzuracastClient

    client = AzuracastClient(
        radio_url="https://demo.azuracast.com/"
    )

    current_song = client.now_playing(1)

    print(
        f"Artist: {current_song.now_playing.song.artist}\n"\
        f"Title: {current_song.now_playing.song.title}\n"\
        f"Album: {current_song.now_playing.song.album}"
    )