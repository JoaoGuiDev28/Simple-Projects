class Bottle:
    __slots__ = ['_capacity', '_volume']

    def __init__(self, capacity, volume):
        self._capacity = capacity if isinstance(capacity, float) else None
        self._volume = volume if isinstance(volume, float) else None
        if capacity < 0:
            raise ValueError('Capacity must be greater than zero!')

    def __str__(self):
        return f'Bottle Capacity, in ml: {self._capacity} | Bottle Volume: {self._volume}'

    @property
    def capacity(self):
        return self._capacity

    @property
    def volume(self):
        return self._volume

    def Fill(self, poe):
        if poe < 0:
            raise ValueError('Error! Amount to be added cannot be negative.')
        if (self._volume + poe) > self._capacity:
            raise ValueError('The new volume exceeds the bottle's capacity.')
        else:
            self._volume += poe

    def Dump(self, remove):
        if remove < 0:
            raise ValueError('The value to be removed cannot be negative.')
        if remove > self._volume:
            raise ValueError('Error! Amount to be removed cannot be greater than what is already present.')
        else:
            self._volume -= remove

try:
    c = float(input('Enter the capacity of the Bottle, in ml: '))
    v = float(input('Enter the volume of the Bottle: '))
    m = Bottle(c, v)
    m.Fill(200)
    #m.Dump(200)
    print(m)

except Exception as e:
    print('\n',e)