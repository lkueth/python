min_volume = 0
max_volume = 2
min_channel = 0
max_channel = 3

class Television:
    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = min_volume
        self._channel = min_channel

    def power(self):
        if not self._status:
            self._status = True
        elif self._status:
            self._status = False

    def mute(self):
        if self._status:
            if self._muted == False:
                self._muted = True
            elif self._muted == True:
                self._muted = False

    def channel_up(self):
        if self._status:
            self._channel += 1
            if self._channel > max_channel:
                self._channel = min_channel


    def channel_down(self):
        if self._status:
            self._channel -= 1
            if self._channel < min_channel:
                self._channel = max_channel


    def volume_up(self):
        self._muted = False
        if self._status:
            if not self._volume == max_volume:
                self._volume += 1

    def volume_down(self):
        self._muted = False
        if self._status:
            if not self._volume == min_volume:
                self._volume -= 1

    def __str__(self):
        if not self._muted:
            return f'Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}.'
        else:
            return f'Power = {self._status}, Channel = {self._channel}, Volume = 0.'






