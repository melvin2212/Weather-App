
import requests, json

api_key = "6b2d7c489fcdb0e84d27fd48ce4b8c0b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter city name : ")


complete_url = base_url + "appid=" + api_key + "&q=" + city_name


response = requests.get(complete_url)


x = response.json()

if x["cod"] != "404":

    y = x["main"]

   
    current_temperature = y["temp"]
    current_humidiy = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature (kelvin) =  " +
                    str(current_temperature) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))

else:
    print(" This city was not found ")
