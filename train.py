from ast import parse
import http.client
import json
from tokenize import triple_quoted
import requests
from datetime import time, timedelta, datetime

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
        dep_t = get_depatureTime(depature, data)
        arr_t = get_arrivalTime(arrival, data)
        print(u"NameTrain:", data[i]['train'], "DepatureTime:", dep_t, "ArrivalTime:", arr_t, "co2 kg:", co2_train(dep_t, arr_t))
        
def co2_train(dep_t, arr_t):
    dep_t = datetime.strptime(dep_t,'%H:%M')
    arr_t = datetime.strptime(arr_t,'%H:%M')
    dep_m = (dep_t.minute * 60 + dep_t.hour * 3600)
    arr_m = (arr_t.minute * 60 + arr_t.hour * 3600)
    #just dont ask where this number is from (its average number of co2 kg per second):D
    return("{:.2f}".format((arr_m - dep_m) * 0.0012882096))
    
def get_depatureTime(depature, data):
    for elem in data:
        if depature in elem['stopName']:
            return (elem['depTime'])

def get_arrivalTime(arrival, data):
    for elem in data:
        if arrival in elem['stopName']:
            return (elem['arrTime'])

#Call this function for and you get informations about trains
#Date needs to be jjjj-mm-ddThh:mm:ss
def iLikeTrain (departure, arrival, date, headers):
    loc_id = location_id(departure, headers)
    train_list = train_id(loc_id, arrival, date, headers)
    details_train(train_list, headers, departure, arrival)

iLikeTrain("Stuttgart Hbf", "München Hbf", "2022-09-25T06:00:00", headers)