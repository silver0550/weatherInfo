import json
from datetime import datetime,timedelta

class Cache:

    _cacheFileName = '\cache.json'
    _cacheFilePath = 'App\Cache'
    _data = {}

    def __init__(self) -> None:
        try: 
            file = open(self._cacheFilePath + self._cacheFileName,"r")
            self.data = json.load(file)
        except:
            file = open(self._cacheFilePath + self._cacheFileName,"w")

        file.close()

    def cacheAble(self, city):
               
        if city in self.data and self.data[city]['time'] > (datetime.now() + timedelta(minutes=-20)).strftime('%Y.%m.%d %H:%M'): return True 

        return False
    
    def store(self, city, data):

        self.data[city] = data

        with open(self._cacheFilePath + self._cacheFileName, 'w') as json_file:
            json.dump(self.data, json_file)

    def get(self, city):

        if city in self.data:
            return self.data[city]
        return None
         
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, data):
        self._data = data
        
if "__main__" == __name__:
    test = Cache()
    print(test.cacheAble('Sopron'))
    test.store("Sopron", {
                "time":"2023.07.17 19:40",
                "data":{
                    "2023.07.12 12:10":"0",
                    "2023.07.12 12:11":"0",
                    "2023.07.12 12:12":"0"
                    }
            })
    print(test.get('Sopron'))