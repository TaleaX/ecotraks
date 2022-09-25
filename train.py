from ast import parse
import http.client
import json
from tokenize import triple_quoted
import requests

headers = {
    'DB-Client-Id': "f8740173874de790367f40ccb961fc0d",
    'DB-Api-Key': "2c12771757fa3f793669820ee00f29e9",
    'accept': "application/json"
    }

def location_id(depature, headers):
    location_endpoint = (f"https://apis.deutschebahn.com/db-api-marketplace/apis/fahrplan/v1/location/{depature}")
    res = requests.get(location_endpoint, headers=headers)
    data = res.json()
    # print(data)
    for elem in data:
        if depature in elem['name']:
            # print(elem['id'])
            return (elem['id'])

def train_id(loc_id, arrival, date, headers):
    url = (f"https://apis.deutschebahn.com/db-api-marketplace/apis/fahrplan/v1/departureBoard/{loc_id}?date={date}")
    res = requests.get(url, headers=headers)
    data = res.json()
    # print(data)
    train_list = []
    for elem in data:
        if arrival in elem['direction']:
            train_list.append(elem['detailsId'])
    # print(train_list)
    return(train_list)

def details_train(train_list, headers, depature, arrival):
    for i in range(len(train_list)):
        url = (f"https://apis.deutschebahn.com/db-api-marketplace/apis/fahrplan/v1/journeyDetails/{train_list[i]}")
        res = requests.get(url, headers=headers)
        data = res.json()
        print(u"NameTrain:", data[i]['train'], "DepatureTime:", get_depatureTime(depature, data), "ArrivalTime:", get_arrivalTime(arrival, data))
        
def get_depatureTime(depature, data):
    for elem in data:
        if depature in elem['stopName']:
            return (elem['depTime'])

def get_arrivalTime(arrival, data):
    for elem in data:
        if arrival in elem['stopName']:
            return (elem['arrTime'])

loc_id = location_id("Berlin Hbf", headers)
train_list = train_id(loc_id, "München Hbf", "2022-09-25T06:00:00", headers)
details_train(train_list, headers, "Berlin Hbf", "München Hbf")


