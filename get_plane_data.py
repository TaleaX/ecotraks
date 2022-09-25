import requests

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
    print(u"id:[%s]\tday:[%s]\tduration:[%s]\tairline:[%s]\tstopOverDur[%s]\tcosts[%s]\tfare_id:[%s]" % (flight['id'],flight['departureDateTime'], flight['duration'], flight['airlineCodes'], flight['stopoverDurationMinutes'], fare_flight['price']['totalAmount'], fare_flight['tripId']))
