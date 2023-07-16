import numpy as np
from datetime import datetime
import pytz

class Separator:

    _divisor = 4
    _timeZone = 'Europe/Budapest'

    def __init__(self, data: list) -> None:

        self.data = data


    def get(self):

        precipitations = np.array([{'dt': self._convertUtcToRealTime(i['dt']),'precipitation': i['precipitation']} for i in self.data])

        precipitations = np.array_split(precipitations, self._divisor)
     
        return precipitations


    def showResult(self): #TODO: __str__

        print('A várható csapadék mennyisége a következő órában 1/{} órás felosztásban '.format(self._divisor))
        
        for n, i in enumerate(self.get()):
            print( '{}. negyed'.format( n + 1 ))
            for j in i:
                print('{}-kor: {}'.format(j['dt'], j['precipitation']))


    def _convertUtcToRealTime(self, utc):

        time = datetime.utcfromtimestamp(utc)
        localTime = time.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(self._timeZone))

        return localTime.strftime('%Y.%m.%d %H:%M')

    def __str__(self) -> str:

        result = 'A várható csapadék mennyisége a következő órában 1/{} órás felosztásban\n'.format(self._divisor)

        for n, i in enumerate(self.get()):
            result += '{}. negyed\n'.format( n + 1 )
            for j in i:
                result += '\t{}-kor: {}\n'.format(j['dt'], j['precipitation'])
        return result 

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data: list):
        #TODO: test input
        self._data = data
    
if "__main__" == __name__:

    
    
    test= Separator([{'dt': 1689413100, 'precipitation': 1}, {'dt': 1689413160, 'precipitation': 2}, {'dt': 1689413220, 'precipitation': 3}, {'dt': 1689413280, 'precipitation': 4}, {'dt': 1689413340, 'precipitation': 0}, {'dt': 1689413400, 'precipitation': 0}, {'dt': 1689413460, 'precipitation': 0}, {'dt': 1689413520, 'precipitation': 0}, {'dt': 1689413580, 'precipitation': 0}, {'dt': 1689413640, 'precipitation': 0}, {'dt': 1689413700, 'precipitation': 0}, {'dt': 1689413760, 'precipitation': 0}, {'dt': 1689413820, 'precipitation': 0}, {'dt': 1689413880, 'precipitation': 0}, {'dt': 1689413940, 'precipitation': 0}, {'dt': 1689414000, 'precipitation': 0}, {'dt': 1689414060, 'precipitation': 0}, {'dt': 1689414120, 'precipitation': 0}, {'dt': 1689414180, 'precipitation': 0}, {'dt': 1689414240, 'precipitation': 0}, {'dt': 1689414300, 'precipitation': 0}, {'dt': 1689414360, 'precipitation': 0}, {'dt': 1689414420, 'precipitation': 0}, {'dt': 1689414480, 'precipitation': 0}, {'dt': 1689414540, 'precipitation': 0}, {'dt': 1689414600, 'precipitation': 0}, {'dt': 1689414660, 'precipitation': 0}, {'dt': 1689414720, 'precipitation': 0}, {'dt': 1689414780, 'precipitation': 0}, {'dt': 1689414840, 'precipitation': 0}, {'dt': 1689414900, 'precipitation': 0}, {'dt': 1689414960, 'precipitation': 0}, {'dt': 1689415020, 'precipitation': 0}, {'dt': 1689415080, 'precipitation': 0}, {'dt': 1689415140, 'precipitation': 0}, {'dt': 1689415200, 'precipitation': 0}, {'dt': 1689415260, 'precipitation': 0}, {'dt': 1689415320, 'precipitation': 0}, {'dt': 1689415380, 'precipitation': 0}, {'dt': 1689415440, 'precipitation': 0}, {'dt': 1689415500, 'precipitation': 0}, {'dt': 1689415560, 'precipitation': 0}, {'dt': 1689415620, 'precipitation': 0}, {'dt': 1689415680, 'precipitation': 0}, {'dt': 1689415740, 'precipitation': 0}, {'dt': 1689415800, 'precipitation': 0}, {'dt': 1689415860, 'precipitation': 0}, {'dt': 1689415920, 'precipitation': 0}, {'dt': 1689415980, 'precipitation': 0}, {'dt': 1689416040, 'precipitation': 0}, {'dt': 1689416100, 'precipitation': 0}, {'dt': 1689416160, 'precipitation': 0}, {'dt': 1689416220, 'precipitation': 0}, {'dt': 1689416280, 'precipitation': 0}, {'dt': 1689416340, 'precipitation': 0}, {'dt': 1689416400, 'precipitation': 0}, {'dt': 1689416460, 'precipitation': 0}, {'dt': 1689416520, 'precipitation': 0}, {'dt': 1689416580, 'precipitation': 0}, {'dt': 1689416640, 'precipitation': 0}, {'dt': 1689416700, 'precipitation': 0}])
    
    print(test.get())