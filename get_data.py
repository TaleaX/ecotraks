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

def get_co2_emission(total_flight_time, amount_dep):
    return (float(total_flight_time / 60) * 90)

def get_flight_data(flight):
    res = 0
    data = []
    for segment in flight['segments']:
        res += segment['durationMinutes']
    data.append(res)
    data.append(len(flight['segments']))
    return (data)

for flight in data['legs']:
    fare_flight = get_fare_flight(flight['id'])
    if (not fare_flight):
        continue
    f_data = get_flight_data(flight)
    em = get_co2_emission(f_data[0], f_data[1])
    cursor.execute("insert into flights (airline, price, departure, duration, emission) values (?, ?, ?, ?, ?)", (flight['airlineCodes'][0], fare_flight['price']['totalAmount'],flight['departureDateTime'], flight['duration'], em))
    connection.commit()