import json
import os.path
import numpy as np

from datetime import datetime,timedelta


def fileCheck() -> bool:
        
        if not os.path.isfile('App\cache.json'): 
            open('App\cache.json',"w").close()
            return False


def cacheAble(city) ->bool:
    
    fileCheck()

    try:
        file = open('App\cache.json',)
        jsonData = json.load(file)
        file.close()
    except:
        return False
    
    if city in jsonData and jsonData[city]['time'] > (datetime.now() + timedelta(minutes=-20)).strftime('%Y.%m.%d %H:%M'): return True 

    return False


def store(city, data):

    try:
        with open('App\cache.json' ) as json_file:
            jsonData = json.load(json_file)
    except:
         jsonData ={} 
    
    jsonData[city] = {"time" : datetime.now().strftime('%Y.%m.%d %H:%M'), "data" : data}

    json_file.close()

    with open('App\cache.json' , 'w') as json_file:
        json.dump(jsonData, json_file)

    json_file.close()


def getFromCache(city):

    with open('App\cache.json' ) as json_file:
        jsonData = json.load(json_file)

    return jsonData[city]["data"]

def printFromCache(city):
    
    with open('App\cache.json' ) as json_file:
        jsonData = json.load(json_file)

    result = 'A várható csapadék mennyisége a következő órában \n'

    data = jsonData[city]["data"]

    
    for n, i in enumerate(np.array_split(list(data.items()),4)):
        result +=  '{}.negyed\n'.format(n+1) 
        for j in i:
            result += '\t{} : {}\n'.format(j[0],j[1])

    print (result)
