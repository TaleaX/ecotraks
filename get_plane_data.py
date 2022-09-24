import requests

req = requests.get('https://api.flightapi.io/onewaytrip/632ddcfccaa6ed253fcf9e6e/BER/CDG/2022-10-03/2/0/1/Economy/EUR')

data = req.json()
for flight in data['legs']:
    print(u"day:[%s]\tduration:[%s]\tairline:[%s]\tstopOverDur[%s]" % (flight['departureDateTime'], flight['duration'], flight['airlineCodes'], flight['stopoverDurationMinutes']) )