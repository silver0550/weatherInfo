from Api.Weather import Weather
from App.Separator import Separator

def main():
    city = input('Kérem a város nevét: ')

    precipitations = Weather.new().of(city).getPrecipitations()

    Separator(precipitations).showResult()

    return precipitations

main()