# Importing Libraries.
import requests
import json
# func
def Status(lon, lat):
    # Requests Constants.
    API_Key = "77df8ee93034bedcbe6b96b0f9eb9f0a"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={API_Key}"
    # Sending Req.
    response = requests.get(url)
    # Get The Response With Json Format
    res = response.json()
    print(res)

    if res["cod"] != "404":
        data = res['main']
        live_wind_speed = data["current"]["wind_speed"]
        live_pressure = data["current"]["pressure"]
        live_wind_degree = data["current"]["wind_deg"]
        return (live_wind_speed, live_wind_degree, live_pressure)
    else:
        return "Error While Fetching The Response Of API Request."
