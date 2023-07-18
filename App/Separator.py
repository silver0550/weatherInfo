import numpy as np
from datetime import datetime
import pytz

class Separator:

    _divisor = 4
    _timeZone = 'Europe/Budapest'

    def __init__(self, data: list) -> None:

        self.data = data


    def get(self):
                
        precipitations = {self._convertUtcToRealTime(i['dt']) : i['precipitation'] for i in self.data}

        return precipitations


    def _convertUtcToRealTime(self, utc):

        time = datetime.utcfromtimestamp(utc)
        localTime = time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(self._timeZone))

        return localTime.strftime('%Y.%m.%d %H:%M')


    def __str__(self) -> str:

        separated = np.array_split(list(self.get().items()), 4)

        result = 'A várható csapadék mennyisége a következő órában \n'

        for n, i in enumerate(separated):
            result += '{}. negyed\n'.format( n + 1 )
            for j in i:
                result += '\t{} : {}\n'.format(j[0],j[1])
        return result 


    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data: list):
        self._data = data
