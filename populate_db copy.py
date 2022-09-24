import requests
import sqlite3

connection = sqlite3.connect("flights.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
req = requests.get('https://api.flightapi.io/onewaytrip/632ddcfccaa6ed253fcf9e6e/BER/CDG/2022-10-03/2/0/1/Economy/EUR')

data = req.json()
for data_flight in data['legs']:
    cursor.execute("insert into flights (airline, price) values (?, ?)", (data_flight['airlineCodes'][0], 100))
    connection.commit()
