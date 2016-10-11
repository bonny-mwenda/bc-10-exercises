import requests


def get_weather():
    """Get weather forecast from OpenWeatherMap"""

    # Send a GET request
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?id=192950&APPID=cc014ad6c4c7e0077ab2617434b2eabe")

    if response.status_code != 200:
        raise Exception(
            "API error. Response status: {}".format(response.status_code))
    else:
        return response.json()
