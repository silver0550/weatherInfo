import pandas as pd
from datetime import datetime

class History:

    _logFileName = 'history.csv'
    

    def __init__(self) -> None:
        while True:
            try:
                self._history = open( self._logFileName, "a+") 
                break                             
            except IOError:
                input('A {} meg van nyitva, kérem zárja be, és nyomjon meg egy gombot!'.format( self._logFileName))

    def save(self, city, data):

        print('{};{}'.format(city, datetime.now().strftime('%Y.%m.%d %H:%M')), file = self._history)
        self._history.close()
        
        pd.DataFrame( data, index=[0]).to_csv(self._logFileName, sep=';', mode='a')

        
if __name__ == "__main__":
    pass