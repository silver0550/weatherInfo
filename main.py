from Api.Weather import Weather
from App.Separator import Separator
from App.History import History
from App.Cache import cacheAble, getFromCache, store

def main() -> None:
    city = input('Kérem a város nevét: ').lower().capitalize()

    if cacheAble(city):    
        print(getFromCache(city))

    precipitations = Weather.new().of(city).getPrecipitations()
    
    separated = Separator(precipitations).get()

    store(city, separated)

    History().save(city, separated)

    print(Separator(precipitations))
    


main()