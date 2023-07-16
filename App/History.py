import pandas as pd
from datetime import datetime

class History:

    _separate = ';'
    _logFileName = 'history.csv'
    _logFilePath = ''

    def __init__(self) -> None:
        while True:
            try:
                self._history = open(self._logFilePath + self._logFileName, "a+") 
                break                             
            except IOError:
                input('A {} meg van nyitva, kérem zárja be, és nyomjon meg egy gombot!'.format(self._logFilePath + self._logFileName))

    def save(self, city, data):
    # get data from separator

        print('{};{}'.format(city, datetime.now().strftime('%Y.%m.%d %H:%M')), file = self._history)
        self._history.close()

        pd.DataFrame(data).to_csv(self._logFilePath + self._logFileName, sep=self._separate, mode='a',)

        

if __name__ == "__main__":
    data = [{'dt': 1689413100, 'precipitation': 1}, {'dt': 1689413160, 'precipitation': 2}, {'dt': 1689413220, 'precipitation': 3}, {'dt': 1689413280, 'precipitation': 4}, {'dt': 1689413340, 'precipitation': 0}, {'dt': 1689413400, 'precipitation': 0}, {'dt': 1689413460, 'precipitation': 0}, {'dt': 1689413520, 'precipitation': 0}, {'dt': 1689413580, 'precipitation': 0}, {'dt': 1689413640, 'precipitation': 0}, {'dt': 1689413700, 'precipitation': 0}, {'dt': 1689413760, 'precipitation': 0}, {'dt': 1689413820, 'precipitation': 0}, {'dt': 1689413880, 'precipitation': 0}, {'dt': 1689413940, 'precipitation': 0}, {'dt': 1689414000, 'precipitation': 0}, {'dt': 1689414060, 'precipitation': 0}, {'dt': 1689414120, 'precipitation': 0}, {'dt': 1689414180, 'precipitation': 0}, {'dt': 1689414240, 'precipitation': 0}, {'dt': 1689414300, 'precipitation': 0}, {'dt': 1689414360, 'precipitation': 0}, {'dt': 1689414420, 'precipitation': 0}, {'dt': 1689414480, 'precipitation': 0}, {'dt': 1689414540, 'precipitation': 0}, {'dt': 1689414600, 'precipitation': 0}, {'dt': 1689414660, 'precipitation': 0}, {'dt': 1689414720, 'precipitation': 0}, {'dt': 1689414780, 'precipitation': 0}, {'dt': 1689414840, 'precipitation': 0}, {'dt': 1689414900, 'precipitation': 0}, {'dt': 1689414960, 'precipitation': 0}, {'dt': 1689415020, 'precipitation': 0}, {'dt': 1689415080, 'precipitation': 0}, {'dt': 1689415140, 'precipitation': 0}, {'dt': 1689415200, 'precipitation': 0}, {'dt': 1689415260, 'precipitation': 0}, {'dt': 1689415320, 'precipitation': 0}, {'dt': 1689415380, 'precipitation': 0}, {'dt': 1689415440, 'precipitation': 0}, {'dt': 1689415500, 'precipitation': 0}, {'dt': 1689415560, 'precipitation': 0}, {'dt': 1689415620, 'precipitation': 0}, {'dt': 1689415680, 'precipitation': 0}, {'dt': 1689415740, 'precipitation': 0}, {'dt': 1689415800, 'precipitation': 0}, {'dt': 1689415860, 'precipitation': 0}, {'dt': 1689415920, 'precipitation': 0}, {'dt': 1689415980, 'precipitation': 0}, {'dt': 1689416040, 'precipitation': 0}, {'dt': 1689416100, 'precipitation': 0}, {'dt': 1689416160, 'precipitation': 0}, {'dt': 1689416220, 'precipitation': 0}, {'dt': 1689416280, 'precipitation': 0}, {'dt': 1689416340, 'precipitation': 0}, {'dt': 1689416400, 'precipitation': 0}, {'dt': 1689416460, 'precipitation': 0}, {'dt': 1689416520, 'precipitation': 0}, {'dt': 1689416580, 'precipitation': 0}, {'dt': 1689416640, 'precipitation': 0}, {'dt': 1689416700, 'precipitation': 0}]

    test = History().save('Budapest', data)