from Api.Weather import Weather
from App.Separator import Separator
from App.History import History
from App.Cache import cacheAble, getFromCache, store, printFromCache

def main() -> None:
    city = input('Kérem a város nevét: ').lower().capitalize()

    if cacheAble(city):    
        
        print(printFromCache(city))

        separated = getFromCache(city)
        
    else:
        precipitations = Weather.new().of(city).getPrecipitations()
    
        separated = Separator(precipitations).get()

        print(Separator(precipitations))

    store(city, separated)

    History().save(city, separated)

    

main()