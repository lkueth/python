
min_volume = 0
max_volume = 2
min_channel = 0
max_channel = 3
"""
Global variables for max and min channel/volume values
"""

class Television:
    """
    Creates class called "Television"
    This will be the logic for main.py
    """
    def __init__(self) -> None:
        self._status = False
        self._muted = False
        self._volume = min_volume
        self._channel = min_channel

    """
    Initializes itself and variables such as:
    Status: If television is off or on, starts turned on
    Muted: If television is muted or un-muted, starts un-muted
    Volume: Television volume starts at 0
    Channel: Television channel starts at 0
    """

    def power(self) -> None:
        if not self._status:
            self._status = True
        elif self._status:
            self._status = False
    """
    Powers on or off the television   
    """

    def mute(self) -> None:
        if self._status:
            if self._muted == False:
                self._muted = True
            elif self._muted == True:
                self._muted = False
    """
    If the television is on, this mutes and un-mutes the television.
    """

    def channel_up(self) -> None:
        if self._status:
            self._channel += 1
            if self._channel > max_channel:
                self._channel = min_channel
    """
    If the television is on, the channel changes by increasing its value.
    """


    def channel_down(self) -> None:
        if self._status:
            self._channel -= 1
            if self._channel < min_channel:
                self._channel = max_channel
    """
    If the television is on, the channel changes by decreasing its value.
    """


    def volume_up(self) -> None:
        self._muted = False
        if self._status:
            if not self._volume == max_volume:
                self._volume += 1

    """
    If the television is on,
    the volume changes by increasing its value and un-mutes the television.
    """

    def volume_down(self) -> None:
        self._muted = False
        if self._status:
            if not self._volume == min_volume:
                self._volume -= 1
    """
    If the television is on, 
    the volume changes by decreasing its value and un-mutes the television.
    """

    def __str__(self) -> str:
        if not self._muted:
            return f'Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}.'
        else:
            return f'Power = {self._status}, Channel = {self._channel}, Volume = 0.'

    """
    If the television is muted or un-muted,
    The values of the status, channel, and volume of the television are printed.
    If it is muted, 0 will be printed for the volume.
    """






