from Api.Weather import Weather
from App.Separator import Separator
from App.History import History
from App.Cache import Cache

def main():
    city = input('Kérem a város nevét: ')

    # if Cache().cacheAble(city): return True

    precipitations = Weather.new().of(city).getPrecipitations()
    
    separated = Separator(precipitations).get()
    # print(separated)

    History().save(city, separated)

    print(Separator(precipitations))
    

    return precipitations

main()