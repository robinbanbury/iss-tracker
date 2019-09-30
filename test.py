#! /usr/bin/env python3

# pylint:disable=all

import datetime
import requests
# import twitter
from pprint import pprint
# from hidden import consumer_key, consumer_secret, access_token, access_secret


ip_data = requests.get('https://ipinfo.io').json()
pprint(ip_data)
city = ip_data['city']
region = ip_data['region']
lat, lon = ip_data['loc'].split(',')
print(lat, lon)

pass_data = requests.get(
    'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(lat, lon)).json()
pprint(pass_data)

pass_time = pass_data['response'][0]['risetime']
pass_duration = pass_data['response'][0]['duration']
now = datetime.datetime.now()
how_long = datetime.timedelta(seconds=pass_time - now.timestamp())
time = now+how_long
mins, secs = divmod(pass_duration, 60)
print(how_long, divmod(pass_duration, 60))

msg = 'ISS next over {city}({region}) in {how_long} for {mins}:{secs}, at {time}'.format(
    city=city,
    region=region,
    how_long=how_long,
    mins=mins,
    secs=secs,
    time=time)

print(msg)
