import googlemaps
import pprint
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyD-h61qVGj-pTEpw4NpfwQnYMW535-3VYo')


def get_commute_mins(origin, destination):
    response = gmaps.distance_matrix(origins=origin,
                                destinations=destination)

    time = response['rows'][0]['elements'][0]['duration']['text']
    value, dist.split(' ')


def time_formatter(time):
    t_list = time.split(' ')
    t_len = len(t_list)
    d = {}

    if t_len%2 != 0:
        raise Exception
        print("Time response elements from Google Routes API was not divisible by two.\n This function therefore can't parse the time data")

    while len(t_list) > 0:
        key, value = t_list.pop(1), t_list.pop(0)
        print(value, key)
        d.update({'unit': key, 'value': value})

    return d
