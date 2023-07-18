import requests

class Weather():
    """ 
        Retrieval of meteorological data from openweathermap.org
        input: API key (str)
    """

    _city = ''
    _lat = ''
    _lon = ''


    def __init__(self, key: str) -> None:
        self.key = key
        self.baseUrl = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily&appid={}'  


    @staticmethod
    def new():

        return Weather('64ed378cc95212fea2574bebbf7ff4de') # My default API key
    

    def _setCoords(self):
        
        request = requests.get ('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(self.city, self.key))

        if request.status_code != 200: raise Exception (request.json()["message"])

        request = request.json()

        self.lon = request['coord']['lon']
        self.lat = request['coord']['lat']


    def of(self, city: str ) :

        self.city = city
        return self
    
    
    def getData(self):

        self._setCoords()

        request = requests.get(self.baseUrl.format(self.lat, self.lon, self.key))

        if request.status_code != 200: raise Exception (request.json()["message"])

        return request.json()
    
    
    def getPrecipitations(self) -> list:
        """ Return the percipitations data"""

        return self.getData()['minutely']


    # Propertys

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, key):
        if len(key) == 32: self._key = key
        else: raise ValueError('Wrong Key')

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def lat(self):
        return self._lat
    @lat.setter
    def lat(self,lat):
        self._lat = lat

    @property
    def lon(self):
        return self._lon
    @lon.setter
    def lon(self, lon):
        self._lon = lon




if "__main__" == __name__ :
    pass