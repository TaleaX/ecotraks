import requests
import json

#berlin
lon_1 = 13.4
lat_1 = 52.5166666
#paris
lon_2 = 2.333
lat_2 = 48.8566
#münchen
lon_2 = 11.575
lat_2 = 48.13743
# call the OSMR API
r = requests.get(f"http://router.project-osrm.org/route/v1/car/{lon_1},{lat_1};{lon_2},{lat_2}?overview=false")
# then you load the response using the json library
# by default you get only one alternative so you access 0-th element of the `routes`
routes = json.loads(r.content)
route_1 = routes.get("routes")[0]
duration = route_1["duration"] / 60 # in min
if duration > 60:
    duration = duration / 60 #in stunden
distance = route_1["distance"] / 1000 # in km

#average co2 emission of a car: 19 kg / 100 km
numofpass = 1 #should be asked for
emission = distance * 19 / 100 / numofpass # in kg

distance = round(distance,2)
duration = round(duration,2)
emission = round(emission,2)
print("berlin-münchen distanz in km: ", distance)
print("berlin-münchen fahrzeit in h: ", duration)
print("berlin-münchen emission in kg: ", emission)