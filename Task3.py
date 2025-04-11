import requests
import folium
import webbrowser
import os

def get_location():
    response = requests.get('https://ipinfo.io/json')
    data = response.json()
    
    loc = data['loc'].split(',')
    latitude = float(loc[0])
    longitude = float(loc[1])
    city = data.get('city', 'Unknown')
    region = data.get('region', '')
    country = data.get('country', '')

    return latitude, longitude, f"{city}, {region}, {country}"

def show_on_map(lat, lon, location_name):
    map_obj = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup=location_name).add_to(map_obj)

    map_file = 'geo_location_map.html'
    map_obj.save(map_file)

    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open('file://' + os.path.realpath(map_file))

if __name__ == "__main__":
    latitude, longitude, location = get_location()
    show_on_map(latitude, longitude, location)
