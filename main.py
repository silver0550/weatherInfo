from Api.Weather import Weather
from App.Separator import Separator
from App.History import History

def main():
    city = input('Kérem a város nevét: ')

    precipitations = Weather.new().of(city).getPrecipitations()
    
    separated = Separator(precipitations).get()

    History().save(city, separated)

    print(Separator(precipitations))
    

    return precipitations

main()