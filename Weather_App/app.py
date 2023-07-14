import requests


def get_weather_data(city):
    key = "0a660178c203eb12052ed7e8749ffefe"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}"
    response = requests.get(url)
    return response.json()


def display_weather_info(city, weather, temperature, feels_like):
    print(f"Weather in {city} today:")
    print(f"Condition: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")


def get_city_weather():
    city = input("Enter City: ")
    data = get_weather_data(city)

    if data['cod'] == '404':
        print(f"Sorry, {city} not found...")
    else:
        weather = data['weather'][0]['main']
        temperature = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        display_weather_info(city, weather, temperature, feels_like)


if __name__ == '__main__':
    get_city_weather()
