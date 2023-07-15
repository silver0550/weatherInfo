from Api.Weather import Weather

def main():
    city = input('Kérem a város nevét: ')

    precipitations = Weather.new().of(city).getPrecipitations()

    return precipitations

print(main())