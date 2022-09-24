import requests
import sqlite3

connection = sqlite3.connect("flights.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

req = requests.get('https://api.flightapi.io/onewaytrip/632ddcfccaa6ed253fcf9e6e/BER/MUC/2022-10-03/2/0/1/Economy/EUR')

data = req.json()

def get_fare_flight(flight_id):
    flight_id = flight_id.rstrip(":0").lstrip("BER-MUC:")
    for flight in data['fares']:
        tripId = flight['tripId'].split(':')[1].replace("-", ":")
        if (tripId == flight_id):
            return (flight)
    return (False)

for flight in data['legs']:
    fare_flight = get_fare_flight(flight['id'])
    if (not fare_flight):
        continue
    cursor.execute("insert into flights (airline, price, departure, duration) values (?, ?, ?, ?)", (flight['airlineCodes'][0], fare_flight['price']['totalAmount'],flight['departureDateTime'], flight['duration']))
    connection.commit()