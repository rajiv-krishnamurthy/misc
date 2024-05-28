import requests
from datetime import datetime, timedelta
import pytz 
from astral.sun import sun
from astral import LocationInfo


# this is the URL for the API, use it for production.

url = 'https://ll.thespacedevs.com/2.2.0/launch/upcoming/'

#this is the URL for the API, use it for development.
#url = 'https://lldev.thespacedevs.com/2.2.0/launch/upcoming/'

response = requests.get(url)
data = response.json()


#create timzeone object for PST
pst=pytz.timezone('US/Pacific')
city = LocationInfo("San Jose", "USA")

# Filter launches by location
cape_canaveral = [launch for launch in data['results'] if 'Cape Canaveral' in launch['pad']['location']['name']]
vandenberg = [launch for launch in data['results'] if 'Vandenberg' in launch['pad']['location']['name']]

print("Cape Canaveral Launches:")
for launch in cape_canaveral:
    name = launch['name']
    window_start = launch['window_start']
    pst_window_start = datetime.strptime(window_start, '%Y-%m-%dT%H:%M:%S%z').astimezone(pst)
    launchdate = pst_window_start.strftime('%Y-%m-%d')
    launchtime = pst_window_start.strftime('%H:%M:%S')
    s = sun(city.observer, date=datetime.strptime(launchdate, '%Y-%m-%d'))
    sunset = s['sunset'].astimezone(pst)+timedelta(hours=7)
    sunset_flag = "| Before Sunset"
    if pst_window_start >= sunset:
        sunset_flag = "| After Sunset"
    print(name, pst_window_start, sunset_flag)
print("\nVandenberg Launches:")
for launch in vandenberg:
    name = launch['name']
    window_start = launch['window_start']
    pst_window_start = datetime.strptime(window_start, '%Y-%m-%dT%H:%M:%S%z').astimezone(pst)
    launchdate = pst_window_start.strftime('%Y-%m-%d')
    launchtime = pst_window_start.strftime('%H:%M:%S')
    s = sun(city.observer, date=datetime.strptime(launchdate, '%Y-%m-%d'))
    sunset = s['sunset'].astimezone(pst)+timedelta(hours=7)
    sunset_flag = "| Before Sunset"
    if pst_window_start >= sunset:
        sunset_flag = "| After Sunset"
    print(name, pst_window_start, sunset_flag)

# added a comment 
