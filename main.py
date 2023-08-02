import json

MOCK_JSON_DATA = '''
{
    "list": [
        {
            "dt_txt": "2023-08-02 12:00:00",
            "main": {
                "temp": 289.51,
                "pressure": 1014
            },
            "wind": {
                "speed": 3.92
            }
        },
        {
            "dt_txt": "2023-08-02 15:00:00",
            "main": {
                "temp": 291.79,
                "pressure": 1015
            },
            "wind": {
                "speed": 4.57
            }
        }
    ]
}
'''

def get_weather_data():
    return json.loads(MOCK_JSON_DATA)

def get_weather_by_date(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["main"]["temp"]
    return None

def get_wind_speed_by_date(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["wind"]["speed"]
    return None

def get_pressure_by_date(weather_data, date):
    for item in weather_data["list"]:
        if item["dt_txt"] == date:
            return item["main"]["pressure"]
    return None

def main():
    weather_data = get_weather_data()

    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temp = get_weather_by_date(weather_data, date)
            if temp is not None:
                print(f"The temperature at {date} is {temp} Kelvin.")
            else:
                print("Weather data not available for the given date.")
        elif choice == 2:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"The wind speed at {date} is {wind_speed} m/s.")
            else:
                print("Wind speed data not available for the given date.")
        elif choice == 3:
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"The pressure at {date} is {pressure} hPa.")
            else:
                print("Pressure data not available for the given date.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
