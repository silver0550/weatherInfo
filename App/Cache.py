import json
import os.path
import numpy as np

from datetime import datetime,timedelta


def fileCheck() -> bool:
        if not os.path.isfile('App\Cache\cache.json'): 
            open('App\Cache\cache.json',"w").close()
            return False


def cacheAble(city) ->bool:
    
    fileCheck()
    try:
        file = open('App\Cache\cache.json',)
        jsonData = json.load(file)
        file.close()
    except:
        return False
    
    if city in jsonData and jsonData[city]['time'] > (datetime.now() + timedelta(minutes=-20)).strftime('%Y.%m.%d %H:%M'): return True 

    return False

def store(city, data):

    try:
        with open('App\Cache\cache.json' ) as json_file:
            jsonData = json.load(json_file)
    except:
         jsonData ={} 
    
    jsonData[city] = {"time" : datetime.now().strftime('%Y.%m.%d %H:%M'), "data" : data}

    json_file.close()

    with open('App\Cache\cache.json' , 'w') as json_file:
        json.dump(jsonData, json_file)

    json_file.close()

def getFromCache(city) -> None:
     
    with open('App\Cache\cache.json' ) as json_file:
        jsonData = json.load(json_file)

    result = 'A várható csapadék mennyisége a következő órában \n'

    data = jsonData[city]["data"]

    
    for n, i in enumerate(np.array_split(list(data.items()),4)):
        result +=  '{}.negyed\n'.format(n+1) 
        for j in i:
            result += '\t{} : {}\n'.format(j[0],j[1])


    return result



# class Cache:

#     _cacheFileName = 'App\Cache\cache.json'
#     _data = {}

#     def __init__(self) -> None:
#         try: 
#             file = open( self._cacheFileName,"r")
#             self.data = json.load(file)
#         except:
#             file = open(self._cacheFileName,"w")

#         file.close()
#     @staticmethod
#     def fileCheck(path) -> bool:
#         return os.path.isfile(path)
    
    
#     def cacheAble(self, city):

#         if Cache.fileCheck(self._cacheFileName):           
#             if city in self.data and self.data[city]['time'] > (datetime.now() + timedelta(minutes=-20)).strftime('%Y.%m.%d %H:%M'): return True 

#         return False
    
#     def store(self, city, data):

#         self.data[city] = data

#         with open( self._cacheFileName, 'w') as json_file:
#             json.dump(self.data, json_file)

#     def get(self, city):

#         if city in self.data:
#             return self.data[city]
#         return None
         
    
#     @property
#     def data(self):
#         return self._data
#     @data.setter
#     def data(self, data):
#         self._data = data
        
if "__main__" == __name__:
    pass