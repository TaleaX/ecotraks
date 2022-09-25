import json
import math

#Haversine Formula
def calc_dist(lat1, lat2, lon1, lon2):

    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = (2 * math.asin(math.sqrt(a))) * 6371
    return (c)

# def calc_emi(flight):

calc_dist()

# calc_emi()